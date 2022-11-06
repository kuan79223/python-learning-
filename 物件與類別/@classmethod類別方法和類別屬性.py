#類別方法是為類別建立獨自的類別功能
#@classmethod修飾詞建立類別方法
#使用類別方法和類別屬性時，必需使用-類別名稱.類別屬性或類別名稱.類別方法
#建立類別方法必需要有一個參數(cls),cls代表類別

class A():
  count = 0
  def __init__(self):
      A.count += 1
  def say(self):
      print("I'm a A!")

  @classmethod
  def calculate(lot):
      print('A 有',lot.count,'個')

easy_a = A()
soso_a = A()
hard_a = A()
A.calculate()
easy_a.say()