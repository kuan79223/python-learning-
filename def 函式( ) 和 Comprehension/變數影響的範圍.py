#函數外的變數:
#函數內可以顯示該變數內容
#不屬於函數的區域內都可以使用

#函數內的變數:
#只在函數內產生效果，不會影響函數外的變數
#若函數內沒有進行變數宣告而進行改變內容動作將會產生錯誤訊息

a = 5  #global


def f_sum():
  #a = 10              #函數內未設定,引用前述變數
  print('函數內:', a)
  return


print('函數外1:', a)
f_sum()
print(f_sum.__class__)  #
print(type(f_sum))  #

print('函數外2:', a)
print('===================')

a = 5


def func_sum():
  a = 0
  a = a + 1
  print("函數內:", a)
  return ()


print("函數外1:", a)
func_sum()
print("函數外2:", a)
print('===================')

a = 3


def f_sum():
  a = 7
  a = a + 6
  print(a)
  return


a += 6
f_sum()
print(a)

#example
#輸入四個月的支出金額後列出最多與最少的支出金額。

def pay():
  list1 = []
  for i in range(4):
    print('輸入第{0:d}個月的資出金額:'.format(i+1))
    list1.append(int(input()))
  print('支出最多金額為:', max(list1))
  print('支出最少金額為:', min(list1))
  print('支出的總額為:', sum(list1))
  print('支出金額由小到大排序為:{}'.format(sorted(list1,reverse=False)))
  

pay()