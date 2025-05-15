# 第 13 週：資料結構整合練習

## 課程目標
- 整合前幾週學習的資料結構（列表和字典），應用於實際問題。
- 設計並實現兩個小型專案：成績管理系統和字詞統計程式。
- 練習結合輸入輸出、迴圈、函式和檔案處理的程式設計技巧。
- 透過實作，提升程式結構化與模組化設計的能力。

## 1. 資料結構整合練習概述
本週課程將前幾週學習的知識（列表、字典、函式、檔案處理、例外處理等）整合，透過兩個小型專案展示資料結構的實際應用：
- **成績管理系統**：管理學生資料，計算平均成績，儲存到檔案。
- **字詞統計程式**：分析文本檔案，統計單詞出現次數並排序輸出。

這些專案強調模組化設計（使用函式）和錯誤處理，模擬真實世界的程式設計場景。

## 2. 專案 1：成績管理系統
成績管理系統允許使用者輸入學生資料（姓名、數學成績、英文成績），計算平均成績，儲存到 CSV 檔案，並提供查詢功能。

### 功能要求
1. 輸入學生資料並驗證輸入（成績需為 0-100 的數字）。
2. 計算每位學生的平均成績。
3. 將資料儲存到 `grades.csv` 檔案。
4. 提供查詢功能，根據姓名顯示學生資料。

### 程式碼範例 1：成績管理系統
```python
import csv

def input_student():
    """輸入並驗證學生資料"""
    while True:
        try:
            name = input("請輸入學生姓名（輸入 'q' 退出）：")
            if name.lower() == 'q':
                return None
            math = int(input("數學成績（0-100）："))
            if not 0 <= math <= 100:
                raise ValueError("數學成績必須在 0 到 100 之間！")
            english = int(input("英文成績（0-100）："))
            if not 0 <= english <= 100:
                raise ValueError("英文成績必須在 0 到 100 之間！")
            return {"name": name, "math": math, "english": english, "average": (math + english) / 2}
        except ValueError as e:
            print(f"錯誤：{e} 請重新輸入。")

def save_grades(students, filename="grades.csv"):
    """將學生資料儲存到 CSV 檔案"""
    try:
        with open(filename, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "math", "english", "average"])
            for student in students:
                writer.writerow([student["name"], student["math"], student["english"], student["average"]])
        print(f"資料已儲存到 {filename}")
    except Exception as e:
        print(f"儲存檔案時發生錯誤：{e}")

def query_student(students, name):
    """查詢學生資料"""
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None

def main():
    students = []
    print("成績管理系統")
    
    # 輸入學生資料
    while True:
        student = input_student()
        if student is None:
            break
        students.append(student)
    
    # 儲存資料
    if students:
        save_grades(students)
    
    # 查詢學生
    while True:
        name = input("請輸入要查詢的學生姓名（輸入 'q' 退出）：")
        if name.lower() == 'q':
            break
        result = query_student(students, name)
        if result:
            print(f"姓名：{result['name']}, 數學：{result['math']}, 英文：{result['english']}, 平均：{result['average']:.2f}")
        else:
            print(f"未找到學生：{name}")

if __name__ == "__main__":
    main()
```
- **說明**：
  - `input_student()`：驗證輸入並返回學生字典，包含姓名和成績。
  - `save_grades()`：將學生資料寫入 CSV 檔案，包含標題行。
  - `query_student()`：根據姓名查找學生並返回資料。
  - `main()`：主程式控制流程，整合輸入、儲存和查詢功能。
  - 使用例外處理確保輸入有效，檔案操作安全。
- **範例輸出**：
```
成績管理系統
請輸入學生姓名（輸入 'q' 退出）：Alice
數學成績（0-100）：85
英文成績（0-100）：90
請輸入學生姓名（輸入 'q' 退出）：Bob
數學成績（0-100）：78
英文成績（0-100）：82
請輸入學生姓名（輸入 'q' 退出）：q
資料已儲存到 grades.csv
請輸入要查詢的學生姓名（輸入 'q' 退出）：Alice
姓名：Alice, 數學：85, 英文：90, 平均：87.50
請輸入要查詢的學生姓名（輸入 'q' 退出）：Cathy
未找到學生：Cathy
請輸入要查詢的學生姓名（輸入 'q' 退出）：q
```
- **生成的 grades.csv 內容**：
```
name,math,english,average
Alice,85,90,87.5
Bob,78,82,80.0
```

## 3. 專案 2：字詞統計程式
字詞統計程式讀取文本檔案，統計每個單詞的出現次數，排序後輸出結果，並將統計結果儲存到新檔案。

### 功能要求
1. 讀取指定文本檔案，忽略標點符號並統一轉為小寫。
2. 統計每個單詞的出現次數，儲存到字典。
3. 按出現次數降序排序，若次數相同則按字母順序排序。
4. 將結果儲存到新檔案。

### 程式碼範例 2：字詞統計程式
假設有一個名為 `sample.txt` 的檔案，內容如下：
```
Hello Python! Hello world.
Python is fun and Python is great.
```

程式碼：
```python
import string

def clean_text(text):
    """清理文本：移除標點符號並轉為小寫"""
    # 移除標點符號
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator)
    # 轉為小寫並分割
    return text.lower().split()

def count_words(filename):
    """統計單詞出現次數"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            words = clean_text(text)
            word_count = {}
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
            return word_count
    except FileNotFoundError:
        print(f"錯誤：檔案 {filename} 不存在！")
        return {}
    except Exception as e:
        print(f"讀取檔案時發生錯誤：{e}")
        return {}

def save_word_count(word_count, output_filename="word_count.txt"):
    """將統計結果儲存到檔案"""
    try:
        # 按次數降序和字母升序排序
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        with open(output_filename, "w", encoding="utf-8") as file:
            file.write("單詞統計結果：\n")
            for word, count in sorted_words:
                file.write(f"{word}: {count}\n")
        print(f"統計結果已儲存到 {output_filename}")
    except Exception as e:
        print(f"儲存檔案時發生錯誤：{e}")

def main():
    filename = input("請輸入要分析的文本檔案名稱：")
    word_count = count_words(filename)
    
    if word_count:
        print("單詞統計結果：")
        # 排序並顯示
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
        
        # 儲存結果
        save_word_count(word_count)

if __name__ == "__main__":
    main()
```
- **說明**：
  - `clean_text()`：移除標點符號並將文本轉為小寫單詞列表。
  - `count_words()`：讀取檔案，統計單詞次數，使用字典儲存。
  - `save_word_count()`：將排序後的統計結果寫入檔案。
  - `main()`：主程式負責輸入檔案名稱、顯示結果和儲存。
  - 使用 `lambda` 函式實現多條件排序（次數降序，字母升序）。
- **範例輸出**（假設使用上述 `sample.txt`）：
```
請輸入要分析的文本檔案名稱：sample.txt
單詞統計結果：
python: 3
hello: 2
and: 1
fun: 1
great: 1
is: 1
world: 1
統計結果已儲存到 word_count.txt
```
- **生成的 word_count.txt 內容**：
```
單詞統計結果：
python: 3
hello: 2
and: 1
fun: 1
great: 1
is: 1
world: 1
```

## 4. 專案設計原則
- **模組化**：將功能分解為獨立函式，提升程式碼可讀性和重用性。
- **錯誤處理**：使用 `try/except` 捕捉檔案操作和輸入錯誤，確保程式穩定。
- **資料結構選擇**：
  - 成績管理使用列表（儲存多個學生）和字典（儲存單一學生資料）。
  - 字詞統計使用字典（鍵為單詞，值為次數）。
- **使用者友好**：提供清晰的提示訊息和錯誤處理。

## 5. 課堂練習
請改進上述兩個專案，實現以下增強功能：
1. **成績管理系統**：
   - 檢查是否輸入重複的學生姓名，若重複則提示重新輸入。
   - 提供排序功能，按平均成績降序顯示所有學生。
2. **字詞統計程式**：
   - 忽略長度小於 3 的單詞（例如 "is", "and"）。
   - 計算檔案中的總單詞數和唯一單詞數。

### 參考解答
#### 改進成績管理系統
```python
import csv

def input_student(existing_names):
    """輸入並驗證學生資料，檢查重複姓名"""
    while True:
        try:
            name = input("請輸入學生姓名（輸入 'q' 退出）：")
            if name.lower() == 'q':
                return None
            if name.lower() in [n.lower() for n in existing_names]:
                raise ValueError("學生姓名已存在！")
            math = int(input("數學成績（0-100）："))
            if not 0 <= math <= 100:
                raise ValueError("數學成績必須在 0 到 100 之間！")
            english = int(input("英文成績（0-100）："))
            if not 0 <= english <= 100:
                raise ValueError("英文成績必須在 0 到 100 之間！")
            return {"name": name, "math": math, "english": english, "average": (math + english) / 2}
        except ValueError as e:
            print(f"錯誤：{e} 請重新輸入。")

def save_grades(students, filename="grades.csv"):
    """將學生資料儲存到 CSV 檔案"""
    try:
        with open(filename, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "math", "english", "average"])
            for student in students:
                writer.writerow([student["name"], student["math"], student["english"], student["average"]])
        print(f"資料已儲存到 {filename}")
    except Exception as e:
        print(f"儲存檔案時發生錯誤：{e}")

def query_student(students, name):
    """查詢學生資料"""
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None

def display_sorted(students):
    """按平均成績降序顯示學生"""
    sorted_students = sorted(students, key=lambda x: x["average"], reverse=True)
    print("按平均成績排序：")
    for student in sorted_students:
        print(f"姓名：{student['name']}, 數學：{student['math']}, 英文：{student['english']}, 平均：{student['average']:.2f}")

def main():
    students = []
    existing_names = []
    print("成績管理系統")
    
    # 輸入學生資料
    while True:
        student = input_student(existing_names)
        if student is None:
            break
        students.append(student)
        existing_names.append(student["name"])
    
    # 儲存資料
    if students:
        save_grades(students)
    
    # 顯示排序結果
    if students:
        display_sorted(students)
    
    # 查詢學生
    while True:
        name = input("請輸入要查詢的學生姓名（輸入 'q' 退出   退出）：")
        if name.lower() == 'q':
            break
        result = query_student(students, name)
        if result:
            print(f"姓名：{result['name']}, 數學：{result['math']}, 英文：{result['english']}, 平均：{result['average']:.2f}")
        else:
            print(f"未找到學生：{name}")

if __name__ == "__main__":
    main()
```

#### 改進字詞統計程式
```python
import string

def clean_text(text):
    """清理文本：移除標點符號並轉為小寫"""
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator)
    # 僅保留長度 >= 3 的單詞
    return [word for word in text.lower().split() if len(word) >= 3]

def count_words(filename):
    """統計單詞出現次數"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            words = clean_text(text)
            word_count = {}
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
            total_words = len(words)
            unique_words = len(word_count)
            return word_count, total_words, unique_words
    except FileNotFoundError:
        print(f"錯誤：檔案 {filename} 不存在！")
        return {}, 0, 0
    except Exception as e:
        print(f"讀取檔案時發生錯誤：{e}")
        return {}, 0, 0

def save_word_count(word_count, total_words, unique_words, output_filename="word_count.txt"):
    """將統計結果儲存到檔案"""
    try:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        with open(output_filename, "w", encoding="utf-8") as file:
            file.write(f"總單詞數：{total_words}\n")
            file.write(f"唯一單詞數：{unique_words}\n")
            file.write("單詞統計結果：\n")
            for word, count in sorted_words:
                file.write(f"{word}: {count}\n")
        print(f"統計結果已儲存到 {output_filename}")
    except Exception as e:
        print(f"儲存檔案時發生錯誤：{e}")

def main():
    filename = input("請輸入要分析的文本檔案名稱：")
    word_count, total_words, unique_words = count_words(filename)
    
    if word_count:
        print(f"總單詞數：{total_words}")
        print(f"唯一單詞數：{unique_words}")
        print("單詞統計結果：")
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
        
        save_word_count(word_count, total_words, unique_words)

if __name__ == "__main__":
    main()
```
- **說明**：
  - 成績管理系統：
    - `input_student()` 檢查重複姓名，防止資料重複。
    - 新增 `display_sorted()` 按平均成績降序顯示。
  - 字詞統計程式：
    - `clean_text()` 過濾長度小於 3 的單詞。
    - `count_words()` 返回總單詞數和唯一單詞數。
    - 輸出和檔案中包含總計資訊。
- **範例輸出**（假設使用上述 `sample.txt`）：
```
請輸入要分析的文本檔案名稱：sample.txt
總單詞數：13
唯一單詞數：5
單詞統計結果：
python: 3
hello: 2
fun: 1
great: 1
world: 1
統計結果已儲存到 word_count.txt
```

## 6. 常見問題與疑難排解
- **問題**：檔案寫入失敗或格式錯誤。
  - **解決**：檢查檔案路徑和編碼，確保使用 `newline=""` 寫入 CSV。
- **問題**：輸入驗證不夠嚴格。
  - **解決**：檢查所有可能的無效輸入（如空字串、特殊字元）。
- **問題**：排序結果不符合預期。
  - **解決**：確認 `key` 函式的邏輯，確保多條件排序正確。

## 7. 回家作業
1. 為成績管理系統新增功能，允許從現有 CSV 檔案載入學生資料，繼續添加新學生。
2. 為字詞統計程式新增功能，允許使用者指定忽略的單詞列表（例如 ["the", "is"]）。
3. 閱讀 Python 官方文件 [docs.python.org](https://docs.python.org/3/) 中的「Data Structures」章節，複習列表和字典的進階用法。

## 8. 延伸學習
- 探索進階資料結構，如 `collections` 模組中的 `Counter`（適用於字詞統計）。
- 學習使用 `pandas`（第17週介紹）簡化 CSV 處理和資料分析。
- 嘗試將專案改進為命令列工具，接受參數（如檔案名稱）。