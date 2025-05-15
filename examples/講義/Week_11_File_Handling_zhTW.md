# 第 11 週：檔案處理

## 課程目標
- 理解 Python 中檔案讀寫的基本概念與操作。
- 掌握使用 `with open()` 語句進行安全檔案操作。
- 學習處理文本檔案（`.txt`）和 CSV 檔案（`.csv`）。
- 透過實例練習，應用檔案處理技術解決實際問題。

## 1. 檔案處理概述
檔案處理是指程式讀取或寫入檔案的過程，常用於儲存資料、記錄日誌或處理大量數據。Python 提供內建函式 `open()` 來操作檔案，並透過 `with` 語句確保檔案正確關閉。

### 檔案操作模式
- `"r"`：讀取模式（預設），檔案不存在會報錯。
- `"w"`：寫入模式，會覆蓋原有檔案，若檔案不存在則創建。
- `"a"`：追加模式，寫入內容追加到檔案末尾。
- `"r+"`：讀寫模式，允許同時讀取和寫入。

### 為什麼使用 `with open()`？
- 自動關閉檔案，防止資源洩漏。
- 簡化程式碼，無需手動呼叫 `file.close()`。
- 處理異常時確保檔案正確關閉。

## 2. 讀取文本檔案
使用 `open()` 和 `with` 語句讀取文本檔案（`.txt`），常見方法包括：
- `read()`：讀取整個檔案內容為字串。
- `readline()`：讀取一行內容。
- `readlines()`：讀取所有行並返回列表。
- 直接迭代檔案物件：逐行讀取，節省記憶體。

### 程式碼範例 1：讀取文本檔案
假設有一個名為 `sample.txt` 的檔案，內容如下：
```
Hello, Python!
This is a test file.
Enjoy coding!
```

程式碼：
```python
# 使用 with open() 讀取檔案
with open("sample.txt", "r", encoding="utf-8")  as file:
    # 讀取整個檔案
    content = file.read()
    print("完整內容：")
    print(content)

# 逐行讀取
with open("sample.txt", "r", encoding="utf-8") as file:
    print("逐行讀取：")
    for line in file:
        print(line.strip())  # 移除換行符
```
- **說明**：
  - `encoding="utf-8"` 確保正確處理中文或其他非 ASCII 字元。
  - `strip()` 移除每行的換行符（`\n`）。
  - `for line in file` 逐行迭代，適合大型檔案。
- **預期輸出**：
```
完整內容：
Hello, Python!
This is a test file.
Enjoy coding!

逐行讀取：
Hello, Python!
This is a test file.
Enjoy coding!
```

## 3. 寫入文本檔案
使用 `"w"` 或 `"a"` 模式寫入檔案，`"w"` 會覆蓋原有內容，`"a"` 則追加內容。

### 程式碼範例 2：寫入文本檔案
```python
# 寫入新檔案
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("這是第一行。\n")
    file.write("這是第二行。\n")

# 追加內容
with open("output.txt", "a", encoding="utf-8") as file:
    file.write("追加的新內容。\n")

# 驗證寫入結果
with open("output.txt", "r", encoding="utf-8") as file:
    print("檔案內容：")
    print(file.read())
```
- **說明**：
  - `"w"` 模式創建或覆蓋 `output.txt`。
  - `"a"` 模式在檔案末尾追加內容。
  - 每次寫入需手動添加換行符 `\n`。
- **預期輸出**：
```
檔案內容：
這是第一行。
這是第二行。
追加的新內容。
```

## 4. 處理 CSV 檔案
CSV（Comma-Separated Values）檔案是一種常見的資料儲存格式，Python 的 `csv` 模組簡化了 CSV 檔案的讀寫。

### 程式碼範例 3：讀寫 CSV 檔案
假設有一個名為 `students.csv` 的檔案，內容如下：
```
name,math,english
Alice,85,90
Bob,78,82
Cathy,95,88
```

程式碼：
```python
import csv

# 讀取 CSV 檔案
with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)  # 跳過標題行
    print(f"標題：{header}")
    for row in reader:
        print(f"學生：{row[0]}, 數學：{row[1]}, 英文：{row[2]}")

# 寫入 CSV 檔案
data = [
    ["name", "math", "english"],
    ["David", 92, 87],
    ["Eve", 88, 91]
]

with open("new_students.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

# 驗證寫入結果
with open("new_students.csv", "r", encoding="utf-8") as file:
    print("\n新 CSV 檔案內容：")
    print(file.read())
```
- **說明**：
  - `csv.reader` 將每行解析為列表。
  - `next(reader)` 跳過標題行。
  - `newline=""` 避免寫入時多餘的換行符（Windows 系統）。
  - `csv.writer` 將列表寫入 CSV 格式。
- **預期輸出**：
```
標題：['name', 'math', 'english']
學生：Alice, 數學：85, 英文：90
學生：Bob, 數學：78, 英文：82
學生：Cathy, 數學：95, 英文：88

新 CSV 檔案內容：
name,math,english
David,92,87
Eve,88,91
```

## 5. 文字處理練習
檔案處理常與文字處理結合，例如統計字數、過濾特定內容等。

### 程式碼範例 4：統計檔案字數
```python
# 統計檔案中的字數
def count_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return "檔案不存在！"

# 測試
filename = "sample.txt"
word_count = count_words(filename)
print(f"{filename} 中的單詞數：{word_count}")
```
- **說明**：
  - `split()` 將內容分割為單詞列表（以空白分隔）。
  - 使用異常處理（後續第12週詳細介紹）避免檔案不存在的錯誤。
- **預期輸出**（假設 `sample.txt` 如範例 1）：
```
sample.txt 中的單詞數：8
```

## 6. 課堂練習
請撰寫一個 Python 程式，完成以下任務：
1. 提示使用者輸入 3 位學生的姓名和成績（數學、英文），儲存到 `grades.csv`。
2. 讀取 `grades.csv`，計算每位學生的平均成績並輸出。
3. 將平均成績追加到原檔案的每一行（新增 `average` 欄位）。
4. 統計 `grades.csv` 中所有單詞的總數（包括標題）。

### 參考解答
```python
import csv

# 任務 1：寫入學生資料
students = []
for _ in range(3):
    name = input("請輸入學生姓名：")
    math = int(input("數學成績："))
    english = int(input("英文成績："))
    students.append([name, math, english])

with open("grades.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "math", "english"])
    writer.writerows(students)

# 任務 2：讀取並計算平均成績
with open("grades.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # 跳過標題
    print("學生平均成績：")
    updated_rows = []
    for row in reader:
        name, math, english = row
        avg = (int(math) + int(english)) / 2
        print(f"{name} 的平均成績：{avg:.2f}")
        updated_rows.append([name, math, english, avg])

# 任務 3：追加平均成績到檔案
with open("grades.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "math", "english", "average"])
    writer.writerows(updated_rows)

# 任務 4：統計單詞數
with open("grades.csv", "r", encoding="utf-8") as file:
    content = file.read()
    words = content.replace(",", " ").split()
    print(f"grades.csv 中的單詞數：{len(words)}")
```
- **說明**：
  - 任務 1 使用 `csv.writer` 寫入學生資料。
  - 任務 2 讀取 CSV，計算平均成績並儲存到新列表。
  - 任務 3 重寫 CSV，包含 `average` 欄位。
  - 任務 4 將逗號替換為空格，分割後統計單詞數。
- **範例輸出**：
```
請輸入學生姓名：Alice
數學成績：85
英文成績：90
請輸入學生姓名：Bob
數學成績：78
英文成績：82
請輸入學生姓名：Cathy
數學成績：95
英文成績：88
學生平均成績：
Alice 的平均成績：87.50
Bob 的平均成績：80.00
Cathy 的平均成績：91.50
grades.csv 中的單詞數：16
```

## 7. 常見問題與疑難排解
- **問題**：`UnicodeDecodeError` 錯誤。
  - **解決**：指定正確的編碼（如 `encoding="utf-8"`），或檢查檔案編碼格式。
- **問題**：寫入 CSV 時多餘換行。
  - **解決**：在 `open()` 中加入 `newline=""` 參數。
- **問題**：`FileNotFoundError`。
  - **解決**：確認檔案路徑正確，或檢查檔案是否存在。

## 8. 回家作業
1. 撰寫一個程式，讀取一個文本檔案，統計每個單詞的出現次數並儲存到新檔案。
2. 改進課堂練習程式，檢查使用者輸入的成績是否在 0-100 之間，若無效則提示重新輸入。
3. 閱讀 Python 官方文件 [docs.python.org](https://docs.python.org/3/) 中的「Input/Output」和「csv — CSV File Reading and Writing」章節，了解更多細節。

## 9. 延伸學習
- 探索 `pandas` 模組（第17週介紹）處理大型 CSV 檔案。
- 學習處理其他檔案格式，如 JSON 或 Excel（使用 `json` 或 `openpyxl`）。
- 嘗試實現檔案備份功能，結合檔案讀寫與複製。