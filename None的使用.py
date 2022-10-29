#None代表變數佔著一個記憶體空間，但沒有儲存任何東西
#None轉換為boolean值時代表為False

thing = None
if thing:
  print("It's something")
else:
  print("It's nothing")

#使用 is 檢查是否為None
if thing is None:
  print("It's nothing")
else:
  print("It's something")

#以下，代表是None
''' 
''空字串
[] 空陣列
(,) 空tuple
{} 空的dictionary
set() 空的set '''

def is_none(thing):
  if thing is None:
    print("It's None")
  elif thing:
    print("It's True")
  else:
    print("It's False")

thing = None   #輸出為None
thing = 1      #輸出為True
thing = 0      #輸出為False
is_none(thing)