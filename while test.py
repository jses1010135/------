def test():
    s=0
    n=1
    while n<=10000:
        s+=n
        n+=1
    print("1+2+3+...+10000=",s)

def test2():   
    s=0
    n=1
    while s<=10000:
        if n%2==0:
            n+=1
            continue
        print(n)
        s+=n
        n+=1
    print("1+2+3+...+10000=",s)

def test3():
    s=0
    n=1
    while True:#無窮迴圈,在滿足條件時跳出
        if n%2==0:
            n+=1
            continue
        print(n)
        s+=n
        n+=1
        if s>10000:
            break
    print("1+2+3+...+10000=",s)
def test4():
    students = []
    while True:
        name = input("請輸入姓名:")
        if name == "exit":
            break
        ch=input(int("請輸入國文:"))   
        eng =input(int("請輸入英文:"))
        math=input(int("請輸入數學:"))
        phy=input(int("請輸入物理:"))
        students.append([name, ch, eng, math, phy])
    return students

if __name__ == "__main__":
    test3()
    