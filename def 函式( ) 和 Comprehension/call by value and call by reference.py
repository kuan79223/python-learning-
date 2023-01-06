#call by value  傳值不傳址
def turbo1(speed):
  print('加速前速度:', speed, '\n 函式裡面的記憶體', id(speed))
  speed += 10
  return speed

speed >> 60
記憶體位置 139653733945120

if __name__ == '__main__':

  speed = turbo1(60)
  print('加速後的速度:', speed, '\n', '函式外的記憶體', id(speed))

speed >> 70
記憶體位置 139653733945440



#call by reference 傳址
def turbo2(listspeed):
  listspeed[0] += 10
  print('加速前速度: ', listspeed[0], '\n 函式裡面的記憶體', id(listspeed[0]))

listspeed[0] >> 110
記憶體位置 139653733946720

if __name__ == '__main__':

  listS = [100]
  turbo2(listS)
  print('加速後的速度: ', listS[0], '\n 函式外的記憶體', id(listS[0]))
  
listS[0] >> 110 
記憶體位置 139653733946720




