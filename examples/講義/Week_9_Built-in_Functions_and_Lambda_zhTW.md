# 第 9 週：內建函式與 Lambda

## 課程目標
- 熟悉 Python 的常用內建函式，包括 `map`, `filter`, 和 `sorted`。
- 理解並應用 Lambda 函式（匿名函式）簡化程式碼。
- 掌握函式式程式設計的基本概念。
- 透過實例練習，將內建函式與 Lambda 應用於實際問題。

## 1. 內建函式概述
Python 提供許多內建函式，無需額外導入即可使用，這些函式簡化常見操作。以下是本週重點介紹的函式：
- **`map(function, iterable)`**：將函式應用於可迭代物件的每個元素，傳回映射結果。
- **`filter(function, iterable)`**：根據函式的布林結果過濾可迭代物件的元素。
- **`sorted(iterable, key=None, reverse=False)`**：對可迭代物件排序，傳回新列表。

### 其他常用內建函式
- `len()`：傳回物件長度。
- `sum()`：計算數值序列的總和。
- `max()` / `min()`：傳回序列中的最大/最小值。
- `zip()`：將多個可迭代物件的元素配對。

## 2. 使用 map 函式
`map()` 將指定函式應用於可迭代物件的每個元素，傳回一個迭代器，通常搭配 `list()` 轉為列表。

### 程式碼範例 1：使用 map 轉換資料
```python
# 定義一個函式，將數字平方
def square(num):
    return num * num

# 使用 map 應用 square 函式
numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(f"平方結果：{squared}")

# 使用 map 將字串轉為大寫
words = ["apple", "banana", "cherry"]
upper_words = list(map(str.upper, words))
print(f"大寫結果：{upper_words}")
```
- **說明**：
  - `map(square, numbers)` 對每個數字應用 `square` 函式。
  - `str.upper` 是內建方法，可直接作為 `map` 的函式參數。
  - 使用 `list()` 將迭代器轉為列表以顯示結果。
- **預期輸出**：
```
平方結果：[1, 4, 9, 16, 25]
大寫結果：['APPLE', 'BANANA', 'CHERRY']
```

## 3. 使用 filter 函式
`filter()` 根據函式的布林結果（`True` 或 `False`）保留可迭代物件中的元素，傳回一個迭代器。

### 程式碼範例 2：使用 filter 篩選資料
```python
# 定義一個函式，檢查是否為偶數
def is_even(num):
    return num % 2 == 0

# 使用 filter 篩選偶數
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(f"偶數：{evens}")

# 使用 filter 篩選長度大於 5 的字串
words = ["apple", "banana", "cherry", "date"]
long_words = list(filter(lambda x: len(x) > 5, words))
print(f"長度大於 5 的字：{long_words}")
```
- **說明**：
  - `filter(is_even, numbers)` 保留 `is_even` 回傳 `True` 的元素。
  - 使用 `lambda` 函式（後續介紹）簡化篩選條件。
- **預期輸出**：
```
偶數：[2, 4, 6]
長度大於 5 的字：['banana', 'cherry']
```

## 4. 使用 sorted 函式
`sorted()` 對可迭代物件排序，傳回新排序列表，可透過 `key` 參數自訂排序規則，`reverse=True` 表示降序。

### 程式碼範例 3：使用 sorted 排序
```python
# 基本排序
numbers = [5, 2, 8, 1, 9]
sorted_nums = sorted(numbers)
print(f"升序排序：{sorted_nums}")
print(f"降序排序：{sorted(numbers, reverse=True)}")

# 按字串長度排序
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=len)
print(f"按長度排序：{sorted_words}")

# 按字典值排序
students = [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 90}, {"name": "Cathy", "score": 88}]
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
print(f"按成績降序排序：{sorted_students}")
```
- **說明**：
  - `sorted()` 傳回新列表，原資料不變（與 `list.sort()` 不同）。
  - `key=len` 按字串長度排序，`key=lambda x: x["score"]` 按字典的 `score` 排序。
- **預期輸出**：
```
升序排序：[1, 2, 5, 8, 9]
降序排序：[9, 8, 5, 2, 1]
按長度排序：['date', 'apple', 'banana', 'cherry']
按成績降序排序：[{'name': 'Bob', 'score': 90}, {'name': 'Cathy', 'score': 88}, {'name': 'Alice', 'score': 85}]
```

## 5. Lambda 函式（匿名函式）
Lambda 函式是一種簡短的匿名函式，使用 `lambda` 關鍵字定義，通常用於簡單操作或作為 `map`, `filter`, `sorted` 的參數。

### 語法
```python
lambda 參數: 表達式
```

### 程式碼範例 4：使用 Lambda 函式
```python
# 使用 Lambda 進行簡單計算
add = lambda x, y: x + y
print(f"加法：{add(3, 5)}")

# 結合 map 和 Lambda
numbers = [1, 2, 3, 4]
cubes = list(map(lambda x: x ** 3, numbers))
print(f"立方結果：{cubes}")

# 結合 filter 和 Lambda
numbers = [10, 15, 20, 25, 30]
large_nums = list(filter(lambda x: x > 20, numbers))
print(f"大於 20 的數字：{large_nums}")

# 結合 sorted 和 Lambda
pairs = [(1, "one"), (3, "three"), (2, "two")]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(f"按字串排序：{sorted_pairs}")
```
- **說明**：
  - `lambda x, y: x + y` 定義一個接受兩個參數的加法函式。
  - Lambda 函式簡化 `map`, `filter`, `sorted` 的函式定義。
- **預期輸出**：
```
加法：8
立方結果：[1, 8, 27, 64]
大於 20 的數字：[25, 30]
按字串排序：[(1, 'one'), (3, 'three'), (2, 'two')]
```

## 6. 課堂練習
請撰寫一個 Python 程式，完成以下任務：
1. 使用 `map` 和 Lambda 函式，將使用者輸入的一組數字（以空格分隔）轉為其兩倍。
2. 使用 `filter` 和 Lambda 函式，篩選出大於平均值的數字。
3. 使用 `sorted` 和 Lambda 函式，按使用者輸入的單詞的倒序字母排序（例如 "apple" 按 "elppa" 排序）。
4. 測試以上功能並輸出結果。

### 參考解答
```python
# 取得使用者輸入的數字
numbers = input("請輸入一組數字（以空格分隔）：")
numbers = [int(x) for x in numbers.split()]

# 任務 1：使用 map 計算兩倍
doubled = list(map(lambda x: x * 2, numbers))
print(f"兩倍結果：{doubled}")

# 任務 2：使用 filter 篩選大於平均值的數字
avg = sum(numbers) / len(numbers)
above_avg = list(filter(lambda x: x > avg, numbers))
print(f"平均值：{avg:.2f}, 大於平均值的數字：{above_avg}")

# 任務 3：按單詞倒序排序
words = input("請輸入一組單詞（以空格分隔）：").split()
sorted_words = sorted(words, key=lambda x: x[::-1])
print(f"按倒序字母排序：{sorted_words}")
```
- **說明**：
  - 列表推導式將輸入字串轉為整數列表。
  - `map(lambda x: x * 2, ...)` 計算每個數字的兩倍。
  - `filter(lambda x: x > avg, ...)` 保留大於平均值的數字。
  - `key=lambda x: x[::-1]` 按單詞反轉後的字母排序。
- **範例輸出**：
```
請輸入一組數字（以空格分隔）：1 2 3 4 5
兩倍結果：[2, 4, 6, 8, 10]
平均值：3.00, 大於平均值的數字：[4, 5]
請輸入一組單詞（以空格分隔）：apple banana cherry
按倒序字母排序：['banana', 'apple', 'cherry']
```

## 7. 常見問題與疑難排解
- **問題**：`TypeError: 'map' object is not subscriptable`。
  - **解決**：`map` 和 `filter` 傳回迭代器，需用 `list()` 轉為列表才能索引或顯示。
- **問題**：Lambda 函式語法錯誤。
  - **解決**：確保 `lambda 參數: 表達式` 格式正確，表達式只能是單一行。
- **問題**：`sorted` 結果不符合預期。
  - **解決**：檢查 `key` 函式的邏輯，或確認資料型態是否一致。

## 8. 回家作業
1. 撰寫一個程式，使用 `map` 和 Lambda 將一組字串的首字母轉為大寫（例如 `"apple"` 變為 `"Apple"`）。
2. 改進課堂練習程式，加入 `zip()` 將數字和其兩倍配對，輸出為字典。
3. 閱讀 Python 官方文件 [docs.python.org](https://docs.python.org/3/) 中的「Built-in Functions」和「Lambda Expressions」章節，了解更多細節。

## 9. 延伸學習
- 探索其他內建函式，如 `reduce()`（需從 `functools` 導入）用於累積計算。
- 嘗試結合 `map`, `filter`, `sorted` 實現複雜資料處理（如多條件排序）。
- 學習函式式程式設計的進階概念，如純函式和不可變資料。