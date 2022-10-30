shortlist = [1,2,3]
a = 5

#shortlist[a] #超出陣列範圍

try:
  shortlist[a]
except:
  print('Need a position between 0 and',len(shortlist)-1,'but got',a)

while True:
  value = input('Postion [q to quit]? ')
  if value == 'q':
    break
  try:
    a = int(value)
    print(shortlist[a])
  except IndexError as err:  #超出陣列範圍
    print('Bad index:',a)
  except Exception as other: #發生錯誤
    print('Something else broke:',other)


    
    #建立自己的Exception
class UppercaseException(Exception):
  pass

words = ['enie','meen','mitb','MO']
for word in words:
  if word.isupper():  #檢查字串是否都為大寫
    raise UppercaseException(word) #發起錯誤

try:
  raise OopsException('panic')

except OopsException as exc:
  print(exc)