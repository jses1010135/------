# quiz_2.py

# 建立空的清單
data = []

# 輸入 10 個數字並加入清單
print("請輸入 10 個數字：")
for i in range(10):
    num = float(input(f"輸入第 {i+1} 個數字："))
    data.append(num)

# 使用氣泡排序法對清單進行由小到大排序
n = len(data)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if data[j] > data[j + 1]:
            # 交換位置
            data[j], data[j + 1] = data[j + 1], data[j]

# 印出排序後的結果
print("排序後的數字為：")
for num in data:
    print(num)
