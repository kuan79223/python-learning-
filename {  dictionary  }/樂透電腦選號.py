import random as r
#印出一組大樂透
if __name__ == '__main__':
  lotto = set()
  while (len(lotto) <= 7):
    random_value = r.randint(1,49)
    lotto.add(random_value)
  print('本期大樂透電腦選號號碼如下:')

  lotlist = list(lotto)
  specialNum = lotlist.pop()
  for item in lotlist:
    print(item,end= ' ')
  print('特別號:%d'% specialNum)

#多組大樂透
for _ in range(5):
  if __name__ == '__main__':
    lotto = set()
    while (len(lotto) <= 7):
      random_value = r.randint(1,49)
      lotto.add(random_value)
    print('本期大樂透電腦選號號碼如下:')

    lotlist = list(lotto)
    specialNum = lotlist.pop()
    for item in lotlist:
      print(item,end= ' ')
    print('特別號:%d'% specialNum)
