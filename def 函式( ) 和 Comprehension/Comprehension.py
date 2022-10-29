#語法:[ expression for item in iterable ]
#語法:[ expression for item in iterable if condition ]
#語法:[expression for item1 in iterable for item2 in iterable]

#使用appen()方法建立
numlist = []
numlist.append(1)
numlist.append(2)
numlist.append(3)
numlist.append(4)
numlist.append(5)
print(numlist)

#使用range()方法加上for in迴圈建立
numlist = []
for i in range(1,6):
  numlist.append(i)
print(numlist)

#使用list()和range()建立
numlist = list(range(1,6))
print(numlist)

#使用list comprehension + for in 建立
numlist = [number for number in range(1,6)]
print(numlist)

#使用list comprehension建立,可以用運算式靈活改變內容值
numlist = [number -1 for number in range(1,6)]
print(numlist)

#使用list comprehension + for in + if
#語法:[ expression for item in iterable if condition ]

numlist = [number for number in range(1,6) if number % 2 == 1]
print(numlist)

a ='''numlist = []
for number in range(1,6):
  if number % 2 == 1:
    numlist.append(number)
print(numlist)'''
print('語法相當於:\n',a)

print('======================')
#使用巢狀迴圈
rows = range(1,4)
cols = range(1,3)
for row in rows:
  for col in cols:
    print(row,col)
print('======================')
#使用list comprehension和巢狀迴圈
rows = range(1,4)
cols = range(1,3)
cells = [(row,col) for row in rows for col in cols]

for cell in cells:
  print(cell)

for row,col in cells:
  print(row,col)
print('======================')
#Dictionary Comprehensions
#語法:{ key_expression : value_expression for expression in iterable }

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)
print('======================')
#將word變為set
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)
print('======================')
#Set Comprehensions
#語法:{expression for expression in iterable }
a_set = {number for number in range(1,6) if number % 3 == 1}
print(a_set)

#Generator Comprehensions
#  tuple 沒有Comprehensions,使用括號()產生的是generator comprehension

numthing = (number for number in range(1,6))

#傳出的是generator物件
print(type(numthing))
for number in numthing:
  print(number)

#generator只可以使用一次,使用完後就被消滅.
try_again = list(numthing)
print(try_again)
