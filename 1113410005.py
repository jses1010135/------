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
    for column in data:
        col_avg = sum(column) / len(column)
        column_averages.append(col_avg)
    return column_averages

def main():
    data_matrix = gen_data()
    

    row_avgs = calc_row_average(data_matrix)
    print("每列平均值:")
    for i, avg in enumerate(row_avgs):
        print(f"列 {i+1}: {avg:.2f}")
    
    col_avgs = calc_column_average(data_matrix)
    print("\n每欄平均值:")
    for i, avg in enumerate(col_avgs):
        print(f"欄 {i+1}: {avg:.2f}")
if __name__ == "__main__":
    main()