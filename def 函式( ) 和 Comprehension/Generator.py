#Generators
'''
generator是一個串列資料，可以存放大量資料，
但不會建立和儲存全部資料於記憶體內。

range()產生的就是一個generators

generators只可以使用一次 
'''

print(sum(range(1,101)))
#利用函式創建一個迴圈

def my_range(first = 0, last = 10, step = 1):
  
  number = first
  
  while number < last:
    yield number #透過yield建立generator的元素
    number += step

print(my_range)

ranger = my_range(1,5)
print(ranger)

for x in ranger:
  print(x)
