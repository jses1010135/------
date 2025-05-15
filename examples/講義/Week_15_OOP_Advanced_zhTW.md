# 第 15 週：類別進階應用

## 課程目標
- 理解物件導向程式設計（OOP）的進階概念，包括繼承、多型和封裝。
- 學習使用特殊方法（如 `__str__` 和 `__repr__`）自訂物件行為。
- 掌握如何設計層次化的類別結構，提升程式碼重用性和可維護性。
- 透過實例練習，應用進階 OOP 技術解決實際問題。

## 1. 進階 OOP 概念概述
本週課程深入探討物件導向程式設計的進階特性，基於第14週介紹的類別與物件基礎，進一步學習以下核心概念：
- **繼承（Inheritance）**：允許子類別繼承父類別的屬性和方法，實現程式碼重用。
- **多型（Polymorphism）**：子類別可以重寫父類別的方法，實現不同行為。
- **封裝（Encapsulation）**：隱藏物件內部細節，透過屬性控制存取。
- **特殊方法（Magic Methods）**：自訂物件行為，例如字串表示或運算符重載。

## 2. 繼承
繼承允許一個類別（子類別）繼承另一個類別（父類別）的屬性和方法，子類別可以擴展或重寫父類別的功能。

### 繼承語法
```python
class 父類別:
    pass

class 子類別(父類別):
    pass
```

### 程式碼範例 1：簡單繼承
```python
# 定義父類別
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"我是 {self.name}，今年 {self.age} 歲"

# 定義子類別
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # 呼叫父類別的建構子
        self.student_id = student_id
    
    def introduce(self):  # 重寫父類別方法
        return f"我是學生 {self.name}，學號 {self.student_id}，今年 {self.age} 歲"

# 實例化並測試
person = Person("Alice", 30)
student = Student("Bob", 20, "S12345")
print(person.introduce())
print(student.introduce())
```
- **說明**：
  - `Person` 是父類別，`Student` 是子類別，繼承 `Person` 的屬性和方法。
  - `super().__init__` 呼叫父類別的建構子，初始化 `name` 和 `age`。
  - `Student` 重寫 `introduce` 方法，提供更具體的描述。
- **預期輸出**：
```
我是 Alice，今年 30 歲
我是學生 Bob，學號 S12345，今年 20 歲
```

## 3. 多型
多型允許不同類別的物件以統一方式調用方法，但表現出不同的行為。通常透過方法重寫實現。

### 程式碼範例 2：多型應用
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "我會發出聲音！"

class Dog(Animal):
    def speak(self):
        return f"{self.name} 說：汪汪！"

class Cat(Animal):
    def speak(self):
        return f"{self.name} 說：喵喵！"

# 測試多型
animals = [Dog("小黑"), Cat("小白")]
for animal in animals:
    print(animal.speak())
```
- **說明**：
  - `Animal` 是父類別，定義通用的 `speak` 方法。
  - `Dog` 和 `Cat` 重寫 `speak`，提供各自的實現。
  - 透過迴圈統一呼叫 `speak`，展現不同行為（多型）。
- **預期輸出**：
```
小黑 說：汪汪！
小白 說：喵喵！
```

## 4. 封裝
封裝透過限制對屬性和方法的直接存取，保護物件的內部狀態。通常使用單下劃線（`_attr`）表示「受保護」屬性，雙下劃線（`__attr`）表示「私有」屬性。

### 程式碼範例 3：封裝與屬性控制
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # 受保護屬性
        self.__secret_pin = "1234"  # 私有屬性
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("餘額不能為負數！")
        self._balance = amount
    
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("餘額不足！")
        self._balance -= amount
        return self._balance

# 測試封裝
account = BankAccount("Alice", 1000)
print(f"初始餘額：{account.balance}")
account.balance = 1500  # 使用 setter
print(f"更新後餘額：{account.balance}")

try:
    account.balance = -500  # 應引發錯誤
except ValueError as e:
    print(f"錯誤：{e}")

try:
    account.withdraw(2000)  # 應引發錯誤
except ValueError as e:
    print(f"錯誤：{e}")

# 嘗試訪問私有屬性
try:
    print(account.__secret_pin)  # 應引發錯誤
except AttributeError:
    print("錯誤：無法訪問私有屬性！")
```
- **說明**：
  - `_balance` 是受保護屬性，建議外部不要直接修改。
  - `__secret_pin` 是私有屬性，外部無法直接訪問（實際上會被名稱改進為 `_BankAccount__secret_pin`）。
  - 使用 `@property` 和 `@balance.setter` 控制 `balance` 的讀取和設置。
- **預期輸出**：
```
初始餘額：1000
更新後餘額：1500
錯誤：餘額不能為負數！
錯誤：餘額不足！
錯誤：無法訪問私有屬性！
```

## 5. 特殊方法
特殊方法（或稱魔術方法）是以雙下劃線開頭和結尾的方法，用於自訂物件行為。常見的特殊方法包括：
- `__str__`：定義物件的字串表示（給人類閱讀）。
- `__repr__`：定義物件的詳細表示（給開發者閱讀，通常可重現物件）。

### 程式碼範例 4：使用特殊方法
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        return self.pages

# 測試特殊方法
book = Book("Python Programming", "John Smith", 300)
print(str(book))  # 呼叫 __str__
print(repr(book))  # 呼叫 __repr__
print(f"頁數：{len(book)}")  # 呼叫 __len__
```
- **說明**：
  - `__str__` 提供友好的字串表示，適合 `print`。
  - `__repr__` 提供詳細表示，方便除錯或重現物件。
  - `__len__` 允許 `len()` 函式返回書籍頁數。
- **預期輸出**：
```
Python Programming by John Smith
Book('Python Programming', 'John Smith', 300)
頁數：300
```

## 6. 課堂練習
請設計一個基於繼承的類別系統，實現以下功能：
1. 定義一個 `Vehicle` 父類別，包含屬性 `brand` 和 `year`，以及方法 `describe`。
2. 定義兩個子類別 `Car` 和 `Bicycle`，分別重寫 `describe` 方法，添加特定屬性（`Car` 有 `fuel_type`，`Bicycle` 有 `is_electric`）。
3. 使用 `__str__` 提供友好的字串表示。
4. 測試類別系統，創建多個物件並呼叫方法。

### 參考解答
```python
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def describe(self):
        return f"這是一輛 {self.year} 年的 {self.brand} 車輛"
    
    def __str__(self):
        return self.describe()

class Car(Vehicle):
    def __init__(self, brand, year, fuel_type):
        super().__init__(brand, year)
        self.fuel_type = fuel_type
    
    def describe(self):
        return f"這是一輛 {self.year} 年的 {self.brand} 汽車，燃料類型：{self.fuel_type}"

class Bicycle(Vehicle):
    def __init__(self, brand, year, is_electric):
        super().__init__(brand, year)
        self.is_electric = is_electric
    
    def describe(self):
        electric = "電動" if self.is_electric else "非電動"
        return f"這是一輛 {self.year} 年的 {self.brand} 自行車，{electric}"

# 測試類別系統
vehicles = [
    Car("Toyota", 2020, "Gasoline"),
    Bicycle("Giant", 2022, True),
    Vehicle("Generic", 2018)
]

for vehicle in vehicles:
    print(str(vehicle))  # 呼叫 __str__
    print(f"描述：{vehicle.describe()}")
    print("-" * 30)
```
- **說明**：
  - `Vehicle` 是父類別，定義基本屬性和方法。
  - `Car` 和 `Bicycle` 繼承 `Vehicle`，重寫 `describe` 方法並添加新屬性。
  - `__str__` 提供一致的字串表示。
  - 透過迴圈測試多型，統一呼叫 `describe`。
- **範例輸出**：
```
這是一輛 2020 年的 Toyota 汽車，燃料類型：Gasoline
描述：這是一輛 2020 年的 Toyota 汽車，燃料類型：Gasoline
------------------------------
這是一輛 2022 年的 Giant 自行車，電動
描述：這是一輛 2022 年的 Giant 自行車，電動
------------------------------
這是一輛 2018 年的 Generic 車輛
描述：這是一輛 2018 年的 Generic 車輛
------------------------------
```

## 7. 常見問題與疑難排解
- **問題**：`super().__init__` 呼叫失敗。
  - **解決**：確保父類別有對應的 `__init__` 方法，且參數匹配。
- **問題**：私有屬性仍可被訪問。
  - **解決**：Python 的私有屬性（`__attr`）僅透過名稱改進限制，建議明確文件化存取規則。
- **問題**：`__str__` 和 `__repr__` 結果不一致。
  - **解決**：確保 `__str__` 提供人類可讀的輸出，`__repr__` 提供詳細的技術表示。

## 8. 回家作業
1. 為 `BankAccount` 類別新增方法，支援存款功能，並使用私有屬性保護餘額。
2. 改進課堂練習的 `Vehicle` 系統，新增 `Motorcycle` 子類別，包含屬性 `has_sidecar`。
3. 閱讀 Python 官方文件 [docs.python.org](https://docs.python.org/3/) 中的「Inheritance」和「Special Method Names」章節，了解更多細節。

## 9. 延伸學習
- 探索多重繼承（Multiple Inheritance）的使用與潛在問題。
- 學習其他特殊方法，如 `__eq__`（比較物件是否相等）或 `__add__`（運算符重載）。
- 嘗試設計更複雜的類別層次結構，例如模擬學校管理系統（教師、學生、課程）。