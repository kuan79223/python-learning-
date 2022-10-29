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



