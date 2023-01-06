call by value

def turbo(speed):
  
  print('加速前速度:',speed)
  speed += 10
  return speed

if __name__ == '__main__':
  
  speed_in = int(input('輸入初速度:'))
  
  after_speed = turbo(speed_in)
  print('加速後的速度:',after_speed)


  
  
  
call by reference

def turbo(listspeed):
  
  print('加速前速度:',listspeed[0])
  listspeed[0] += 10

  
if __name__ == '__main__':
  
  speed_in = int(input('輸入初速度:'))

  listS = [speed_in]
  turbo(listS)
  print('加速後的速度:',listS[0])
