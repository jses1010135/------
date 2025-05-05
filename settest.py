import copy
s=set()
s1=set([30,58,87,25,30,65,30])
print(s1)
l=[30,58,87,25,30,65,30]
i=[70,80]
l.extend(i)#extend必須是清單的list
#extend若是字串會將字串拆開來
#l.extend("abc") #extend若是字串會將字串拆開來
l.insert(0, 100)#insert(0,100)在第0個位置插入100
l.remove(30)#remove(30)刪除第一個30
l=list(set(l))#去除重複的元素
l.sort(reverse=True)#sort()#sort(reverse=True)由大到小排序
#l.sort()#sort()由小到大排序
l.reverse()
l.copy()#copy()複製一份清單
i_colone=l.deepcopy()#deepcopy()複製一份清單,但不會影響原本的清單
#l.clear()#清空清單
print(f"l1=",l)
c= list(s1)
s.add(30)
s.add(65)
s.add(87)
s.add(25)
s.add(25)
s.index(30)#index(30)找出30的索引值
s.pop()#pop()隨機刪除一個元素
s.discard(30)#discard(30)刪除30,如果沒有30不會報錯
s.count(30)#count(30)計算30的個數

s.clear()#清空集合
print(s) 
