x=eval(input("請輸入x的值: "))
y=eval(input("請輸入y的值: "))
# if x>y:
#     z=x
# else:
#     z=y
# print(f"最大值為: {z}")


# z=x if x>y else y
# print(f"最大值為: {z}")

#巢狀if else
# if x>y:
#     if x>z:
#         z=x
#     else:
#         z=y
# else:
#     if y>z:
#         z=y
#     else:
#         z=x
# print(f"最大值為: {z}")


# x= float(input("請輸入x的值: "))
# if x>10000 and x>50000:
#     print("D")
# elif x>10000 and x<50000:
#     print("C")
# elif x<10000 and x>5000:
#     print("B")
# else:
#     print("A")


#非對稱if else
x=float(input("請輸入x的值: "))
if x<5000:
    print("A")
elif x<10000:
    print("B")
elif x<50000:
    print("C")
elif x<100000:
    print("D")
else:
    print("E")
