# quiz_1.py

# 輸入 a 與 b 兩個浮點數
a = float(input("請輸入 a 的值："))
b = float(input("請輸入 b 的值："))

# 檢查分母是否為 0，避免除以零錯誤
if a**2 - b**2 == 0:
    print("錯誤：分母為 0，無法計算。")
else:
    # 計算 c 的值
    c = (a**2 + b**2) / (a**2 - b**2)
    # 列印結果
    print("c 的數值為：", c)
