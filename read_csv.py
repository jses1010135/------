import csv

def read_csv():
    data=[]
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)  # 跳過標題行
        #print(f"標題：{header}")
        for row in reader:
            #print(f"學生：{row[0]}, 數學：{row[1]}, 英文：{row[2]}")
            data.append(row)
    return data,header
def write_csv(data,header):

    with open("new_students.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        writer.writerows(header)
        for row in data:
            writer.writerow(row)
    return data,header

def append_csv(data):
    with open("new_students.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
    return data
def caculate_average(data):
    for row in data:
        math_score = int(row[1])
        english_score = int(row[2])
        average = (math_score + english_score) / 2
        row.append(average)
    return data


def main():
    data = [
    ["David", 92, 87],
    ["Eve", 88, 91]
]
    d,h=read_csv()
    write_csv(d,h)
    append_csv(data)
    print(f"標題：{h[0]}")
    for row in d:
        print(f"學生：{row[0]}")

if __name__ == "__main__":
    main()