import random as r
r.seed(65,20)
def gen_data():
    data=[]
    for _ in range (100):
        row=[]
        for _ in range(10):
            row.append(r.random())
        data.append(row)
    return data
def calc_row_average(data):
    row_averages = []
    for row in data:
        row_avg = sum(row) / len(row)
        row_averages.append(row_avg)
    return row_averages

def calc_column_average(data):
    column_averages = []
    for col_idx in range(len(data[0])):
        column_values = [row[col_idx] for row in data] # 
        col_avg = sum(column_values) / len(column_values)
        column_averages.append(col_avg)
    return column_averages

def main():
    data_matrix = gen_data()
    

    row_avgs = calc_row_average(data_matrix)
    print("每列平均值:")
    i = 0
    while i < len(row_avgs):
        avg = row_avgs[i]
        print(f"列 {i+1}: {avg:.2f}")
        i += 1
    col_avgs = calc_column_average(data_matrix)
    print("\n每欄平均值:")
    i = 0
    while i < len(col_avgs):
        avg = col_avgs[i]
        print(f"欄 {i+1}: {avg:.2f}")
        i += 1
if __name__ == "__main__":
    main()