import csv
import math

def load_csv(filename):
    """讀取 CSV 並回傳二維 list，第一列為欄位名稱，數值欄位轉為 float"""
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data = []
            for i, row in enumerate(reader):
                if i == 0:
                    data.append(row)  # header
                else:
                    # 學號與姓名為字串，2~5 為成績欄位轉 float
                    converted_row = row[:2] + [float(x) for x in row[2:6]]
                    data.append(converted_row)
            return data
    except Exception as e:
        print("❌ 讀取 CSV 錯誤:", e)
        return []

def save_csv(filename, data):
    """將資料重新寫回 CSV 檔案"""
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                # 將 float 四捨五入保留兩位
                formatted_row = [f"{x:.2f}" if isinstance(x, float) else x for x in row]
                writer.writerow(formatted_row)
        print("✅ 成績已寫回 CSV 檔案")
    except Exception as e:
        print("❌ 寫入 CSV 檔案錯誤:", e)

def compute_weighted_scores(data):
    """計算每位學生的加權總分與加權平均，並將結果加入每列"""
    for row in data[1:]:
        try:
            chinese = row[2]
            english = row[3]
            math = row[4]
            physics = row[5]
            weighted_score = chinese * 1 + english * 2 + math * 3 + physics * 3
            weighted_avg = weighted_score / 9
            row.append(weighted_score)
            row.append(weighted_avg)
        except Exception as e:
            print("⚠️ 加權計算錯誤:", e)

def compute_individual_stats(data):
    """計算每位學生的四科平均與標準差，並加入每列"""
    for row in data[1:]:
        try:
            scores = row[2:6]
            mean = sum(scores) / 4
            stddev = math.sqrt(sum((x - mean) ** 2 for x in scores) / 4)
            row.append(mean)
            row.append(stddev)
        except Exception as e:
            print("⚠️ 個人統計錯誤:", e)

def add_10_to_english(data):
    """將英文成績加10分（最多不超過100）"""
    for row in data[1:]:
        row[3] = min(row[3] + 10, 100)

def print_student_scores(data):
    """列印每位學生的加權分數與平均"""
    print("=== 每位學生的加權成績與平均 ===")
    print("ID\tName\tWeighted\tAverage")
    for row in data[1:]:
        print(f"{row[0]}\t{row[1]}\t{row[6]:.2f}\t\t{row[7]:.2f}")

def print_subject_stats(data):
    """計算每科的全班平均與標準差"""
    print("\n=== 每科平均與標準差 ===")
    subject_names = ['Chinese', 'English', 'Math', 'Physics']
    subject_indices = [2, 3, 4, 5]
    num_students = len(data) - 1

    for name, idx in zip(subject_names, subject_indices):
        try:
            scores = [row[idx] for row in data[1:]]
            mean = sum(scores) / num_students
            stddev = math.sqrt(sum((x - mean) ** 2 for x in scores) / num_students)
            print(f"{name}: 平均 = {mean:.2f}, 標準差 = {stddev:.2f}")
        except Exception as e:
            print(f"⚠️ {name} 科統計錯誤:", e)

def main():
    filename = 'students_scores.csv'  # 修改為你的檔案路徑
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
