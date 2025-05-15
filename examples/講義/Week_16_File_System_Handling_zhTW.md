# 第 16 週：檔案系統處理

## 課程目標
- 理解 Python 中檔案系統操作的基本概念。
- 學習使用 `os` 模組進行資料夾和檔案管理。
- 掌握 `pathlib` 模組的現代化路徑處理方法。
- 透過實例練習，實現批次檔案處理，提升自動化能力。

## 1. 檔案系統處理概述
檔案系統處理涉及操作作業系統中的檔案和資料夾，例如創建、刪除、遍歷資料夾或批次處理檔案。Python 提供兩個主要模組：
- **`os` 模組**：提供底層檔案系統操作，跨平台相容。
- **`pathlib` 模組**：現代化的路徑處理工具，物件導向設計，程式碼更直觀。

### 為什麼需要檔案系統處理？
- **自動化任務**：批次重命名檔案、整理資料夾。
- **資料管理**：掃描目錄、篩選特定檔案類型。
- **跨平台相容**：確保程式在不同作業系統（Windows、Linux、macOS）上正常運行。

## 2. 使用 `os` 模組
`os` 模組提供與作業系統交互的功能，包括檔案和資料夾操作、路徑處理等。

### 常用 `os` 函式
- `os.listdir(path)`：列出目錄中的檔案和子資料夾。
- `os.mkdir(path)`：創建單層資料夾。
- `os.makedirs(path)`：創建多層資料夾（若中間資料夾不存在則自動創建）。
- `os.remove(path)`：刪除檔案。
- `os.rmdir(path)`：刪除空資料夾。
- `os.path.join(path, *paths)`：拼接路徑，自動處理分隔符。
- `os.path.exists(path)`：檢查檔案或資料夾是否存在。
- `os.path.isfile(path)` / `os.path.isdir(path)`：檢查是否為檔案或資料夾。

### 程式碼範例 1：使用 `os` 管理資料夾與檔案
```python
import os

# 當前工作目錄
print(f"當前工作目錄：{os.getcwd()}")

# 創建資料夾
folder = "test_folder"
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"已創建資料夾：{folder}")

# 創建檔案
file_path = os.path.join(folder, "example.txt")
with open(file_path, "w", encoding="utf-8") as file:
    file.write("這是一個測試檔案。\n")

# 列出資料夾內容
print(f"{folder} 中的內容：{os.listdir(folder)}")

# 檢查檔案是否存在
print(f"檔案 {file_path} 是否存在：{os.path.exists(file_path)}")

# 刪除檔案和資料夾
os.remove(file_path)
print(f"已刪除檔案：{file_path}")
os.rmdir(folder)
print(f"已刪除資料夾：{folder}")
```
- **說明**：
  - `os.getcwd()` 取得當前工作目錄。
  - `os.path.join()` 安全拼接路徑，適應不同作業系統的分隔符（`/` 或 `\`）。
  - 使用 `os.path.exists()` 避免重複創建資料夾。
  - `os.remove()` 和 `os.rmdir()` 分別刪除檔案和空資料夾。
- **預期輸出**：
```
當前工作目錄：/path/to/current/directory
已創建資料夾：test_folder
test_folder 中的內容：['example.txt']
檔案 test_folder/example.txt 是否存在：True
已刪除檔案：test_folder/example.txt
已刪除資料夾：test_folder
```

## 3. 使用 `pathlib` 模組
`pathlib` 提供物件導向的路徑操作，比 `os` 更直觀且現代化，特別適合處理複雜路徑。

### 常用 `pathlib` 方法
- `Path.cwd()`：取得當前工作目錄。
- `Path.mkdir(parents=True, exist_ok=True)`：創建資料夾，支援多層。
- `Path.glob(pattern)`：搜尋符合模式的檔案。
- `Path.read_text()` / `Path.write_text()`：讀寫文本檔案。
- `Path.unlink()`：刪除檔案。
- `Path.is_file()` / `Path.is_dir()`：檢查是否為檔案或資料夾。

### 程式碼範例 2：使用 `pathlib` 操作檔案系統
```python
from pathlib import Path

# 當前工作目錄
current_dir = Path.cwd()
print(f"當前工作目錄：{current_dir}")

# 創建資料夾
folder = current_dir / "data_folder"
folder.mkdir(exist_ok=True)
print(f"已創建資料夾：{folder}")

# 創建並寫入檔案
file_path = folder / "sample.txt"
file_path.write_text("這是一個 pathlib 測試檔案。\n", encoding="utf-8")
print(f"已創建檔案：{file_path}")

# 讀取檔案內容
content = file_path.read_text(encoding="utf-8")
print(f"檔案內容：\n{content}")

# 列出資料夾中的所有 .txt 檔案
print("資料夾中的 .txt 檔案：")
for txt_file in folder.glob("*.txt"):
    print(txt_file.name)

# 刪除檔案和資料夾
file_path.unlink()
print(f"已刪除檔案：{file_path}")
folder.rmdir()
print(f"已刪除資料夾：{folder}")
```
- **說明**：
  - `Path.cwd()` 返回當前目錄的 `Path` 物件。
  - 使用 `/` 運算子拼接路徑，簡潔且跨平台。
  - `glob("*.txt")` 搜尋指定模式的檔案。
  - `read_text` 和 `write_text` 簡化檔案讀寫。
- **預期輸出**：
```
當前工作目錄：/path/to/current/directory
已創建資料夾：/path/to/current/directory/data_folder
已創建檔案：/path/to/current/directory/data_folder/sample.txt
檔案內容：
這是一個 pathlib 測試檔案。

資料夾中的 .txt 檔案：
sample.txt
已刪除檔案：/path/to/current/directory/data_folder/sample.txt
已刪除資料夾：/path/to/current/directory/data_folder
```

## 4. 批次處理檔案
批次處理檔案是檔案系統處理的常見應用，例如重命名檔案、篩選特定類型檔案或移動檔案。

### 程式碼範例 3：批次重命名檔案
```python
from pathlib import Path

def batch_rename(folder_path, prefix="file_"):
    """批次為資料夾中的檔案加上前綴"""
    folder = Path(folder_path)
    if not folder.exists():
        print(f"資料夾 {folder} 不存在！")
        return
    
    try:
        for file_path in folder.iterdir():
            if file_path.is_file():
                new_name = prefix + file_path.name
                new_path = file_path.with_name(new_name)
                file_path.rename(new_path)
                print(f"已將 {file_path.name} 重命名為 {new_name}")
    except Exception as e:
        print(f"重命名時發生錯誤：{e}")

# 測試批次重命名
folder = Path("test_files")
folder.mkdir(exist_ok=True)

# 創建測試檔案
for i in range(3):
    (folder / f"doc{i}.txt").write_text(f"測試檔案 {i}\n", encoding="utf-8")

print("原始檔案：", [f.name for f in folder.iterdir()])
batch_rename(folder, prefix="renamed_")
print("重命名後檔案：", [f.name for f in folder.iterdir()])
```
- **說明**：
  - `batch_rename` 為資料夾中的每個檔案加上指定前綴。
  - `iterdir()` 遍歷資料夾內容，`with_name()` 生成新檔案名稱。
  - 使用例外處理確保操作安全。
  - 程式先創建測試檔案，然後執行重命名。
- **預期輸出**：
```
原始檔案：['doc0.txt', 'doc1.txt', 'doc2.txt']
已將 doc0.txt 重命名為 renamed_doc0.txt
已將 doc1.txt 重命名為 renamed_doc1.txt
已將 doc2.txt 重命名為 renamed_doc2.txt
重命名後檔案：['renamed_doc0.txt', 'renamed_doc1.txt', 'renamed_doc2.txt']
```

## 5. 課堂練習
請撰寫一個 Python 程式，實現以下功能：
1. 創建一個名為 `backup` 的資料夾。
2. 掃描指定資料夾，找出所有 `.txt` 檔案。
3. 將這些 `.txt` 檔案複製到 `backup` 資料夾，檔案名稱加上 `_backup` 後綴。
4. 統計複製的檔案數量並顯示。

### 參考解答
```python
from pathlib import Path
import shutil

def backup_txt_files(source_folder, backup_folder="backup"):
    """將指定資料夾中的 .txt 檔案備份到 backup 資料夾"""
    source = Path(source_folder)
    backup = Path(backup_folder)
    
    # 創建備份資料夾
    backup.mkdir(exist_ok=True)
    
    # 統計計數器
    count = 0
    
    try:
        # 掃描 .txt 檔案
        for file_path in source.glob("*.txt"):
            if file_path.is_file():
                # 生成備份檔案名稱
                backup_name = file_path.stem + "_backup" + file_path.suffix
                backup_path = backup / backup_name
                # 複製檔案
                shutil.copy2(file_path, backup_path)
                print(f"已備份 {file_path.name} 到 {backup_path}")
                count += 1
        
        print(f"共備份 {count} 個 .txt 檔案")
    except Exception as e:
        print(f"備份時發生錯誤：{e}")
    
    return count

# 測試程式
source_folder = "test_files"
# 創建測試資料夾和檔案
source = Path(source_folder)
source.mkdir(exist_ok=True)
for i in range(3):
    (source / f"note{i}.txt").write_text(f"筆記 {i}\n", encoding="utf-8")
(source / "image.png").write_text("假圖片檔案\n", encoding="utf-8")

# 執行備份
backup_txt_files(source_folder)
```
- **說明**：
  - `backup_txt_files` 掃描指定資料夾中的 `.txt` 檔案。
  - 使用 `shutil.copy2` 複製檔案，保留元資料（如創建時間）。
  - `stem` 和 `suffix` 分離檔案名稱和副檔名，生成新名稱。
  - 統計並顯示備份的檔案數量。
- **範例輸出**：
```
已備份 note0.txt 到 backup/note0_backup.txt
已備份 note1.txt 到 backup/note1_backup.txt
已備份 note2.txt 到 backup/note2_backup.txt
共備份 3 個 .txt 檔案
```

## 6. 常見問題與疑難排解
- **問題**：`PermissionError` 無法訪問檔案或資料夾。
  - **解決**：檢查程式是否有足夠權限，或確認檔案未被其他程式鎖定。
- **問題**：路徑在不同作業系統上不一致。
  - **解決**：使用 `os.path.join` 或 `pathlib` 處理跨平台路徑。
- **問題**：`FileExistsError` 嘗試創建已存在的資料夾。
  - **解決**：使用 `exist_ok=True` 或檢查 `exists()`。

## 7. 回家作業
1. 撰寫一個程式，遍歷指定資料夾及其子資料夾，列出所有檔案的完整路徑和大小（以 KB 為單位）。
2. 改進課堂練習程式，新增功能檢查備份檔案是否已存在，若存在則跳過複製。
3. 閱讀 Python 官方文件 [docs.python.org](https://docs.python.org/3/) 中的「os — Miscellaneous operating system interfaces」和「pathlib — Object-oriented filesystem paths」章節，了解更多細節。

## 8. 延伸學習
- 探索 `shutil` 模組的高階功能，如移動檔案或壓縮資料夾。
- 學習使用 `glob` 模組進行更複雜的檔案模式匹配。
- 嘗試實現一個簡單的檔案整理工具，根據檔案類型自動分類到不同資料夾。