def input_student():
    while True:
        students = []
        name= int(input("請輸入學生人數: "))  
    
    
        subjects = ["chinese", "english", "math", "physics"]
    
    

        if name.lower == "exit":
            break
        
        students.append(name)  
        
        scores = []
        for subject in subjects:
            score = float(input(f"請輸入{name}的{subject}成績: "))
            scores.append(score)
        students.append(scores)  
        students.append(students)
    return students


def calculate_individual_average(students):
    weights = [1, 2, 3, 3]  
    result = []
    
    for student in students:
        name = student[0]
        scores = student[1]  
        
        total_score = 0
        for score in scores:
            total_score += score
        
        weighted_total = 0
        total_weights = 0
        
        for i in range(len(scores)):
            weighted_total += scores[i] * weights[i]
            total_weights += weights[i]
        weighted_avg = weighted_total / total_weights
        

        result.append([name, total_score, weighted_avg])
    
    return result


def calculate_statistics(result):
    # 提取所有學生的總分和加權平均值
    total_scores = [student[1] for student in result]
    w_avgs = [student[2] for student in result]  # 修正：取加權平均值，索引應為2
    
    # 計算總分的統計值
    total_mean = sum(total_scores) / len(total_scores) if total_scores else 0
    total_variance = sum((x - total_mean) ** 2 for x in total_scores) / len(total_scores) if total_scores else 0
    total_std_dev = total_variance ** 0.5
    
    # 計算加權平均值的統計值
    w_avg_mean = sum(w_avgs) / len(w_avgs) if w_avgs else 0
    w_avg_variance = sum((x - w_avg_mean) ** 2 for x in w_avgs) / len(w_avgs) if w_avgs else 0
    w_avg_std_dev = w_avg_variance ** 0.5
    
    # 返回統計結果列表 [總分平均, 總分變異數, 總分標準差, 加權平均平均值, 加權平均變異數, 加權平均標準差]
    return [total_mean, total_variance, total_std_dev, w_avg_mean, w_avg_variance, w_avg_std_dev]
    

def main():
    students = input_student()
    data = calculate_individual_average(students)
    statistics = calculate_statistics(data)  # 修正：函式名稱拼寫錯誤
    
    # 顯示每位學生資料
    print("\n學生資料:")
    for student in data:
        print(f"姓名: {student[0]}, 總分: {student[1]}, 加權平均: {student[2]:.2f}")
    
    # 修正：正確顯示統計資料
    print(f"總分平均: {statistics[0]:.2f}, 變異數: {statistics[1]:.2f}, 標準差: {statistics[2]:.2f}")
    print(f"加權平均平均值: {statistics[3]:.2f}, 變異數: {statistics[4]:.2f}, 標準差: {statistics[5]:.2f}")
    

if __name__ == "__main__":
    main()