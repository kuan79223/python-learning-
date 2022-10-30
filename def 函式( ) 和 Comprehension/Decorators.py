#一個decorator是一個function, 這個function有一個參數，可以利用參數傳入其它function,然後傳出其它修改過的function

def document(fc):
  #'''內部的函數'''
  def Inner_function(*args, **kwargs):
                    #fc參數傳入內部函數
    print('要執行的function:', fc.__name__)
    print('引數位置:', args)
    print('keyword引數名稱', kwargs)
    #fc參數傳入內部函數
    result = fc(*args, **kwargs)

    print('結果:', result)
    return result

  return Inner_function  

#手動傳遞function當作參數
#外部函數  
def add_1(a, b):
  return a + b
#呼叫 decorator(將外部函數傳入)
cool = document(add_1)  
cool(3, 5)

print('========================')

#另一種傳遞function當作參數的寫法,使用 @
@document    #呼叫 decorator
def add_2(a, b):
  return a + b

add_2(3, 5)

#也可以傳遞一個function給多個decorator
print('========================')

def square(fc):
  
  def Inside_function(*args, **kwargs):
  
    result = fc(*args , **kwargs)
    
    return result * result
  
  return Inside_function

#同時使用2個decorator
@document   #先執行第一個decorator 兩數相加
@square     #再執行第二個decorator 數值相乘
def add_3(a, b):
  return a + b

add_3(3,5)
print('====================')

#改變decorator的順序
@square
@document
def add_4(a, b):
  return a + b 

add_4(3,5)