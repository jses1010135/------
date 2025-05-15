"""
Python List 所有內建方法與範例示範程式

本程式展示 Python 中 list 類型的所有方法使用方式，包含每個方法的操作效果，
並在每個示範函數中加入 try-except 錯誤處理，方便教學或除錯使用。

方法總覽：
------------------------------------------------------------------------------
| 方法名稱        | 用途說明                                                 |
|-----------------|----------------------------------------------------------|
| append(x)       | 在 list 尾端新增一個元素 x                               |
| extend(iter)    | 把 iterable（如另一個 list）中的所有元素加入目前 list   |
| insert(i, x)    | 在索引 i 的位置插入元素 x                                |
| remove(x)       | 移除第一個出現的元素 x（若無則拋出 ValueError）         |
| pop([i])        | 移除並回傳索引 i 的元素（預設為最後一個）               |
| index(x)        | 回傳第一個出現的元素 x 的索引值                         |
| count(x)        | 回傳元素 x 出現的次數                                   |
| sort()          | 原地升冪排序元素                                         |
| sort(reverse=True) | 原地降冪排序元素                                      |
| reverse()       | 原地將 list 順序反轉                                     |
| copy()          | 回傳 list 的淺層複製（新物件，但指向同一子元素）       |
| clear()         | 移除所有元素，使 list 為空                              |
| del lst[i]      | 移除指定 index 的元素                                    |
| del lst[i:j]    | 移除索引範圍內的元素                                     |
| lst *= n        | 將 list 的內容重複 n 次                                  |
| [expr for x in iterable] | List comprehension 建立新 list                |
------------------------------------------------------------------------------
"""

# 以下為方法示範與主程式，含錯誤處理

def demo_append():
    try:
        lst = ['apple', 'banana']
        lst.append('cherry')
        print("append:", lst)
    except Exception as e:
        print("append error:", e)

def demo_extend():
    try:
        lst = ['apple', 'banana']
        lst.extend(['cherry', 'date'])
        print("extend:", lst)
    except Exception as e:
        print("extend error:", e)

def demo_insert():
    try:
        lst = ['apple', 'banana']
        lst.insert(1, 'blueberry')
        print("insert:", lst)
    except Exception as e:
        print("insert error:", e)

def demo_remove():
    try:
        lst = ['apple', 'banana', 'cherry']
        lst.remove('banana')
        print("remove:", lst)
    except Exception as e:
        print("remove error:", e)

def demo_pop():
    try:
        lst = ['apple', 'banana', 'cherry']
        item = lst.pop()
        print("pop:", lst, "; popped item:", item)
    except Exception as e:
        print("pop error:", e)

def demo_index():
    try:
        lst = ['apple', 'banana', 'cherry']
        index = lst.index('banana')
        print("index of 'banana':", index)
    except Exception as e:
        print("index error:", e)

def demo_count():
    try:
        lst = ['apple', 'banana', 'apple', 'cherry']
        count = lst.count('apple')
        print("count of 'apple':", count)
    except Exception as e:
        print("count error:", e)

def demo_sort():
    try:
        lst = ['banana', 'apple', 'cherry']
        lst.sort()
        print("sort:", lst)
    except Exception as e:
        print("sort error:", e)

def demo_sort_reverse():
    try:
        lst = ['banana', 'apple', 'cherry']
        lst.sort(reverse=True)
        print("sort (reverse):", lst)
    except Exception as e:
        print("sort reverse error:", e)

def demo_reverse():
    try:
        lst = ['apple', 'banana', 'cherry']
        lst.reverse()
        print("reverse:", lst)
    except Exception as e:
        print("reverse error:", e)

def demo_copy():
    try:
        lst = ['apple', 'banana']
        copied = lst.copy()
        print("copy:", copied)
    except Exception as e:
        print("copy error:", e)

def demo_clear():
    try:
        lst = ['apple', 'banana']
        lst.clear()
        print("clear:", lst)
    except Exception as e:
        print("clear error:", e)

def demo_del():
    try:
        lst = ['apple', 'banana', 'cherry', 'date']
        del lst[1]
        print("del index 1:", lst)
        del lst[1:3]
        print("del slice 1:3:", lst)
    except Exception as e:
        print("del error:", e)

def demo_multiplication():
    try:
        lst = [1, 2, 3]
        lst *= 2
        print("multiplication:", lst)
    except Exception as e:
        print("multiplication error:", e)

def demo_list_comprehension():
    try:
        squares = [x**2 for x in range(5)]
        print("list comprehension (squares):", squares)
    except Exception as e:
        print("list comprehension error:", e)

def main():
    print("=== List Method Demonstrations with Error Handling ===")
    demo_append()
    demo_extend()
    demo_insert()
    demo_remove()
    demo_pop()
    demo_index()
    demo_count()
    demo_sort()
    demo_sort_reverse()
    demo_reverse()
    demo_copy()
    demo_clear()
    demo_del()
    demo_multiplication()
    demo_list_comprehension()

if __name__ == '__main__':
    main()
