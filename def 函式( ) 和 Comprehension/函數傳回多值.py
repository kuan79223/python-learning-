#Python 的函數可以傳回多值。
#傳回多值的做法是將傳回值轉為 tuple 型態，接收後再拆解給變數。

def manyvalue(a , b):
  c = a * b
  return (a-2,b+3,c)

x, y, z = manyvalue(3,5)
print(x,y,z)

def a():
  return 1,2,3,4

tup = a()
print(type(tup))

#example
def cycle(n):
  i = 1
  while True:
    if i > n:
      return
    print(i)
    i += 1
if __name__ == '__main__':
  num = int(input('輸入數值:'))
  cycle(num)
