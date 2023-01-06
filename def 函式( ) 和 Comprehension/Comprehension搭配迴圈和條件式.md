* 語法:[ expression for item in iterable ]
語法:[ expression for item in iterable if condition ]
語法:[expression for item1 in iterable for item2 in iterable]

#### 使用append()方法建立
numlist = []
numlist.append(1)
numlist.append(2)
numlist.append(3)
numlist.append(4)
numlist.append(5)



#### 使用range()方法加上for in迴圈建立
numlist = []
for i in range(1,6):
  numlist.append(i)

#### 使用list()和range()建立
list1 = list(range(1,6))

#### 使用list comprehension + for in 建立
com_list = [num for num in range(1,6)]
print(com_list)

#使用list comprehension建立,可以用運算式靈活改變內容值
compre_list = [num-1 for num in range(2,7)]
print(compre_list)
