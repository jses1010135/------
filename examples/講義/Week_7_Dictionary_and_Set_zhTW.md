# 第 7 週：Dictionary 與 Set

## 課程目標
- 理解 Python 中字典 (`dict`) 和集合 (`set`) 的基本概念與用途。
- 掌握字典的建立、鍵值查找與常用方法。
- 學習集合的建立與集合運算（如聯集、交集、差集）。
- 透過實例練習，應用字典和集合解決實際問題。

## 1. 字典與集合概述
字典和集合是 Python 中用於儲存和操作資料的內建資料結構，適用於不同的場景：
- **字典 (`dict`)**：儲存鍵值對（key-value pairs），透過鍵快速查找對應的值，定義使用大括號 `{}`。
- **集合 (`set`)**：儲存唯一的元素，無序且無重複，支援集合運算，定義使用大括號 `{}` 或 `set()`。

### 共同特性
- 都是可迭代物件，可用 `for` 迴圈遍歷。
- 都支援檢查元素是否存在（使用 `in` 運算子）。
- 字典的鍵和集合的元素必須是**可雜湊 (hashable)** 的（例如數字、字串、元組，但不可為列表）。

## 2. 字典操作
字典是一種可變資料結構，鍵必須唯一且不可變，值可以是任意型態。

### 建立字典
- 使用大括號：`{key1: value1, key2: value2}`
- 使用 `dict()` 建構函式：`dict(key1=value1, key2=value2)`

### 常用方法
- `get(key, default)`：取得鍵對應的值，若鍵不存在傳回預設值。
- `keys()`：傳回所有鍵的視圖。
- `values()`：傳回所有值的視圖。
- `items()`：傳回所有鍵值對的視圖。
- `update(dict)`：更新或添加鍵值對。
- `pop(key)`：移除指定鍵並傳回其值。
- `clear()`：清空字典。

### 程式碼範例 1：字典基本操作
```python
# 建立字典
student = {"name": "Alice", "age": 20, "grade": "A"}

# 訪問值
print(f"姓名：{student['name']}")
print(f"年齡：{student.get('age')}")

# 添加/修改鍵值對
student["id"] = "S123"
student["age"] = 21
print(f"更新後：{student}")

# 移除鍵值對
grade = student.pop("grade")
print(f"移除的成績：{grade}, 字典：{student}")

# 遍歷字典
print("鍵值對遍歷：")
for key, value in student.items():
    print(f"{key}: {value}")
```
- **說明**：
  - 使用 `[]` 或 `get()` 存取值，`get()` 可避免鍵不存在時的錯誤。
  - `items()` 提供鍵值對，適合用於迴圈。
- **預期輸出**：
```
姓名：Alice
年齡：20
更新後：{'name': 'Alice', 'age': 21, 'grade': 'A', 'id': 'S123'}
移除的成績：A, 字典：{'name': 'Alice', 'age': 21, 'id': 'S123'}
鍵值對遍歷：
name: Alice
age: 21
id: S123
```

### 程式碼範例 2：巢狀字典
```python
# 巢狀字典（模擬學生資料庫）
students = {
    "S001": {"name": "Alice", "scores": [85, 90, 88]},
    "S002": {"name": "Bob", "scores": [78, 82, 80]}
}

# 訪問巢狀資料
print(f"Alice 的數學成績：{students['S001']['scores'][0]}")

# 修改資料
students["S002"]["scores"][1] = 85
print(f"更新後的 Bob 成績：{students['S002']['scores']}")

# 添加新學生
students["S003"] = {"name": "Cathy", "scores": [90, 95, 92]}
print(f"添加新學生後：{students}")
```
- **說明**：
  - 巢狀字典允許儲存複雜資料結構。
  - 使用多層索引（如 `['S001']['scores'][0]`）存取內層資料。
- **預期輸出**：
```
Alice 的數學成績：85
更新後的 Bob 成績：[78, 85, 80]
添加新學生後：{'S001': {'name': 'Alice', 'scores': [85, 90, 88]}, 'S002': {'name': 'Bob', 'scores': [78, 85, 80]}, 'S003': {'name': 'Cathy', 'scores': [90, 95, 92]}}
```

## 3. 集合操作
集合是一種無序、不可重複的資料結構，常用於去重或執行集合運算。

### 建立集合
- 使用大括號：`{item1, item2, ...}`
- 使用 `set()`：`set([item1, item2, ...])`
- 注意：空集合必須使用 `set()`，因為 `{}` 表示空字典。

### 常用方法
- `add(item)`：添加元素。
- `remove(item)`：移除元素，若不存在則引發錯誤。
- `discard(item)`：移除元素，若不存在不報錯。
- `clear()`：清空集合。
- `union()` 或 `|`：聯集。
- `intersection()` 或 `&`：交集。
- `difference()` 或 `-`：差集。
- `symmetric_difference()` 或 `^`：對稱差集。

### 程式碼範例 3：集合基本操作
```python
# 建立集合
fruits = {"蘋果", "香蕉", "橘子"}
print(f"初始集合：{fruits}")

# 添加元素
fruits.add("葡萄")
print(f"添加後：{fruits}")

# 移除元素
fruits.discard("香蕉")
print(f"移除後：{fruits}")

# 檢查元素
print(f"蘋果是否在集合中：{'蘋果' in fruits}")

# 集合運算
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"聯集：{set1 | set2}")
print(f"交集：{set1 & set2}")
print(f"差集（set1 - set2）：{set1 - set2}")
print(f"對稱差集：{set1 ^ set2}")
```
- **說明**：
  - 集合自動去除重複元素。
  - 集合運算符（如 `|`、`&`）簡化聯集、交集等操作。
- **預期輸出**：
```
初始集合：{'橘子', '蘋果', '香蕉'}
添加後：{'橘子', '葡萄', '蘋果', '香蕉'}
移除後：{'橘子', '葡萄', '蘋果'}
蘋果是否在集合中：True
聯集：{1, 2, 3, 4, 5, 6}
交集：{3, 4}
差集（set1 - set2）：{1, 2}
對稱差集：{1, 2, 5, 6}
```

## 4. 字典與集合的應用場景
- **字典**：
  - 儲存結構化資料（如學生資料、配置文件）。
  - 快速查找（鍵值對的時間複雜度為 O(1)）。
  - 計數或映射（例如單詞頻率統計）。
- **集合**：
  - 去除重複資料（如唯一用戶 ID）。
  - 執行集合運算（如共同興趣、差異分析）。
  - 檢查成員資格（高效的 `in` 操作）。

### 程式碼範例 4：計數應用（字典）
```python
# 統計單詞出現次數
sentence = input("請輸入一句話：")
words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"單詞計數：{word_count}")
```
- **說明**：
  - `split()` 將句子分割為單詞列表。
  - `get(word, 0)` 提供預設值 0，方便計數。
- **範例輸出**：
```
請輸入一句話：I love Python and Python is great
單詞計數：{'I': 1, 'love': 1, 'Python': 2, 'and': 1, 'is': 1, 'great': 1}
```

### 程式碼範例 5：去重應用（集合）
```python
# 去除重複數字
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_numbers = set(numbers)
print(f"去重後：{unique_numbers}")

# 轉回列表（若需要）
unique_list = list(unique_numbers)
print(f"轉為列表：{unique_list}")
```
- **說明**：
  - `set()` 自動去除重複元素。
  - 可將集合轉回列表進行後續操作。
- **預期輸出**：
```
去重後：{1, 2, 3, 4, 5}
轉為列表：[1, 2, 3, 4, 5]
```

## 5. 課堂練習
請撰寫一個 Python 程式，完成以下任務：
1. 提示使用者輸入 3 位學生的姓名和成績（數學、英文），儲存到字典。
2. 計算每位學生的平均成績並添加到字典。
3. 提示使用者輸入一組數字（以空格分隔），將其轉為集合並去除重複。
4. 檢查是否有學生姓名出現在輸入的數字集合中（假設數字可能是學生的 ID）。

### 參考解答
```python
# 儲存學生資料
students = {}
for i in range(3):
    name = input(f"請輸入第 {i+1} 位學生姓名：")
    math = int(input("數學成績："))
    english = int(input("英文成績："))
    students[name] = {"math": math, "english": english}
    # 計算平均成績
    students[name]["average"] = (math + english) / 2

print(f"學生資料：{students}")

# 取得數字集合
numbers = input("請輸入一組數字（以空格分隔）：")
number_set = set(numbers.split())
print(f"數字集合：{number_set}")

# 檢查姓名是否在數字集合中
for name in students.keys():
    if name in number_set:
        print(f"學生 {name} 的姓名出現在數字集合中！")
    else:
        print(f"學生 {name} 的姓名不在數字集合中。")
```
- **說明**：
  - 巢狀字典儲存學生資料，包含平均成績。
  - `split()` 將輸入字串轉為列表，`set()` 去除重複。
  - 使用 `keys()` 檢查學生姓名是否出現在集合中。
- **範例輸出**：
```
請輸入第 1 位學生姓名：Alice
數學成績：85
英文成績：90
請輸入第 2 位學生姓名：Bob
數學成績：78
英文成績：82
請輸入第 3 位學生姓名：Cathy
數學成績：95
英文成績：88
學生資料：{'Alice': {'math': 85, 'english': 90, 'average': 87.5}, 'Bob': {'math': 78, 'english': 82, 'average': 80.0}, 'Cathy': {'math': 95, 'english': 88, 'average': 91.5}}
請輸入一組數字（以空格分隔）：Alice 123 456
數字集合：{'Alice', '123', '456'}
學生 Alice 的姓名出現在數字集合中！
學生 Bob 的姓名不在數字集合中。
學生 Cathy 的姓名不在數字集合中。
```

## 6. 常見問題與疑難排解
- **問題**：`KeyError` 當訪問不存在的鍵。
  - **解決**：使用 `get()` 方法或檢查鍵是否存在（`key in dict`）。
- **問題**：`TypeError: unhashable type: 'list'`。
  - **解決**：字典鍵或集合元素不可為列表，改用元組或字串。
- **問題**：集合運算結果不符合預期。
  - **解決**：檢查集合內容，確保元素型態一致（例如數字與字串不同）。

## 7. 回家作業
1. 撰寫一個程式，提示使用者輸入一句話，統計每個字母（忽略大小寫）的出現次數，儲存到字典並輸出。
2. 改進課堂練習程式，檢查兩個學生是否有相同的成績（使用集合比較）。
3. 閱讀 Python 官方文件 [docs.python.org](https://docs.python.org/3/) 中的「Mapping Types — dict」和「Set Types — set, frozenset」章節，了解更多細節。

## 8. 延伸學習
- 探索字典推導式（dictionary comprehension），簡化字典創建。
- 學習 `frozenset()`，一種不可變的集合型態。
- 嘗試使用字典和集合實現進階應用，如圖形資料結構（後續週次介紹）。