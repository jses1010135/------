import csv
import os

def read_csv(filename="students.csv"):
    data = []
    # 檢查文件是否存在，不存在則創建一個基本結構
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "math", "english"])
        return [], ["name", "math", "english"]
        
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)  # 跳過標題行
        for row in reader:
            data.append(row)
    return data, header

def write_csv(header, data, filename="new_students.csv"):
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for row in data:
            writer.writerow(row)
    return data

def append_to_students_csv(data, filename="students.csv"):
    """將新學生資料添加到students.csv"""
    with open(filename, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
    
def main():
    # 建議先清空舊檔案，重新開始
    # 新學生資料
    new_students = [
        ["David", 92, 87],
        ["Eve", 88, 91]
    ]
    
    # 先清空並重建 students.csv
    with open("students.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "math", "english"])
        writer.writerow(["alice", 85, 90])
        writer.writerow(["bob", 78, 82])
        writer.writerow(["cathy", 95, 88])
    
    # 步驟1: 將新學生資料添加到students.csv
    append_to_students_csv(new_students)
    
    # 步驟2: 讀取更新後的students.csv
    header, data = read_csv()
    
    # 步驟3: 將完整資料寫入new_students.csv
    write_csv(header, data)
    
    print("操作成功完成！")
    print(f"標題：{header}")
    print("學生列表：")
    for row in data:
        print(f"學生：{row[0]}, 數學：{row[1]}, 英文：{row[2]}")

if __name__ == "__main__":
    main()