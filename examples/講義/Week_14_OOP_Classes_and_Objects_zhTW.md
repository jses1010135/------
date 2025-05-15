# 第 14 週：OOP：類別與物件

## 課程目標
- 理解物件導向程式設計（OOP）的基本概念。
- 學習如何在 Python 中定義類別、建構子和實例化物件。
- 掌握屬性（資料）和方法（行為）的定義與使用。
- 透過實例練習，應用類別與物件解決實際問題。

## 1. 物件導向程式設計概述
物件導向程式設計（OOP）是一種程式設計範式，將程式組織為「物件」，每個物件包含資料（屬性）和行為（方法）。Python 支援 OOP，透過類別（`class`）定義物件的藍圖。

### OOP 的核心概念
- **類別（Class）**：物件的模板，定義屬性和方法。
- **物件（Object）**：類別的實例，擁有具體的屬性值。
- **屬性（Attribute）**：物件的資料，例如姓名、年齡。
- **方法（Method）**：物件的行為，例如計算、顯示資料。

### 為什麼使用 OOP？
- **模組化**：將程式碼組織為獨立的物件，易於維護。
- **重用性**：類別可重複使用於不同程式。
- **封裝**：將資料和行為綁定，隱藏內部細節（後續第15週詳細介紹）。

## 2. 定義類別與實例化物件
類別使用 `class` 關鍵字定義，物件透過類別實例化（創建）。

### 類別語法
```python
class 類別名稱:
    def __init__(self, 參數):
        # 初始化屬性
        self.屬性 = 參數
    
    def 方法(self):
        # 定義行為
        pass
```

- `__init__` 是建構子，用於初始化物件屬性。
- `self` 代表當前物件實例，必須明確寫在方法的第一個參數。

### 程式碼範例 1：簡單類別與物件
```python
# 定義學生類別
class Student:
    def __init__(self, name, age):
        self.name = name  # 實例屬性
        self.age = age
    
    def introduce(self):
        return f"我是 {self.name}，今年 {self.age} 歲"

# 實例化物件
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# 訪問屬性和方法
print(student1.name)  # 訪問屬性
print(student1.introduce())  # 呼叫方法
print(student2.introduce())
```
- **說明**：
  - `Student` 類別定義了 `name` 和 `age` 屬性，以及 `introduce` 方法。
  - `student1` 和 `student2` 是 `Student` 類別的兩個物件，各有自己的屬性值。
  - 使用點運算子（`.`）訪問屬性和方法。
- **預期輸出**：
```
Alice
我是 Alice，今年 20 歲
我是 Bob，今年 22 歲
```

## 3. 屬性與方法的類型
- **實例屬性**：每個物件獨有的屬性，定義在 `__init__` 中。
- **類別屬性**：所有物件共享的屬性，定義在類別層級。
- **實例方法**：操作物件資料的方法，帶 `self` 參數。
- **類別方法**：操作類別資料的方法，使用 `@classmethod` 裝飾器。
- **靜態方法**：不依賴物件或類別的方法，使用 `@staticmethod` 裝飾器。

### 程式碼範例 2：類別屬性與多種方法
```python
class Student:
    school = "Python 高中"  # 類別屬性
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):  # 實例方法
        return f"我是 {self.name}，來自 {self.school}"
    
    @classmethod
    def get_school(cls):  # 類別方法
        return f"學校名稱：{cls.school}"
    
    @staticmethod
    def is_adult(age):  # 靜態方法
        return age >= 18

# 使用類別與物件
print(Student.get_school())  # 呼叫類別方法
print(Student.is_adult(20))  # 呼叫靜態方法

student = Student("Alice", 20)
print(student.introduce())  # 呼叫實例方法
print(f"是否成年：{student.is_adult(student.age)}")
```
- **說明**：
  - `school` 是類別屬性，所有 `Student` 物件共享。
  - `introduce` 是實例方法，訪問物件的 `name` 和類別的 `school`。
  - `get_school` 是類別方法，透過 `cls` 訪問類別屬性。
  - `is_adult` 是靜態方法，不依賴物件或類別。
- **預期輸出**：
```
學校名稱：Python 高中
True
我是 Alice，來自 Python 高中
是否成年：True
```

## 4. 應用實例：成績管理類別
設計一個 `GradeBook` 類別，管理學生成績，包含添加學生、計算平均成績等功能。

### 程式碼範例 3：成績管理類別
```python
class GradeBook:
    def __init__(self):
        self.students = []  # 儲存學生資料的列表
    
    def add_student(self, name, math, english):
        """添加學生及其成績"""
        if not (0 <= math <= 100 and 0 <= english <= 100):
            raise ValueError("成績必須在 0 到 100 之間！")
        student = {"name": name, "math": math, "english": english, "average": (math + english) / 2}
        self.students.append(student)
    
    def get_student(self, name):
        """查詢學生資料"""
        for student in self.students:
            if student["name"].lower() == name.lower():
                return student
        return None
    
    def get_class_average(self):
        """計算全班平均成績"""
        if not self.students:
            return 0
        total = sum(student["average"] for student in self.students)
        return total / len(self.students)

# 使用 GradeBook 類別
grade_book = GradeBook()

try:
    grade_book.add_student("Alice", 85, 90)
    grade_book.add_student("Bob", 78, 82)
    print(f"全班平均成績：{grade_book.get_class_average():.2f}")
    
    student = grade_book.get_student("Alice")
    if student:
        print(f"姓名：{student['name']}, 數學：{student['math']}, 英文：{student['english']}, 平均：{student['average']:.2f}")
    else:
        print("學生不存在！")
    
    # 測試無效成績
    grade_book.add_student("Cathy", 150, 88)  # 應引發錯誤
except ValueError as e:
    print(f"錯誤：{e}")
```
- **說明**：
  - `GradeBook` 類別管理學生資料，`students` 屬性是一個列表，儲存字典格式的學生資訊。
  - `add_student` 方法驗證成績並計算平均值。
  - `get_student` 方法查詢學生，`get_class_average` 計算全班平均成績。
  - 使用例外處理確保成績有效。
- **預期輸出**：
```
全班平均成績：85.50
姓名：Alice, 數學：85, 英文：90, 平均：87.50
錯誤：成績必須在 0 到 100 之間！
```

## 5. 課堂練習
請設計一個 `Library` 類別，實現以下功能：
1. 初始化時創建一個空的書籍列表。
2. 添加書籍（包含書名和作者）。
3. 查詢指定書名是否存在。
4. 顯示所有書籍清單。
5. 使用者輸入書籍資料並測試功能。

### 參考解答
```python
class Library:
    def __init__(self):
        self.books = []  # 儲存書籍的列表
    
    def add_book(self, title, author):
        """添加書籍"""
        book = {"title": title, "author": author}
        self.books.append(book)
        print(f"已添加書籍：{title} by {author}")
    
    def find_book(self, title):
        """查詢書籍"""
        for book in self.books:
            if book["title"].lower() == title.lower():
                return book
        return None
    
    def list_books(self):
        """顯示所有書籍"""
        if not self.books:
            print("圖書館目前沒有書籍。")
        else:
            print("圖書館書籍清單：")
            for book in self.books:
                print(f"書名：{book['title']}, 作者：{book['author']}")

# 主程式
library = Library()

# 添加書籍
while True:
    title = input("請輸入書名（輸入 'q' 退出）：")
    if title.lower() == 'q':
        break
    author = input("請輸入作者：")
    library.add_book(title, author)

# 顯示所有書籍
library.list_books()

# 查詢書籍
search_title = input("請輸入要查詢的書名：")
book = library.find_book(search_title)
if book:
    print(f"找到書籍：書名：{book['title']}, 作者：{book['author']}")
else:
    print(f"未找到書籍：{search_title}")
```
- **說明**：
  - `Library` 類別使用列表儲存書籍（字典格式）。
  - `add_book` 添加新書籍，`find_book` 查詢書籍，`list_books` 顯示清單。
  - 主程式透過迴圈接受使用者輸入，測試所有功能。
- **範例輸出**：
```
請輸入書名（輸入 'q' 退出）：Python Programming
請輸入作者：John Smith
已添加書籍：Python Programming by John Smith
請輸入書名（輸入 'q' 退出）：Data Science
請輸入作者：Jane Doe
已添加書籍：Data Science by Jane Doe
請輸入書名（輸入 'q' 退出）：q
圖書館書籍清單：
書名：Python Programming, 作者：John Smith
書名：Data Science, 作者：Jane Doe
請輸入要查詢的書名：Python Programming
找到書籍：書名：Python Programming, 作者：John Smith
```

## 6. 常見問題與疑難排解
- **問題**：`AttributeError: 'NoneType' object has no attribute 'xxx'`。
  - **解決**：檢查物件是否正確初始化，或方法是否返回 `None`。
- **問題**：忘記傳遞 `self` 參數。
  - **解決**：實例方法的第一個參數必須是 `self`，類別方法使用 `cls`。
- **問題**：類別屬性被意外修改。
  - **解決**：小心操作類別屬性，考慮使用實例屬性替代。

## 7. 回家作業
1. 為 `GradeBook` 類別新增方法，實現按平均成績排序並顯示學生清單。
2. 改進 `Library` 類別，新增檢查重複書名的功能，若書名已存在則提示使用者。
3. 閱讀 Python 官方文件 [docs.python.org](https://docs.python.org/3/) 中的「Classes」章節，了解更多類別細節。

## 8. 延伸學習
- 探索類別的進階特性，如繼承和封裝（第15週介紹）。
- 學習使用 `@property` 裝飾器控制屬性存取。
- 嘗試設計更複雜的類別系統，例如模擬銀行帳戶或購物車。