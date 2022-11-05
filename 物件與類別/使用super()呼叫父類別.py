class Person():
  def __init__(self,name):
      self.name = name

class Email(Person):
  #當建立自訂的__init__,就不會繼承父類別的__init__
  def __init__(self,name,email):
      super().__init__(name)
      self.email = email 

man = Email('名字','信箱@yahoo.com')
print(man.name)
print(man.email)