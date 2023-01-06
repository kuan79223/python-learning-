#call by value
def turbo1(speed):
  print('加速前速度:', speed, '\n 函式裡面的記憶體', id(speed))
  speed += 10
  return speed


if __name__ == '__main__':

  speed = turbo1(60)
  print('加速後的速度:', speed, '\n', '函式外的記憶體', id(speed))


#call by reference
def turbo2(listspeed):
  listspeed[0] += 10
  print('加速前速度: ', listspeed[0], '\n 函式裡面的記憶體', id(listspeed[0]))


if __name__ == '__main__':

  listS = [100]
  turbo2(listS)
  print('加速後的速度: ', listS[0], '\n 函式外的記憶體', id(listS[0]))


# 全域變數的有效範圍
def scope():
  aa = 1  #區域變數中只有 a 有預設值
  print(aa, b)  #列印(區域變數的 a ,主程式的 b )


if __name__ == '__main__':
  a = 10
  b = 20
  scope()
  print(a, b)


def scope():
  global a  #利用global 函式 將a變成全域變數
  a = 1
  b = 2
  print(a, b)  #列印(全域變數a,區域變數b)


if __name__ == '__main__':
  a = 10
  b = 20
  #呼叫函式
  scope()

  print(a, b)  # a 已經變成全域變數,所以列印(1,20)
