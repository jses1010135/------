import csv
import math

def load_csv(filename):
    """使用 csv.DictReader 讀取 CSV，回傳 list of dict"""
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = []
            for row in reader:
                # 將科目欄位轉為 float
                row['Chinese'] = float(row['Chinese'])
                row['English'] = float(row['English'])
                row['Math'] = float(row['Math'])
                row['Physics'] = float(row['Physics'])
                data.append(row)
            return data
    except Exception as e:
        print("❌ 讀取檔案失敗:", e)
        return []

def save_csv(filename, data):
    """將資料寫入 CSV 檔案"""
    fieldnames = ['StudentID', 'Name', 'Chinese', 'English', 'Math', 'Physics']
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow({
                    'StudentID': row['StudentID'],
                    'Name': row['Name'],
                    'Chinese': f"{row['Chinese']:.2f}",
                    'English': f"{row['English']:.2f}",
                    'Math': f"{row['Math']:.2f}",
                    'Physics': f"{row['Physics']:.2f}",
                })
        print("✅ 成績已寫入檔案")
    except Exception as e:
        print("❌ 寫入檔案失敗:", e)

def compute_weighted_scores(data):
    """計算每位學生的加權分數與加權平均"""
    for student in data:
        weighted = (
            student['Chinese'] * 1 +
            student['English'] * 2 +
            student['Math'] * 3 +
            student['Physics'] * 3
        )
        student['WeightedScore'] = weighted
        student['WeightedAverage'] = weighted / 9

def compute_individual_stats(data):
    """計算每位學生的四科平均與標準差"""
    for student in data:
        scores = [student['Chinese'], student['English'], student['Math'], student['Physics']]
        mean = sum(scores) / 4
        stddev = math.sqrt(sum((x - mean) ** 2 for x in scores) / 4)
        student['Mean'] = mean
        student['StdDev'] = stddev

def add_10_to_english(data):
    """將英文成績加10分（不超過100）"""
    for student in data:
        student['English'] = min(student['English'] + 10, 100)

def print_student_scores(data):
    """列印每位學生的加權分數與平均（對齊格式）"""
    print("=== 每位學生的加權成績與平均 ===")
    print("ID\tName\tWeighted\tAverage")
    for student in data:
        print(f"{student['StudentID']}\t{student['Name']}\t{student['WeightedScore']:.2f}\t\t{student['WeightedAverage']:.2f}")

def print_subject_stats(data):
    """列印每科的平均與標準差"""
    print("\n=== 每科平均與標準差 ===")
    subjects = ['Chinese', 'English', 'Math', 'Physics']
    for subject in subjects:
        scores = [s[subject] for s in data]
        mean = sum(scores) / len(scores)
        stddev = math.sqrt(sum((x - mean) ** 2 for x in scores) / len(scores))
        print(f"{subject}: 平均 = {mean:.2f}, 標準差 = {stddev:.2f}")

def main():
    filename = 'students_scores.csv'  # 可修改為你實際的檔案路徑
    data = load_csv(filename)
    if not data:
        return

    compute_weighted_scores(data)
    compute_individual_stats(data)
    print_student_scores(data)
    print_subject_stats(data)

    #add_10_to_english(data)
    #save_csv(filename, data)

if __name__ == '__main__':
    main()
