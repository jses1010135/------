import csv
import os

def read_csv_file():
    if not os.path.exists('student_scores.csv'):
        print("檔案不存在，請確認 'student_scores.csv' 是否在正確位置。")
        return None
        
    try:
        data = []
        with open('student_scores.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
    except Exception as e:
        print(f"錯誤: {e}")
        return None

def adjust_grades(data, subject):
    if not data:
        print("沒有資料")
        return None
    
    adjusted_data = []
    for student in data:
        new_student = {}
        for key, value in student.items():
            new_student[key] = value
        
        if subject in new_student:
            try:
                score = float(new_student[subject])
                new_score = round((score ** 0.5) * 10, 2)
                new_student[subject] = new_score
            except:
                pass
        
        adjusted_data.append(new_student)
    
    return adjusted_data

def save_csv_file(filename, data):
    if not data:
        print("沒有資料")
        return
    
    try:
        fields = list(data[0].keys())
        
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for student in data:
                writer.writerow(student)
        
        print(f" {filename}")
    except Exception as e:
        print(f" {e}")

def calc_student_sum_avg(data, col):
    if not data:
        print("沒有資料")
        return None, 0
    
    scores = []
    total = 0
    
    for student in data:
        if col in student:
            try:
                score = float(student[col])
                scores.append(score)
                total += score
            except:
                pass
    
    count = len(scores)
    average = total / count if count > 0 else 0
    
    return scores, round(average, 2)

def frequency_distribution(data, col):
    if not data:
        return {}
    
    dist = {}
    
    for student in data:
        if col in student:
            try:
                score = float(student[col])
                if score in dist:
                    dist[score] += 1
                else:
                    dist[score] = 1
            except:
                pass
    
    return dist

def query(data, col, value):
    if not data:
        return []
    
    result = []
    for student in data:
        if col in student and student[col] == value:
            result.append(student)
    
    return result

def get_student_statistics(student):
    if not student:
        return {}, 0, 0
    
    subjects = {}
    total = 0
    count = 0
    
    for field, value in student.items():
        if field not in ["Student ID", "Name"]:
            try:
                score = float(value)
                subjects[field] = score
                total += score
                count += 1
            except:
                pass
    
    avg = total / count if count > 0 else 0
    
    return subjects, total, avg

def main():
    students = read_csv_file()
    if not students:
        print("找不到學生資料，程式結束")
        return
    
    student_id = input("請輸入查詢的學號: ")
    
    results = query(students, "Student ID", student_id)
    
    if not results:
        print(f"沒有找到 {student_id}")
        return
    
    student = results[0]
    
    subjects, total, average = get_student_statistics(student)
    
    print("\n學生")
    print(f"學號: {student.get('Student ID')}")
    print(f"姓名: {student.get('Name')}")
    
    print("\n成績資訊")
    for subject, score in subjects.items():
        print(f"{subject}: {score}")
    print(f"總分: {round(total, 2)}")
    print(f"平均值: {round(average, 2)}")

if __name__ == "__main__":
    main()