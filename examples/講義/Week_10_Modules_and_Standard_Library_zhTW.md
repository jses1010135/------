# 第 10 週：模組與標準庫

## 課程目標
- 理解 Python 模組的概念與作用。
- 學習如何導入和使用標準庫模組，包括 `math`、`random` 和 `datetime`。
- 掌握創建和使用自訂模組的方法。
- 透過實例練習，應用模組和標準庫解決實際問題。

## 1. 模組概述
模組是包含 Python 程式碼的檔案（通常以 `.py` 結尾），用於組織和重複使用程式碼。模組可以包含函式、類別或變數，通過 `import` 關鍵字引入程式。

### 為什麼使用模組？
- **程式碼組織**：將相關功能分離到不同檔案，增強可讀性與維護性。
- **重複使用**：將常用功能封裝為模組，跨程式使用。
- **標準庫**：Python 提供豐富的標準庫模組，無需自行實現複雜功能。

### 導入模組的方式
- `import module`：導入整個模組。
- `from module import item`：導入模組中的特定項目。
- `import module as alias`：為模組指定別名。
- `from module import *`：導入模組所有內容（不建議，易造成命名衝突）。

## 2. 使用標準庫模組
Python 的標準庫包含許多模組，本週介紹三個常用模組：`math`、`random` 和 `datetime`。

### 2.1 math 模組
`math` 模組提供數學運算功能，如三角函式、對數、常數等。

#### 程式碼範例 1：使用 math 模組
```python
import math

# 常用數學函式
print(f"圓周率：{math.pi}")
print(f"e 的值：{math.e}")
print(f"2 的平方根：{math.sqrt(2)}")
print(f"30 度的正弦值：{math.sin(math.radians(30))}")
print(f"5 的階乘：{math.factorial(5)}")

# 取整函式
number = 3.7
print(f"向上取整：{math.ceil(number)}")
print(f"向下取整：{math.floor(number)}")
```
- **說明**：
  - `math.pi` 和 `math.e` 是常數。
  - `math.radians()` 將角度轉為弧度，供三角函式使用。
  - `math.factorial(n)` 計算 n 的階乘。
- **預期輸出**：
```
圓周率：3.141592653589793
e 的值：2.718281828459045
2 的平方根：1.4142135623730951
30 度的正弦值：0.49999999999999994
5 的階乘：120
向上取整：4
向下取整：3
```

### 2.2 random 模組
`random` 模組用於生成隨機數或隨機選擇，常用於遊戲、模擬等場景。

#### 程式碼範例 2：使用 random 模組
```python
import random

# 生成隨機數
print(f"0 到 1 之間的隨機浮點數：{random.random()}")
print(f"1 到 10 之間的隨機整數：{random.randint(1, 10)}")
print(f"0 到 100 之間，步進 5 的隨機數：{random.randrange(0, 101, 5)}")

# 隨機選擇
fruits = ["蘋果", "香蕉", "橘子", "葡萄"]
print(f"隨機水果：{random.choice(fruits)}")
print(f"隨機選 2 個水果：{random.sample(fruits, 2)}")

# 打亂列表
random.shuffle(fruits)
print(f"打亂後的列表：{fruits}")
```
- **說明**：
  - `random.random()` 生成 0 到 1 的浮點數。
  - `random.randint(a, b)` 生成 a 到 b 的整數（包含 b）。
  - `random.choice()` 和 `random.sample()` 用於隨機選擇。
  - `random.shuffle()` 就地打亂列表。
- **預期輸出**（隨機結果，僅供參考）：
```
0 到 1 之間的隨機浮點數：0.723942837
1 到 10 之間的隨機整數：7
0 到 100 之間，步進 5 的隨機數：45
隨機水果：香蕉
隨機選 2 個水果：['蘋果', '葡萄']
打亂後的列表：['葡萄', '橘子', '蘋果', '香蕉']
```

### 2.3 datetime 模組
`datetime` 模組用於處理日期和時間，支援日期計算、格式化等功能。

#### 程式碼範例 3：使用 datetime 模組
```python
from datetime import datetime, timedelta

# 取得當前時間
now = datetime.now()
print(f"當前時間：{now}")

# 格式化日期
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"格式化時間：{formatted_date}")

# 日期計算
one_week_later = now + timedelta(days=7)
print(f"一週後：{one_week_later}")

# 解析日期字串
date_str = "2025-05-12"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print(f"解析後的日期：{parsed_date}")
```
- **說明**：
  - `datetime.now()` 取得當前日期和時間。
  - `strftime()` 將日期格式化為字串，`strptime()` 將字串解析為日期。
  - `timedelta` 用於日期加減。
- **預期輸出**（假設當前日期為 2025-05-12）：
```
當前時間：2025-05-12 10:30:45.123456
格式化時間：2025-05-12 10:30:45
一週後：2025-05-19 10:30:45.123456
解析後的日期：2025-05-12 00:00:00
```

## 3. 創建自訂模組
自訂模組是一個包含函式、變數或類別的 `.py` 檔案，可被其他程式導入。

### 程式碼範例 4：創建與使用自訂模組
假設創建一個名為 `utils.py` 的模組，包含以下內容：
```python
# utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159
```

現在在另一個程式中使用 `utils` 模組：
```python
# main.py
import utils

# 使用模組中的函式
print(f"加法：{utils.add(3, 5)}")
print(f"乘法：{utils.multiply(4, 2)}")

# 使用模組中的變數
print(f"圓周率：{utils.PI}")
```
- **說明**：
  - `utils.py` 定義了兩個函式和一個常數。
  - 在 `main.py` 中透過 `import utils` 導入，並使用點運算子（`.`）存取模組內容。
- **預期輸出**：
```
加法：8
乘法：8
圓周率：3.14159
```

### 注意事項
- 模組檔案需與主程式位於同一目錄，或指定正確路徑。
- 可使用 `import utils as u` 簡化名稱。
- 若模組內容改變，需重新執行程式以載入最新版本。

## 4. 模組導入進階
### 選擇性導入
從模組導入特定項目，減少命名空間污染。

#### 程式碼範例 5：選擇性導入
```python
from math import sqrt, pi
from random import choice

print(f"16 的平方根：{sqrt(16)}")
print(f"圓周率：{pi}")
print(f"隨機選擇：{choice(['紅', '藍', '綠'])}")
```
- **說明**：
  - 僅導入 `sqrt` 和 `pi`，無需使用 `math.` 前綴。
  - 直接使用 `choice` 函式。
- **預期輸出**（隨機結果，僅供參考）：
```
16 的平方根：4.0
圓周率：3.141592653589793
隨機選擇：藍
```

### 模組路徑
若模組不在當前目錄，可使用 `sys.path` 或相對/絕對路徑導入。

## 5. 課堂練習
請撰寫一個 Python 程式，完成以下任務：
1. 使用 `random` 模組生成 10 個 1 到 100 的隨機整數，儲存到列表。
2. 使用 `math` 模組計算列表中所有數字的平方根之和。
3. 使用 `datetime` 模組記錄程式執行時間，並格式化輸出。
4. 創建一個自訂模組，包含一個計算圓面積的函式，然後在主程式中呼叫。

### 參考解答
假設自訂模組 `geometry.py`：
```python
# geometry.py
import math

def circle_area(radius):
    return math.pi * radius ** 2
```

主程式：
```python
import random
import math
import datetime
import geometry

# 任務 1：生成隨機數列表
numbers = [random.randint(1, 100) for _ in range(10)]
print(f"隨機數列表：{numbers}")

# 任務 2：計算平方 landowner和
sqrt_sum = sum(math.sqrt(num) for num in numbers)
print(f"平方根之和：{sqrt_sum:.2f}")

# 任務 3：記錄執行時間
start_time = datetime.datetime.now()
print(f"程式開始時間：{start_time.strftime('%Y-%m-%d %H:%M:%S')}")

# 任務 4：使用自訂模組計算圓面積
radius = 5
area = geometry.circle_area(radius)
print(f"半徑 {radius} 的圓面積：{area:.2f}")
```
- **說明**：
  - 列表推導式生成隨機數。
  - `sum(math.sqrt(num) ...)` 計算平方根總和。
  - `datetime.now()` 記錄時間，`strftime()` 格式化。
  - `geometry.circle_area` 呼叫自訂模組函式。
- **範例輸出**（隨機結果，僅供參考）：
```
隨機數列表：[23, 45, 67, 12, 89, 34, 56, 78, 9, 41]
平方根之和：62.34
程式開始時間：2025-05-12 10:30:45
半徑 5 的圓面積：78.54
```

## 6. 常見問題與疑難排解
- **問題**：`ModuleNotFoundError: No module named 'module'`。
  - **解決**：確認模組檔案是否存在、名稱正確，且位於正確路徑。
- **問題**：模組內容未更新。
  - **解決**：重新執行程式，或使用 `importlib.reload()`（進階用法）。
- **問題**：`random` 結果總是相同。
  - **解決**：檢查是否誤用 `random.seed()`，或移除固定種子。

## 7. 回家作業
1. 撰寫一個程式，使用 `random` 模組模擬擲骰子 100 次，統計每個點數的出現次數。
2. 改進課堂練習程式，加入 `datetime` 計算程式執行耗時（結束時間 - 開始時間）。
3. 閱讀 Python 官方文件 [docs.python.org](https://docs.python.org/3/) 中的「Modules」和「Standard Library」章節，了解更多模組。

## 8. 延伸學習
- 探索其他標準庫模組，如 `os`（檔案操作）、`sys`（系統參數）。
- 學習模組打包與發佈，創建可分享的 Python 套件。
- 嘗試使用 `time` 模組實現簡單計時功能。