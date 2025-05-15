# 第 1 週：認識 Python 與開發環境

## 課程目標
- 了解 Python 程式語言的基本概念及其應用領域。
- 成功設定 Python 開發環境，包括 Visual Studio Code (VSCode) 與 Jupyter Notebook。
- 撰寫並執行第一個 Python 程式，熟悉基本語法與執行流程。

## 1. Python 語言介紹
Python 是一種高階、解釋型程式語言，以其簡潔的語法和強大的功能受到廣泛歡迎。它適用於多種領域，包括網頁開發、資料分析、人工智慧、自動化腳本等。Python 的設計哲學強調程式碼的可讀性，使其成為初學者學習程式設計的理想選擇。

### Python 的優勢
- **簡單易學**：語法接近自然語言，減少學習曲線。
- **跨平台**：可在 Windows、macOS、Linux 等系統上運行。
- **豐富的生態系統**：擁有大量的標準庫和第三方套件，支援多種應用。
- **活躍的社群**：全球龐大的開發者社群提供豐富的資源與支援。

### Python 版本
- **Python 3**：目前的主流版本（例如，2025年的 Python 3.11 或更新版本），本課程將使用 Python 3。
- **Python 2**：已於2020年停止支援，不建議使用。

## 2. 設定 Python 開發環境
要開始撰寫 Python 程式，您需要安裝 Python 解釋器並選擇合適的程式碼編輯器。本課程推薦使用 Visual Studio Code (VSCode) 作為主要編輯器，並介紹 Jupyter Notebook 進行互動式程式設計。

### 2.1 安裝 Python
1. 訪問 [python.org](https://www.python.org/downloads/) 下載最新版本的 Python。
2. 安裝時，務必勾選「Add Python to PATH」選項，以便在終端機中使用 Python 指令。
3. 安裝完成後，開啟終端機（Windows 使用命令提示字元或 PowerShell，macOS/Linux 使用終端機），輸入以下指令驗證：
```bash
python --version
```
- 預期輸出：`Python 3.x.x`（例如 `Python 3.11.7`）。
- 若顯示錯誤，檢查是否正確加入 PATH 或重新安裝。

### 2.2 安裝 Visual Studio Code (VSCode)
1. 從 [code.visualstudio.com](https://code.visualstudio.com/) 下載並安裝 VSCode。
2. 開啟 VSCode，前往「擴充功能」(Extensions) 面板，搜尋並安裝「Python」擴充功能（由 Microsoft 提供）。
3. 建立一個新檔案，儲存為 `.py` 副檔名（例如 `first_program.py`），即可開始撰寫 Python 程式碼。

### 2.3 安裝並使用 Jupyter Notebook
Jupyter Notebook 是一個互動式編程環境，適合初學者進行程式碼測試與學習。
1. 在終端機中安裝 Jupyter：
```bash
pip install jupyter
```
2. 啟動 Jupyter Notebook：
```bash
jupyter notebook
```
3. 瀏覽器將自動開啟 Jupyter 介面，點擊「New」建立一個 Python Notebook。
4. 在 Notebook 的單元格中輸入程式碼並按「Shift + Enter」執行。

## 3. 撰寫第一個 Python 程式
我們將從一個經典的「Hello, World!」程式開始，學習 Python 的基本語法和執行方式。

### 程式碼範例 1：Hello World
```python
# 這是一個單行註解，用來記錄程式碼的說明
print("Hello, World!")
```
- **說明**：
  - `#` 開頭的內容為註解，Python 會忽略這些內容，僅用於說明程式碼。
  - `print()` 是內建函式，用於將指定的內容輸出到控制台。
  - `"Hello, World!"` 是一個字串，必須用單引號 `'` 或雙引號 `"` 括起來。
- **執行方式**：
  - **VSCode**：將程式碼儲存為 `hello.py`，右鍵點擊檔案，選擇「在終端機中執行 Python 檔案」。
  - **Jupyter Notebook**：在單元格中輸入程式碼，按「Shift + Enter」執行。
- **預期輸出**：
```
Hello, World!
```

### 程式碼範例 2：與使用者互動
以下程式會提示使用者輸入姓名，並輸出個人化的問候訊息。
```python
# 提示使用者輸入姓名
name = input("請輸入您的姓名：")
# 使用 f-string 格式化輸出問候訊息
print(f"您好，{name}！歡迎體驗 Python 程式設計！")
```
- **說明**：
  - `input()` 函式顯示提示訊息並等待使用者輸入，傳回值為字串。
  - `name` 是一個變數，用於儲存使用者輸入的內容。
  - `f"..."` 是 f-string（格式化字串），允許在字串中直接嵌入變數（例如 `{name}`）。
- **執行方式**：同上，儲存並執行程式。
- **範例輸出**：
```
請輸入您的姓名：Alice
您好，Alice！歡迎體驗 Python 程式設計！
```

## 4. Python 基本語法規則
在撰寫 Python 程式時，需遵守以下語法規則：
- **大小寫敏感**：Python 區分大小寫，例如 `print` 和 `Print` 是不同的。
- **縮排**：Python 使用縮排（通常 4 個空格）來定義程式碼區塊，例如迴圈或函式的內容。
- **無分號**：Python 不需要在程式碼行末加上分號 `;`。
- **註解**：
  - 單行註解：使用 `#`，例如 `# 這是註解`。
  - 多行註解：使用三引號 `"""` 或 `'''`，例如：
```python
"""
這是多行註解，
用於記錄較長的說明。
"""
```

## 5. 課堂練習
請撰寫一個 Python 程式，完成以下任務：
1. 提示使用者輸入姓名和年齡。
2. 輸出一個格式化的訊息，例如：「您好，[姓名]！您今年 [年齡] 歲。」

### 參考解答
```python
# 取得使用者輸入的姓名和年齡
name = input("請輸入您的姓名：")
age = input("請輸入您的年齡：")
# 輸出格式化訊息
print(f"您好，{name}！您今年 {age} 歲。")
```
- **執行方式**：
  - 儲存為 `greet.py` 或在 Jupyter Notebook 中執行。
  - 輸入範例：姓名「Bob」，年齡「25」。
- **預期輸出**：
```
請輸入您的姓名：Bob
請輸入您的年齡：25
您好，Bob！您今年 25 歲。
```

## 6. 常見問題與疑難排解
- **問題**：終端機顯示「python: command not found」。
  - **解決**：確認 Python 是否正確安裝並加入 PATH，或重新安裝 Python 並勾選「Add Python to PATH」。
- **問題**：執行程式時出現 `SyntaxError`。
  - **解決**：檢查語法是否正確，例如引號是否成對、縮排是否一致。
- **問題**：變數未定義（`NameError`）。
  - **解決**：確保變數在使用前已定義，例如 `name = input(...)`。

## 7. 回家作業
1. 在您的電腦上完成 Python、VSCode 和 Jupyter Notebook 的安裝。
2. 撰寫一個 Python 程式，提示使用者輸入兩個資訊（例如，最喜歡的動物和城市），並輸出一句創意句子，例如：「[動物] 在 [城市] 裡快樂地生活！」。
3. 瀏覽 Python 官方文件 [docs.python.org](https://docs.python.org/3/)，閱讀「Tutorial」部分的「An Informal Introduction to Python」。

## 8. 延伸學習
- 嘗試在 VSCode 中使用「Python Interactive」窗口（Jupyter-like 環境）執行程式碼。
- 探索 Python 的內建函式，例如 `len()`、`type()`，並在程式中試用。