import csv
import random

def generate_subject_scores(mean_range=(50, 70), stddev_range=(10, 20), count=100):
    """使用常態分配產生一科的成績"""
    mean = random.uniform(*mean_range)
    stddev = random.uniform(*stddev_range)
    scores = []
    for _ in range(count):
        score = random.gauss(mean, stddev)
        score = max(0, min(100, round(score)))  # 限制在 0~100 並四捨五入
        scores.append(score)
    return scores, mean, stddev

def write_csv(filename, header, rows):
    """寫入 CSV 檔案"""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows)
        print(f"✅ 成功寫入 {len(rows)} 筆資料到 {filename}")
    except Exception as e:
        print(f"❌ 寫入 CSV 檔案時發生錯誤: {e}")

def generate_sample_data(filename, count=100):
    header = ['StudentID', 'Name', 'Chinese', 'English', 'Math', 'Physics']
    
    # 為每一科產生常態分布的成績
    chinese_scores, chinese_mean, chinese_std = generate_subject_scores()
    english_scores, english_mean, english_std = generate_subject_scores()
    math_scores, math_mean, math_std = generate_subject_scores()
    physics_scores, physics_mean, physics_std = generate_subject_scores()

    rows = []
    for i in range(count):
        student_id = f"S{i+1:03d}"
        name = f"John{i+1}"
        row = [
            student_id,
            name,
            chinese_scores[i],
            english_scores[i],
            math_scores[i],
            physics_scores[i],
        ]
        rows.append(row)

    write_csv(filename, header, rows)

    # 印出每科模擬的平均與標準差
    print("📊 每科模擬的平均與標準差如下：")
    print(f"  Chinese: μ={chinese_mean:.2f}, σ={chinese_std:.2f}")
    print(f"  English: μ={english_mean:.2f}, σ={english_std:.2f}")
    print(f"  Math   : μ={math_mean:.2f}, σ={math_std:.2f}")
    print(f"  Physics: μ={physics_mean:.2f}, σ={physics_std:.2f}")

if __name__ == '__main__':
    generate_sample_data('students_scores.csv')

