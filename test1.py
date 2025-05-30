import csv
import random

def generate_scores(count=100, min_mean=50, max_mean=60, min_dev=70, max_dev=80):
    mean = random.uniform(min_mean, max_mean)
    std_dev = random.uniform(min_dev, max_dev)
    
    scores = []
    for _ in range(count):
        score = random.gauss(mean, std_dev)
        score = round(max(0, min(100, score)))
        scores.append(score)
    
    return scores

def generate_data(count):
    data = []
    scores = generate_scores(count)
    for i in range(1, count + 1): 
        student_id = f"id_{i}"#
        name = f"name_{i}"
        
        chinese = scores[i - 1] 
        english = scores[i - 1]
        math = scores[i - 1]
        physics = scores[i - 1]
        
        student_data = [student_id, name, chinese, english, math, physics]
        data.append(student_data)
    
    return data

def write_csv(filename, header, data):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(data)

def main():
    student_count = 100
    header = ["ID", "Name", "Chinese", "English", "Math", "Physics"]
    output_file = "student_scores.csv"
    
    student_data = generate_data(student_count)
    
    write_csv(output_file, header, student_data)


if __name__ == "__main__":
    main()