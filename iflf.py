def income():
    while True:
        try:
            text = input("icome: ")
            income = float(text)
            if income < 0:
                print("收入不能為負數")
                continue
            if income > 4090000:
                rate = 0.4
                difference = 721100
            elif income > 2180000:
                rate = 0.3
                difference = 312000
            elif income > 1090000:
                rate = 0.21
                difference = 115900
            elif income > 410000:
                rate = 0.13
                difference = 28700
            else:
                rate = 0.06
                difference = 0
            return income, rate, difference
        except ValueError:
            print("請輸入有效的數字")

def main():
    income_value, rate, difference = income()
    tax = max(0, income_value * rate - difference)
    print(f"tax: {tax:,.0f} 元")

if __name__ == "__main__":
    main()