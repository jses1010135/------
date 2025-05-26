import os
import csv
def filetest():
    with open("test.txt", "w", encoding="UTF-8") as f:
       
        f.write("第一行\n")
        f.write("第二行\n")
def filetest1():
    with open("test.txt", "a", encoding="UTF-8") as f:
        f.write("追加的內容\n")
def filetest2():
    with open("test.txt", "r", encoding="UTF-8") as f:
        print("檔案內容：")
        for line in f.readlines():
            print(line.strip())# 去除行尾的換行符號
        #print(f.read(10)) # 讀取前10個字元
            #print(f.readline(10))
        #print(f.read())
        #print(f.readlines()) # 讀取所有行
        #print(f.readline()) # 讀取一行
def filetest_csv():
     with open("test.csv", "w", encoding="UTF-8") as f:
        reader = csv.reader(f)
        reader=next(reader)
        for row in reader:
            print(row)
def main():
    filetest()
    filetest1()
    filetest2()

if __name__ == "__main__":
    main()