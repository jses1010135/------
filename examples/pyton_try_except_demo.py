import os
"""
Python try-except 錯誤處理完整示範程式

本程式展示以下 try-except 的常見用法：
1. 基本 try-except 捕捉錯誤
2. 多個 except 處理不同錯誤類型
3. 使用 else 於無錯誤時執行
4. 使用 finally 不論是否出錯都會執行
5. 自訂錯誤與 raise 語法
"""
def file_not_found():
    try:
        file = open("sample.txt", "r", encoding="utf-8")
        content = file.read()
    except FileNotFoundError:
        print("錯誤：檔案不存在！")
        print("請確認檔案路徑是否正確。")
        # 修正：先以寫入模式開啟檔案
        file = open("sample.txt", "w", encoding="utf-8")
        os.write(file, "這是自動建立的檔案內容。\n")
        
        file.close()
        print("已自動建立檔案 sample.txt")
    else:
        print("檔案內容：")
        print(content)
    finally:
        try:
            file.close()
            print("檔案已關閉。")
        except NameError:
            print("檔案未成功開啟，無需關閉。")

def zero_division_error():
    try:
        num = int(input("請輸入一個數字："))
        result = 10 / num
        print(f"10 除以 {num} 的結果：{result}")
    except ZeroDivisionError:
        print("錯誤：不能除以零！")
    except ValueError:
        print("錯誤：請輸入有效的數字！")

def basic_try_except():
    try:
        result = 10 / 0  # 除以零錯誤
    except ZeroDivisionError as e:
        print("❌ ZeroDivisionError:", e)

def multiple_except():
    try:
        value = int("abc")  # 轉型失敗
        lst = [1, 2, 3]
        print(lst[5])  # 越界存取
    except ValueError as e:
        print("❌ ValueError:", e)
    except IndexError as e:
        print("❌ IndexError:", e)

def try_except_else():
    try:
        number = int("100")  # 正常轉型
    except ValueError as e:
        print("❌ ValueError:", e)
    else:
        print("✅ 轉型成功，值為:", number)

def try_finally():
    try:
        print("🔍 嘗試執行可能出錯的程式碼")
        x = 1 / 1  # 正常情況
    finally:
        print("📌 finally: 無論有無錯誤都會執行")

def try_except_finally():
    try:
        x = int("abc")  # 轉型錯誤
    except ValueError:
        print("❌ 發生 ValueError")
    finally:
        print("📌 finally: 收尾或清理資源")

def custom_exception_demo():
    class NegativeNumberError(Exception):
        """自定義例外類型"""
        pass

    def square_root(x):
        if x < 0:
            raise NegativeNumberError("不能計算負數的平方根")
        return x ** 0.5

    try:
        result = square_root(-9)
    except NegativeNumberError as e:
        print("❌ 自定義錯誤:", e)

def main():
    file_not_found()
    zero_division_error()
    print("=== Python try-except 範例示範 ===")
    basic_try_except()
    multiple_except()
    try_except_else()
    try_finally()
    try_except_finally()
    custom_exception_demo()

if __name__ == '__main__':
    main()
