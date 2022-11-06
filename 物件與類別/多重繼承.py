class Father():
  def __init__(self,person,words):
      self.person = person
      self.words = words
  #父類別的方法
  def who(self):
      return self.person

  def says(self):
      return self.words + '.'
#繼承父類別
class Mother(Father):
  def says(self):#自定義方法
      return self.words + '?'
#繼承父類別
class Son(Father):
  def says(self):#自定義方法
      return self.words +'!'

father = Father('fa',"That's OK")
print(father.who(),'says:',father.says())

mother = Mother('ma',"what's up")
print(mother.who(),'talk to me:',mother.says())

son = Son('baby','I want play')
print(son.who(),'cry',son.says())



class other():
    def who(self):
      return 'brook'
    def says(self):
      return 'baddling'


def whosays(self):
  print(self.who(),'says',self.says())

whosays(father)
whosays(mother)
whosays(son)