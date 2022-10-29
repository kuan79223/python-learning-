#call by value
def turbo(speed):
  print('加速前速度:',speed)
  speed += 10
  return speed
if __name__ == '__main__':
  speed = int(input('輸入初速度:'))
  speed = turbo(speed)
  print('加速後的速度:',speed)

#call by reference
def turbo(listspeed):
  print('加速前速度:',listspeed[0])
  listspeed[0] += 10
  
s = int(input('輸入初速度:'))
listS = [s]
turbo(listS)
print('加速後的速度:',listS[0])