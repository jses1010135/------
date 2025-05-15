d={"a":36,"b":12,"c":24}
# 1. 使用字典的get方法获取键"a"对应的值
# 2. 如果键不存在，返回默认值0
# 3. 如果键存在，返回对应的值
# 4. 使用print函数输出结果
d.values() # iterator
list(d.keys()) # list
value=d.get("a")
d.items() #取出所有的鍵值對
list(d.items()) # list
d.update({"a":100,"x":21}) # 更新字典
#d.clear() # 清空字典
#d.pop("a") # 刪除鍵值對
for key,value in d.items():
    print(f"{key},{value}") # 取出所有的鍵值對
print(list(d.items())) # list
for key in d.keys():
    print(key)

for value in d.values():
    print(value)