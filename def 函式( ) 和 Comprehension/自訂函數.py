def sum(a,b):
  c = a+ b
  print('call function')
  print(c)
  return(c)

#沒有帶引數都互叫函式,會發生錯誤
#print(sum())
sum(5,3)

def func_sum(a, b): 
	c=a+b
	return (c)
z = func_sum(10, 15) 
print(z)

print('==================')

def func_sum(a, b): 
	c = a + b * 2 
	return (c)
	
print("1")
z = func_sum(3, 4) 
print("2")
print(z)

print('===================')
def sayhello():
  print('welcome')

if __name__ == '__main__':
  sayhello()

#用定義函式來當作判斷句
def agree():
  return True


if agree():
  print('splendid')
else:
  print('it was unexpected.')

def echo(anything):
  return anything + ' ' + anything

print(echo('str'))

def commentary(color):
  if color ==' red ':
    return "It's a tomato."
  elif color == 'green':
    return "It's a vegetable."
  elif color == 'yellow':
    return "It's a banana."
  else:
    return "I've never heard of the color " + color 

comment = commentary('blue')
print(comment)



#example 
#輸入攝氏溫度，求華氏溫度
def temperature(value):
    return 1.8 * value + 32

if __name__ == '__main__':
    runAgain = True;
    print('攝氏10度轉華氏溫度=',temperature(10))
    print('------------------')
    while(runAgain):
        value = int(input('請輸入攝氏溫度:'))
        result = temperature(value)
        print('華氏溫度=', result)
        inputValue = input('程式還要繼續嗎?(輸入N...結束):')
        if inputValue == 'N':
            runAgain = False
        else:
            runAgain = True