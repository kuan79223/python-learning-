#名稱代表的就是變數名稱，function名稱
  #一個名稱空間內不可以有設定相同的名稱
  #不同的名稱空間內可以設定相同的名稱，不會衝突
#function內的程式區塊就是建立一個function的名稱空間
#主程式py(__ name __ )是 __ main __就是全域的名稱空間，在全域名稱空間內定義的變數稱為【全域變數】
#function內如果要改變全域變數的值，建議使用關鍵字「global 全域變數」
#使用【  locals()  】,【  globals()  】

animal = 'horse'
def print_global():
  print('在函數裡輸出全域變數\n',animal)

print_global()
print()

print('直接輸出全域變數:',animal)
print()

#def change_and_print_global():
  #print('在函數內交換並輸出全域函數:',animal)
  #animal = 'cow'  #在不同區域使用相同變數名稱,會發生錯誤
  #print('更換後的全域變數:',animal)

#change_and_print_global()

def change_local():
  animal = 'cow'
  print('定義在函數裡的變數:',animal,id(animal))

change_local()    #區域變數與全域變數的位址不同
print(id(animal))

print('===============')

def change_variable_global():
  print('在函數內更換全域變數')
  global animal
  animal = 'cow'
  print(animal)

change_variable_global()
print()

animal = 'horse'
def p_local():
  animal = 'cow'
  print('區域變數:',locals())

print(p_local())

