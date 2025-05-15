# 第 5 週：字串操作與格式化

## 課程目標
- 理解 Python 中字串的基本概念與操作。
- 掌握字串的索引、切片技術，靈活存取子字串。
- 學習常用的字串方法，進行文字處理。
- 熟練使用 f-string 與 `format()` 方法進行字串格式化。
- 透過實例練習，應用字串操作解決實際問題。

## 1. 字串概述
在 Python 中，字串 (`str`) 是一種用來表示文字資料的型態，使用單引號 `'` 或雙引號 `"` 定義。字串是**不可變**的，意味著一旦創建，其內容無法直接修改，但可以透過操作創建新字串。

### 字串特性
- **可迭代**：字串中的每個字元都可以逐一存取。
- **索引**：字串中的字元有編號（從 0 開始），可用索引存取。
- **不可變**：無法直接修改字串中的字元，但可創建新字串。

### 程式碼範例 1：基本字串操作
```python
# 定義字串
message = "Hello, Python!"
print(f"字串內容：{message}")
print(f"字串長度：{len(message)}")
print(f"第一個字元：{message[0]}")
print(f"最後一個字元：{message[-1]}")
```
- **說明**：
  - `len()` 傳回字串長度（字元數）。
  - 索引從 0 開始，負索引（如 `-1`）從末尾計數。
- **預期輸出**：
```
字串內容：Hello, Python!
字串長度：13
第一個字元：H
最後一個字元：!
```

## 2. 字串索引與切片
字串中的每個字元都有對應的索引，索引從 0 開始。切片允許提取字串的一部分。

### 索引
- 正索引：從左到右，0, 1, 2, ...
- 負索引：從右到左，-1, -2, -3, ...

### 切片語法
```python
字串[start:stop:step]
```
- `start`：開始索引（包含）。
- `stop`：結束索引（不包含）。
- `step`：步進值（預設為 1），可為負數表示反向。

### 程式碼範例 2：索引與切片
```python
text = "Python Programming"

# 索引
print(f"第一個字元：{text[0]}")
print(f"最後一個字元：{text[-1]}")

# 切片
print(f"前五個字元：{text[:5]}")
print(f"從索引 7 到結尾：{text[7:]}")
print(f"每隔一個字元：{text[::2]}")
print(f"反轉字串：{text[::-1]}")
```
- **說明**：
  - `[:5]` 提取索引 0 到 4 的字元。
  - `[7:]` 提取從索引 7 到結尾的字元。
  - `[::2]` 每隔一個字元取一個。
  - `[::-1]` 反轉整個字串。
- **預期輸出**：
```
第一個字元：P
最後一個字元：g
前五個字元：Pytho
從索引 7 到結尾：Programming
每隔一個字元：Pto rgamn
反轉字串：gnimmargorP nohtyP
```

## 3. 常用字串方法
Python 提供豐富的字串方法，用於處理和操作文字資料。以下是常用的方法：
- `upper()`：轉為全大寫。
- `lower()`：轉為全小寫。
- `strip()`：移除首尾空白（或指定字元）。
- `replace(old, new)`：替換指定子字串。
- `split(sep)`：以指定分隔符分割字串為列表。
- `join(iterable)`：將可迭代物件的元素連接成字串。
- `find(sub)`：尋找子字串的首次出現索引，找不到傳回 -1。
- `startswith(prefix)`：檢查是否以指定前綴開頭。
- `endswith(suffix)`：檢查是否以指定後綴結尾。

### 程式碼範例 3：字串方法應用
```python
text = "  Hello, Python!  "

# 基本字串方法
print(f"轉大寫：{text.upper()}")
print(f"轉小寫：{text.lower()}")
print(f"移除首尾空白：{text.strip()}")
print(f"替換 Python 為 World：{text.replace('Python', 'World')}")
print(f"分割字串：{text.split(',')}")

# 連接列表元素
words = ["Python", "is", "awesome"]
print(f"連接字串：{' '.join(words)}")

# 查找與檢查
print(f"查找 'Python' 的索引：{text.find('Python')}")
print(f"是否以 'Hello' 開頭：{text.startswith('Hello')}")
print(f"是否以 '!' 結尾：{text.endswith('!')}")
```
- **說明**：
  - 方法不會修改原字串，而是傳回新字串（因字串不可變）。
  - `split()` 將字串分割為列表，`join()` 將列表元素連接為字串。
- **預期輸出**：
```
轉大寫：  HELLO, PYTHON!  
轉小寫：  hello, python!  
移除首尾空白：Hello, Python!
替換 Python 為 World：  Hello, World!  
分割字串：['  Hello', ' Python!  ']
連接字串：Python is awesome
查找 'Python' 的索引：8
是否以 'Hello' 開頭：False
是否以 '!' 結尾：True
```

## 4. 字串格式化
字串格式化是用來將變數或值嵌入字串的方式。Python 提供多種格式化方法，本課程聚焦於 `f-string` 和 `format()`。

### 4.1 f-string（格式化字串）
f-string 是 Python 3.6+ 引入的簡潔格式化方式，使用 `f` 前綴並在字串中嵌入變數或表達式。

### 程式碼範例 4：使用 f-string
```python
# 使用 f-string 格式化
name = input("請輸入您的姓名：")
age = int(input("請輸入您的年齡："))

# 基本格式化
print(f"您好，{name}！您今年 {age} 歲。")

# 表達式嵌入
print(f"五年後您將是 {age + 5} 歲。")

# 控制數字格式
height = 175.5678
print(f"身高：{height:.2f} 公分")  # 保留 2 位小數
```
- **說明**：
  - `{}` 內可放入變數或表達式。
  - `:.2f` 指定浮點數格式，保留 2 位小數。
- **範例輸出**：
```
請輸入您的姓名：Alice
請輸入您的年齡：25
您好，Alice！您今年 25 歲。
五年後您將是 30 歲。
身高：175.57 公分
```

### 4.2 str.format() 方法
`format()` 是較早的格式化方法，透過 `{}` 佔位符和 `format()` 方法指定值。

### 程式碼範例 5：使用 format()
```python
# 使用 format() 格式化
name = "Bob"
age = 30
height = 180.1234

# 基本格式化
print("您好，{}！您今年 {} 歲。".format(name, age))

# 指定索引
print("姓名：{0}, 年齡：{1}, 姓名重複：{0}".format(name, age))

# 控制格式
print("身高：{:.1f} 公分".format(height))
```
- **說明**：
  - `{}` 內可指定索引（如 `{0}`），對應 `format()` 的參數順序。
  - 格式化語法類似 f-string，例如 `{:.1f}` 保留 1 位小數。
- **預期輸出**：
```
您好，Bob！您今年 30 歲。
姓名：Bob, 年齡：30, 姓名重複：Bob
身高：180.1 公分
```

## 5. 課堂練習
請撰寫一個 Python 程式，完成以下任務：
1. 提示使用者輸入一句話（例如一句自我介紹）。
2. 執行以下操作並輸出結果：
   - 將句子轉為全大寫和全小寫。
   - 計算句子中的字元數（包含空格）。
   - 提取句子的前 5 個字元（若不足 5 個，提取全部）。
   - 檢查句子是否以「我」開頭。
3. 使用 f-string 格式化輸出，使用者的姓名（另行輸入）與上述結果。

### 參考解答
```python
# 取得使用者輸入
name = input("請輸入您的姓名：")
sentence = input("請輸入一句自我介紹：")

# 字串操作
upper_sentence = sentence.upper()
lower_sentence = sentence.lower()
length = len(sentence)
first_five = sentence[:5]
starts_with_me = sentence.startswith("我")

# 格式化輸出
print(f"您好，{name}！您的自我介紹分析如下：")
print(f"全大寫：{upper_sentence}")
print(f"全小寫：{lower_sentence}")
print(f"字元數：{length}")
print(f"前五個字元：{first_five}")
print(f"是否以'我'開頭：{starts_with_me}")
```
- **說明**：
  - 使用字串方法處理輸入句子。
  - `[:5]` 提取前 5 個字元，若句子較短則取全部。
  - f-string 整合所有結果。
- **範例輸出**：
```
請輸入您的姓名：Alice
請輸入一句自我介紹：我是一個學生
您好，Alice！您的自我介紹分析如下：
全大寫：我是一個學生
全小寫：我是一個學生
字元數：7
前五個字元：我是一個學
是否以'我'開頭：True
```

## 6. 常見問題與疑難排解
- **問題**：`IndexError: string index out of range`。
  - **解決**：檢查索引是否超出字串長度，例如 `text[100]` 當 `len(text)` 只有 10。
- **問題**：切片結果不符合預期。
  - **解決**：確認 `start:stop:step` 的範圍，記住 `stop` 不包含。
- **問題**：字串方法未改變原字串。
  - **解決**：字串不可變，方法傳回新字串，需賦值給變數（例如 `new_text = text.upper()`）。

## 7. 回家作業
1. 撰寫一個程式，提示使用者輸入電子郵件地址，檢查是否包含 `@` 並以 `.com` 結尾，輸出檢查結果。
2. 改進課堂練習程式，加入 `split()` 分割句子為單詞列表，並計算單詞數。
3. 閱讀 Python 官方文件 [docs.python.org](https://docs.python.org/3/) 中的「Text Sequence Type — str」章節，了解更多字串方法。

## 8. 延伸學習
- 探索其他字串方法，如 `count()`（計算子字串出現次數）或 `isalpha()`（檢查是否全為字母）。
- 嘗試使用正規表達式（`re` 模組，後續週次介紹）進行進階文字處理。
- 練習格式化進階應用，例如對齊文字或填充字元（例如 `{name:>10}` 右對齊）。