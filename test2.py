import csv
def load_csv():
    with open('student_scores.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        data = [row for row in reader]
    return header, data
def caculate_individual_score(data):
    for row in data:
        chinese = int(row[2])
        english = int(row[3])
        math = int(row[4])
        physics = int(row[5])
        total = chinese*1 + english*2 + math*3 + physics*3
        w_avg = total / 9
        row.append(total)
        row.append(w_avg)
    return data
def caculateing_statistics(data):
    total_scores = [int(row[6]) for row in data]
    w_avg_scores = [float(row[7]) for row in data]
    
    # 計算 total 的平均值和標準差
    total_avg = sum(total_scores) / len(total_scores)
    total_variance = sum((x - total_avg) ** 2 for x in total_scores) / len(total_scores)
    total_stddev = (total_variance)**0.5
    
    # 計算 w_avg 的平均值和標準差
    w_avg_avg = sum(w_avg_scores) / len(w_avg_scores)
    w_avg_variance = sum((x - w_avg_avg) ** 2 for x in w_avg_scores) / len(w_avg_scores)
    w_avg_stddev = (w_avg_variance)**0.5
    
    return {
        'total': {'avg': total_avg, 'stddev': total_stddev},
        'w_avg': {'avg': w_avg_avg, 'stddev': w_avg_stddev}
    }
    
def main():
    header, data = load_csv()
    data = caculate_individual_score(data)
    statistics = caculateing_statistics(data)
    
    # 輸出結果
    print("個人總分和加權平均分數:")
    for row in data:
        print(f"ID: {row[0]}, Name: {row[1]}, Total: {row[6]}, Weighted Average: {row[7]}")
    
    print("\n統計資訊:")
    print(f"Total - 平均值: {statistics['total']['avg']}, 標準差: {statistics['total']['stddev']}")
    print(f"W_avg - 平均值: {statistics['w_avg']['avg']}, 標準差: {statistics['w_avg']['stddev']}")
if __name__ == "__main__":
    main()