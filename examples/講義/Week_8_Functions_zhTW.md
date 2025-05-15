# 第 8 週：函式定義與使用

## 課程目標
- 理解 Python 中函式的基本概念與作用。
- 學習如何定義函式、傳遞參數以及回傳值。
- 掌握本地與全域變數的作用範圍。
- 應用預設參數和關鍵字參數，提升函式的靈活性。
- 透過實例練習，設計和使用函式解決實際問題。

## 1. 函式概述
函式是一段命名、可重複使用的程式碼，用於執行特定任務。函式可以接受輸入（參數）、處理邏輯並返回結果（回傳值），提高程式碼的模組化與可讀性。

### 為什麼使用函式？
- **重複使用**：避免重複撰寫相同程式碼。
- **模組化**：將程式分解為小塊，易於維護。
- **可讀性**：透過有意義的函式名稱，使程式邏輯更清晰。

### 函式語法
```python
def 函式名稱(參數):
    # 函式主體
    return 回傳值  # 可選
```

## 2. 定義與呼叫函式
函式使用 `def` 關鍵字定義，呼叫函式時需使用函式名稱和適當的參數。

### 程式碼範例 1：簡單函式
```python
# 定義問候函式
def greet(name):
    message = f"您好，{name}！"
    return message

# 呼叫函式
result = greet("Alice")
print(result)
print(greet("Bob"))  # 直接輸出
```
- **說明**：
  - `def greet(name)` 定義一個接受單一參數的函式。
  - `return` 傳回結果，若無 `return`，則傳回 `None`。
  - 呼叫函式時傳入實際參數（例如 `"Alice"`）。
- **預期輸出**：
```
您好，Alice！
您好，Bob！
```

## 3. 參數與回傳值
函式可以接受多個參數，並透過 `return` 傳回結果。參數可以是任何型態（數字、字串、列表等）。

### 程式碼範例 2：多參數與回傳值
```python
# 定義計算面積的函式
def calculate_area(width, height):
    area = width * height
    return area

# 呼叫函式
rect_area = calculate_area(5, 3)
print(f"矩形面積：{rect_area} 平方單位")

# 傳遞不同型態的參數
print(f"另一個面積：{calculate_area(4.5, 2.5)}")
```
- **說明**：
  - 函式接受兩個參數 `width` 和 `height`，計算並回傳面積。
  - 回傳值可儲存到變數或直接使用。
- **預期輸出**：
```
矩形面積：15 平方單位
另一個面積：11.25
```

### 程式碼範例 3：多回傳值
```python
# 定義計算統計值的函式
def stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average  # 返回元組

# 呼叫函式
nums = [1, 2, 3, 4, 5]
total, avg = stats(nums)  # 解包回傳值
print(f"總和：{total}, 平均：{avg}")
```
- **說明**：
  - 使用逗號返回多個值，實際上返回一個元組。
  - 解包將回傳的元組賦值給多個變數。
- **預期輸出**：
```
總和：15, 平均：3.0
```

## 4. 本地與全域變數
- **本地變數**：在函式內定義，仅在函式內有效，函式結束後銷毀。
- **全域變數**：在函式外定義，全局可見，函式內可讀取但修改需用 `global` 關鍵字。

### 程式碼範例 4：本地與全域變數
```python
# 全域變數
count = 0

def increment():
    global count  # 聲明使用全域變數
    count += 1   # 修改全域變數
    local_var = 10  # 本地變數
    print(f"函式內：count = {count}, local_var = {local_var}")

# 呼叫函式
increment()
print(f"函式外：count = {count}")
# print(local_var)  # 錯誤：local_var 未定義
```
- **說明**：
  - `global count` 允許函式修改全域變數。
  - `local_var` 是本地變數，函式外無法存取。
- **預期輸出**：
```
函式內：count = 1, local_var = 10
函式外：count = 1
```

## 5. 預設參數與關鍵字參數
- **預設參數**：為參數設定預設值，若呼叫時未提供則使用預設值。
- **關鍵字參數**：呼叫函式時指定參數名稱，允許任意順序傳遞參數。

### 程式碼範例 5：預設參數與關鍵字參數
```python
# 定義帶預設參數的函式
def describe_person(name, age=18, city="未知"):
    return f"{name} 年齡 {age}，來自 {city}"

# 呼叫函式
print(describe_person("Alice"))  # 使用預設值
print(describe_person("Bob", 25))  # 提供部分參數
print(describe_person(name="Cathy", city="台北", age=30))  # 關鍵字參數
```
- **說明**：
  - `age=18` 和 `city="未知"` 是預設參數。
  - 關鍵字參數（如 `name="Cathy"`）允許任意順序傳遞。
- **預期輸出**：
```
Alice 年齡 18，來自 未知
Bob 年齡 25，來自 未知
Cathy 年齡 30，來自 台北
```

## 6. 可變參數
Python 支援可變數量的參數：
- `*args`：接受任意數量的位置參數，儲存為元組。
- `**kwargs`：接受任意數量的關鍵字參數，儲存為字典。

### 程式碼範例 6：可變參數
```python
# 定義接受可變參數的函式
def print_info(*args, **kwargs):
    print(f"位置參數：{args}")
    print(f"關鍵字參數：{kwargs}")

# 呼叫函式
print_info(1, 2, 3, name="Alice", age=20)
print_info("test", key="value")
```
- **說明**：
  - `*args` 收集所有位置參數（如 `1, 2, 3`）。
  - `**kwargs` 收集所有關鍵字參數（如 `name="Alice"`）。
- **預期輸出**：
```
位置參數：(1, 2, 3)
關鍵字參數：{'name': 'Alice', 'age': 20}
位置參數：('test',)
關鍵字參數：{'key': 'value'}
```

## 7. 課堂練習
請撰寫一個 Python 程式，完成以下任務：
1. 定義一個函式，接受一個數字列表，計算並返回最大值、最小值和平均值。
2. 定義另一個函式，接受姓名和任意數量的興趣（使用 `*args`），返回格式化的描述字串。
3. 使用預設參數定義一個函式，計算折扣價格（預設折扣率 10%）。
4. 測試以上函式，確保正確運行。

### 參考解答
```python
# 函式 1：計算列表統計值
def list_stats(numbers):
    if not numbers:  # 檢查空列表
        return None, None, None
    max_val = max(numbers)
    min_val = min(numbers)
    avg_val = sum(numbers) / len(numbers)
    return max_val, min_val, avg_val

# 函式 2：描述興趣
def describe_hobbies(name, *hobbies):
    hobbies_str = ", ".join(hobbies) if hobbies else "無"
    return f"{name} 的興趣是：{hobbies_str}"

# 函式 3：計算折扣價格
def calculate_discount(price, discount_rate=0.1):
    discounted_price = price * (1 - discount_rate)
    return discounted_price

# 測試函式
numbers = [10, 5, 8, 12, 3]
max_val, min_val, avg_val = list_stats(numbers)
print(f"最大值：{max_val}, 最小值：{min_val}, 平均值：{avg_val}")

hobby_desc = describe_hobbies("Alice", "閱讀", "跑步", "繪畫")
print(hobby_desc)

price = 1000
print(f"折扣後價格（10%）：{calculate_discount(price)}")
print(f"折扣後價格（20%）：{calculate_discount(price, 0.2)}")
```
- **說明**：
  - `list_stats` 使用內建函式 `max()`, `min()`, `sum()` 計算統計值。
  - `describe_hobbies` 使用 `*args` 收集興趣，`join()` 格式化輸出。
  - `calculate_discount` 使用預設參數計算折扣。
- **範例輸出**：
```
最大值：12, 最小值：3, 平均值：7.6
Alice 的興趣是：閱讀, 跑步, 繪畫
折扣後價格（10%）：900.0
折扣後價格（20%）：800.0
```

## 8. 常見問題與疑難排解
- **問題**：`NameError: name 'variable' is not defined`。
  - **解決**：檢查變數是否在函式內定義，或是否正確使用 `global`。
- **問題**：函式未返回預期結果。
  - **解決**：確認是否遺漏 `return`，或檢查回傳值是否正確賦值。
- **問題**：參數順序錯誤。
  - **解決**：確保位置參數在關鍵字參數之前，`*args` 和 `**kwargs` 放在最後。

## 9. 回家作業
1. 撰寫一個函式，接受一個字串和分隔符（預設為空格），返回分割後的單詞數量和單詞列表。
2. 改進課堂練習的 `list_stats` 函式，加入檢查輸入是否為數字列表（若無效則返回錯誤訊息）。
3. 閱讀 Python 官方文件 [docs.python.org](https://docs.python.org/3/) 中的「Defining Functions」章節，了解更多函式細節。

## 10. 延伸學習
- 探索函式的高階用法，如巢狀函式和閉包。
- 嘗試使用 `lambda` 函式（下一週介紹）簡化小型函式。
- 練習將複雜程式分解為多個小函式，提升程式結構化程度。