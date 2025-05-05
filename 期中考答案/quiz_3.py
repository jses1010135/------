# quiz_3.py

def input_grades():
    students = []
    while True:
        name = input("請輸入學生姓名（輸入 'exit' 結束）：")
        if name.lower() == 'exit': # 使用 lower() 方法將輸入轉為小寫，這樣可以避免大小寫問題
            break
        chinese = float(input("國文成績："))
        english = float(input("英文成績："))
        math = float(input("數學成績："))
        physics = float(input("物理成績："))
        students.append([name, chinese, english, math, physics])
    return students

def calculate_individual_scores(data):
    results = []
    for student in data:
        name, chinese, english, math, physics = student
        total = chinese * 1 + english * 2 + math * 3 + physics * 3
        w_avg = total / 9
        results.append([name, total, w_avg])
    return results

# 自建統計函式
def my_avg(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)

def my_var(data):
    mean = my_avg(data)
    total = 0
    for x in data:
        total += (x - mean) ** 2
    return total / len(data)

def my_stddev(data):
    return my_var(data) ** 0.5

def calculating_statistics(data):
    total_scores = [item[1] for item in data]
    w_avg_scores = [item[2] for item in data]

    stats = {
        'total': {
            'avg': my_avg(total_scores),
            'var': my_var(total_scores),
            'stddev': my_stddev(total_scores)
        },
        'w_avg': {
            'avg': my_avg(w_avg_scores),
            'var': my_var(w_avg_scores),
            'stddev': my_stddev(w_avg_scores)
        }
    }
    return stats

def main():
    # 讀取成績
    student_data = input_grades()
    
    # 計算個人成績
    scores = calculate_individual_scores(student_data)
    
    # 計算統計數據
    stats = calculating_statistics(scores)

    # 輸出統計結果
    print("\n=== 成績統計 ===")
    print("總分:")
    print(f"  平均值：{stats['total']['avg']:.2f}")
    print(f"  變異數：{stats['total']['var']:.2f}")
    print(f"  標準差：{stats['total']['stddev']:.2f}")
    print("加權平均:")
    print(f"  平均值：{stats['w_avg']['avg']:.2f}")
    print(f"  變異數：{stats['w_avg']['var']:.4f}")
    print(f"  標準差：{stats['w_avg']['stddev']:.4f}")

# 程式進入點
if __name__ == "__main__":
    main()

