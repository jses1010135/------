#range(0,100)=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
#range(0,100,2)=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98]
#range(100,0,-2)=[100,98,96,94,92,90,88,86,84,82,80,78,76,74,72,70,68,66,64,62,60,58,56,54,52,50,48,46,44,42,40,38,36,34,32,30,28,26,24,22,20,18,16,14,12,10,8,6,4,2]
#for i in range(0,100): i=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99
#range=整數清單
# s=0
# for i in range(1,101):
#     s+=i
# print(s)
#s+100次i
#s=5050

# def main():
#     score = eval(input("請輸入分數: "))#eval()函數用來執行一個字符串表達式，並返回表達式的值，即把字符串當成有效的表達式來求值並返回計算結果
#     sum = 0
#     avg=0
#     for i in score:
#         sum += i
#     avg=sum/len(score)
#     print(f"總分: {sum}")
#     print(f"平均: {avg}")
#     print(f"最高分: {max(score)}")
#     print(f"最低分: {min(score)}")
# if __name__ == "__main__":
#     main()

#for i in items.items(): i=(key,value)
#for i in items.values(): i=value
#for i in items.keys(): i=key
# def main():
#     # 定義成績字典
#     scores = {
#         "國文": eval(input("請輸入國文分數: ")),
#         "英文": eval(input("請輸入英文分數: ")),
#         "數學": eval(input("請輸入數學分數: "))
#     }
#     total_score = 0
#     weights = {"國文": 1, "英文": 2, "數學": 3}
    
#     for subject, score in scores.items():
#         total_score += score * weights[subject]
    
#     total_weights = sum(weights.values())
#     avg = total_score / total_weights
    
#     print(f"加權總分: {total_weights}")
#     print(f"加權平均: {avg:.2f}")

# if __name__ == "__main__":
#     main()

# def main():
#     for k in range(1,8,3):
#         for j in range(1,10):
#             for i in range(k,k+3):
#                 print(f"{i}x{j}={i*j}\t",end="")
#             print()
#         print()
    
            
# if __name__ == "__main__":
#     main()

# 輸入10個整數，計算並輸出這10個整數的總和、最大值，並判斷每個整數是否為偶數。
#將這10個整數由大到小排序後輸出。
# 輸入說明：
def input_integer():
    integer=[]#建立空list
    for i in range (10):
        integer.append(int(input(f"請輸入整數{i+1}: ")))#利用append()方法將輸入的整數加入list
    return integer

#加總
def sum_integer(integer):
    sum=0
    for i in integer:#將list中的整數加總
        sum+=i#sum=sum+i
    return sum

#最大值
def max_integer(integer):
    max_value=0
    for i in integer:
        if i>max_value:
            max_value=i
    return max_value

#排序
def sort_sequence_integer(integer):

    for i in range(len(integer)):
        for j in range(i+1,len(integer)):#len()函數返回對象（字符、列表、元組等）的長度或項目的個數
            if integer[i]<integer[j]:#如果第i個元素小於第j個元素，則交換位置
                integer[i],integer[j]=integer[j],integer[i]#交換位置
    return integer
    
        
    

#主程式
def main():
    integer=input_integer()
    max_value=max_integer(integer)
    sort_integer=sort_sequence_integer(integer)
    for num in integer:
        if num % 2 == 0:
            print(f"{num}是偶數")
    sum=sum_integer(integer)
    print(f"總和: {sum}")
    print(f"最大值: {max_value}")
    print(f"輸入的整數序列:{sort_integer}")
    
    print()

    
    
             



if __name__ == "__main__":
    main()



