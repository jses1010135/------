"""
Python Dict 所有內建方法與範例示範程式

本程式展示 Python 中 dict 類型的所有方法使用方式，包含每個方法的操作效果，
並在每個示範函數中加入 try-except 錯誤處理，方便教學或除錯使用。

方法總覽：
------------------------------------------------------------------------------
| 方法名稱         | 用途說明                                                 |
|------------------|----------------------------------------------------------|
| clear()          | 清空字典所有內容                                         |
| copy()           | 回傳字典的淺層複製                                       |
| fromkeys(seq, v) | 以指定鍵序列與預設值建立新字典（類別方法）              |
| get(k, d)        | 取得指定鍵的值，若不存在回傳預設值 d（預設為 None）     |
| items()          | 回傳所有鍵值對的 tuple 可迭代物件                        |
| keys()           | 回傳所有鍵的可迭代物件                                   |
| values()         | 回傳所有值的可迭代物件                                   |
| pop(k[,d])       | 移除並回傳指定鍵的值，若鍵不存在回傳 d 或拋 KeyError    |
| popitem()        | 移除並回傳一個鍵值對（預設為最後插入的項目）            |
| setdefault(k[,v])| 若鍵存在則回傳其值，否則插入鍵與預設值 v 並回傳 v      |
| update(m)        | 使用另一個 dict 或 key-value 組更新目前字典             |
------------------------------------------------------------------------------
"""

def demo_clear():
    try:
        d = {'a': 1, 'b': 2}
        d.clear()
        print("clear:", d)
    except Exception as e:
        print("clear error:", e)

def demo_copy():
    try:
        d = {'a': 1, 'b': 2}
        d2 = d.copy()
        print("copy:", d2)
    except Exception as e:
        print("copy error:", e)

def demo_fromkeys():
    try:
        keys = ['x', 'y', 'z']
        d = dict.fromkeys(keys, 0)
        print("fromkeys:", d)
    except Exception as e:
        print("fromkeys error:", e)

def demo_get():
    try:
        d = {'a': 1, 'b': 2}
        print("get existing:", d.get('a'))           # 回傳 1
        print("get missing with default:", d.get('c', 100))  # 回傳 100
    except Exception as e:
        print("get error:", e)

def demo_items():
    try:
        d = {'a': 1, 'b': 2}
        print("items:", list(d.items()))
    except Exception as e:
        print("items error:", e)

def demo_keys():
    try:
        d = {'a': 1, 'b': 2}
        print("keys:", list(d.keys()))
    except Exception as e:
        print("keys error:", e)

def demo_values():
    try:
        d = {'a': 1, 'b': 2}
        print("values:", list(d.values()))
    except Exception as e:
        print("values error:", e)

def demo_pop():
    try:
        d = {'a': 1, 'b': 2}
        value = d.pop('a')
        print("pop 'a':", value, "; dict:", d)
        # 測試 pop 不存在鍵，使用預設值
        value = d.pop('x', 'not found')
        print("pop 'x':", value)
    except Exception as e:
        print("pop error:", e)

def demo_popitem():
    try:
        d = {'a': 1, 'b': 2}
        item = d.popitem()  # 預設移除最後插入的鍵值對
        print("popitem:", item, "; dict:", d)
    except Exception as e:
        print("popitem error:", e)

def demo_setdefault():
    try:
        d = {'a': 1}
        print("setdefault existing:", d.setdefault('a', 100))  # 回傳 1 不改變值
        print("setdefault new:", d.setdefault('b', 200))       # 插入 b=200
        print("dict after setdefault:", d)
    except Exception as e:
        print("setdefault error:", e)

def demo_update():
    try:
        d = {'a': 1}
        d.update({'b': 2, 'c': 3})
        print("update with dict:", d)
        d.update(d=4, e=5)  # 使用關鍵字參數方式
        print("update with kwargs:", d)
    except Exception as e:
        print("update error:", e)

def main():
    print("=== Dict Method Demonstrations with Error Handling ===")
    demo_clear()
    demo_copy()
    demo_fromkeys()
    demo_get()
    demo_items()
    demo_keys()
    demo_values()
    demo_pop()
    demo_popitem()
    demo_setdefault()
    demo_update()

if __name__ == '__main__':
    main()
