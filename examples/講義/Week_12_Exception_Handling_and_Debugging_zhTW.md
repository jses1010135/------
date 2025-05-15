# 第 12 週：例外處理與除錯

## 課程目標
- 理解 Python 中的例外（Exception）概念與處理方式。
- 掌握使用 `try/except` 語句捕捉和處理錯誤。
- 認識常見錯誤類型及其原因。
- 學習除錯技巧，提升程式穩定性和可維護性。
- 透過實例練習，應用例外處理與除錯解決實際問題。

## 1. 例外處理概述
例外是程式執行過程中發生的錯誤事件，例如檔案不存在、除以零或輸入無效資料。如果不處理例外，程式會終止並顯示錯誤訊息。Python 使用 `try/except` 結構捕捉和處理例外，確保程式穩定運行。

### 例外處理語法
```python
try:
    # 可能引發例外的程式碼
except 例外類型 as 變數:
    # 處理例外的程式碼
else:
    # 無例外時執行的程式碼（可選）
finally:
    # 無論是否發生例外都會執行的程式碼（可選）
```

### 為什麼需要例外處理？
- **防止程式崩潰**：捕捉錯誤並提供替代方案。
- **提升用戶體驗**：顯示友好的錯誤訊息，而非技術性錯誤。
- **資源管理**：確保檔案、網路連線等資源正確關閉。

## 2. 常見錯誤類型
以下是 Python 中常見的內建例外類型：
- `ZeroDivisionError`：除以零。
- `FileNotFoundError`：檔案不存在。
- `ValueError`：函式接收無效參數（例如將字串轉為整數失敗）。
- `TypeError`：操作或函式應用於不適當的型態。
- `IndexError`：列表索引超出範圍。
- `KeyError`：字典鍵不存在。

### 程式碼範例 1：捕捉常見例外
```python
try:
    num = int(input("請輸入一個數字："))
    result = 10 / num
    print(f"10 除以 {num} 的結果：{result}")
except ZeroDivisionError:
    print("錯誤：不能除以零！")
except ValueError:
    print("錯誤：請輸入有效的數字！")
```
- **說明**：
  - `int(input())` 可能引發 `ValueError`（無效輸入）。
  - `10 / num` 可能引發 `ZeroDivisionError`（除以零）。
  - `except` 塊處理特定錯誤並顯示友好的訊息。
- **範例輸出**：
```
請輸入一個數字：0
錯誤：不能除以零！
請輸入一個數字：abc
錯誤：請輸入有效的數字！
請輸入一個數字：5
10 除以 5 的結果：2.0
```

## 3. 使用 else 和 finally
- `else`：僅在 `try` 塊無例外時執行。
- `finally`：無論是否發生例外都執行，常用於清理資源（如關閉檔案）。

### 程式碼範例 2：完整例外處理結構
```python
try:
    file = open("sample.txt", "r", encoding="utf-8")
    content = file.read()
except FileNotFoundError:
    print("錯誤：檔案不存在！")
else:
    print("檔案內容：")
    print(content)
finally:
    try:
        file.close()
        print("檔案已關閉。")
    except NameError:
        print("檔案未成功開啟，無需關閉。")
```
- **說明**：
  - `try` 嘗試開啟並讀取檔案。
  - `except FileNotFoundError` 處理檔案不存在的情況。
  - `else` 在成功讀取時顯示內容。
  - `finally` 確保檔案關閉，若檔案未開啟則捕捉 `NameError`。
- **範例輸出**（假設 `sample.txt` 不存在）：
```
錯誤：檔案不存在！
檔案未成功開啟，無需關閉。
```

## 4. 自訂例外
可以透過繼承 `Exception` 類別創建自訂例外，用於特定場景。

### 程式碼範例 3：自訂例外
```python
# 定義自訂例外
class InvalidScoreError(Exception):
    pass

# 使用自訂例外
def record_score(score):
    if not 0 <= score <= 100:
        raise InvalidScoreError("成績必須在 0 到 100 之間！")
    return f"成績：{score}"

try:
    score = int(input("請輸入學生成績："))
    result = record_score(score)
    print(result)
except InvalidScoreError as e:
    print(f"錯誤：{e}")
except ValueError:
    print("錯誤：請輸入有效的數字！")
```
- **說明**：
  - `InvalidScoreError` 是自訂例外類別。
  - `raise` 關鍵字引發例外，帶有錯誤訊息。
  - `except InvalidScoreError` 捕捉自訂例外。
- **範例輸出**：
```
請輸入學生成績：150
錯誤：成績必須在 0 到 100 之間！
請輸入學生成績：abc
錯誤：請輸入有效的數字！
請輸入學生成績：85
成績：85
```

## 5. 除錯技巧
除錯（Debugging）是找出並修復程式錯誤的過程。以下是常見除錯技巧：
- **打印日誌**：使用 `print()` 輸出變數值，檢查程式流程。
- **斷點調試**：在 IDE（如 VSCode）中設置斷點，逐行執行並檢查變數。
- **異常堆疊追蹤**：閱讀錯誤訊息的堆疊追蹤（Traceback），定位問題行。
- **單元測試**：撰寫小段程式碼測試函式或模組功能。
- **簡化問題**：將問題程式碼簡化，逐一測試以找出錯誤根源。

### 程式碼範例 4：使用打印日誌除錯
```python
def calculate_average(numbers):
    print(f"輸入數字：{numbers}")  # 除錯用
    total = sum(numbers)
    print(f"總和：{total}")  # 除錯用
    count = len(numbers)
    print(f"數量：{count}")  # 除錯用
    return total / count

try:
    nums = [1, 2, "3", 4]  # 故意包含字串
    avg = calculate_average(nums)
    print(f"平均值：{avg}")
except TypeError as e:
    print(f"錯誤：{e}")
```
- **說明**：
  - `print()` 輸出中間結果，幫助檢查 `numbers`、`total` 和 `count`。
  - 程式因 `sum([1, 2, "3", 4])` 引發 `TypeError`（字串無法相加）。
  - 透過日誌可發現問題出在輸入資料型態。
- **範例輸出**：
```
輸入數字：[1, 2, '3', 4]
錯誤：unsupported operand type(s) for +: 'int' and 'str'
```

## 6. 課堂練習
請撰寫一個 Python 程式，完成以下任務：
1. 提示使用者輸入檔案名稱，嘗試讀取檔案內容並顯示。
2. 處理以下例外：
   - `FileNotFoundError`：檔案不存在。
   - `UnicodeDecodeError`：檔案編碼錯誤。
3. 提示使用者輸入一組數字（以空格分隔），計算平均值，處理：
   - `ValueError`：無效數字輸入。
   - `ZeroDivisionError`：無輸入數字。
4. 使用打印日誌除錯，記錄輸入和計算過程。

### 參考解答
```python
def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print(f"檔案內容：\n{content}")
    except FileNotFoundError:
        print(f"錯誤：檔案 {filename} 不存在！")
    except UnicodeDecodeError:
        print("錯誤：檔案編碼不支援，請使用 UTF-8 編碼的文本檔案！")

def calculate_average(numbers_str):
    print(f"原始輸入：{numbers_str}")  # 除錯用
    try:
        numbers = [float(x) for x in numbers_str.split()]
        print(f"轉換後數字：{numbers}")  # 除錯用
        if not numbers:
            raise ZeroDivisionError("無有效數字輸入！")
        total = sum(numbers)
        count = len(numbers)
        print(f"總和：{total}, 數量：{count}")  # 除錯用
        return total / count
    except ValueError:
        print("錯誤：請輸入有效的數字！")
        return None
    except ZeroDivisionError as e:
        print(f"錯誤：{e}")
        return None

# 主程式
filename = input("請輸入檔案名稱：")
read_file(filename)

numbers_str = input("請輸入一組數字（以空格分隔）：")
avg = calculate_average(numbers_str)
if avg is not None:
    print(f"平均值：{avg:.2f}")
```
- **說明**：
  - `read_file` 函式處理檔案讀取，捕捉檔案相關例外。
  - `calculate_average` 使用列表推導式轉換輸入，記錄中間結果以便除錯。
  - 程式處理無效輸入、空輸入和檔案錯誤，顯示友好的錯誤訊息。
- **範例輸出**：
```
請輸入檔案名稱：sample.txt
錯誤：檔案 sample.txt 不存在！
請輸入一組數字（以空格分隔）：1 2 3 4
原始輸入：1 2 3 4
轉換後數字：[1.0, 2.0, 3.0, 4.0]
總和：10.0, 數量：4
平均值：2.50
```

## 7. 常見問題與疑難排解
- **問題**：未捕捉所有可能的例外。
  - **解決**：使用廣泛的 `except Exception as e` 捕捉未知錯誤（僅用於除錯），並記錄 `e` 資訊。
- **問題**：`finally` 塊未正確執行。
  - **解決**：檢查 `finally` 中的程式碼是否引發新例外。
- **問題**：除錯時難以定位錯誤。
  - **解決**：增加更多 `print()` 語句，或使用 IDE 的斷點功能檢查變數值。

## 8. 回家作業
1. 撰寫一個程式，讀取 CSV 檔案並計算每列的總和，處理 `FileNotFoundError` 和 `ValueError`。
2. 改進課堂練習程式，加入自訂例外，檢查數字輸入是否為正數，若為負數則引發錯誤。
3. 閱讀 Python 官方文件 [docs.python.org](https://docs.python.org/3/) 中的「Errors and Exceptions」章節，了解更多細節。

## 9. 延伸學習
- 探索進階除錯工具，如 Python 的 `pdb` 模組或 `logging` 模組。
- 學習單元測試框架（如 `unittest`），確保程式碼穩定性。
- 嘗試結合例外處理與檔案操作，實現資料驗證與錯誤日誌記錄。