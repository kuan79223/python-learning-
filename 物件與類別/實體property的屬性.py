#實作屬性attribute的Getter和Setter方法成為一個新屬性(Property)
#目的是讓實體不可以直接存取屬性attribute
'''
方法一:
1.建立attribute的getter
2.建立attributer的setter
3.使用name = property(get,set), 建立name property  
'''
class Country():
  def __init__(self,newname):
    self._name = newname
    #私有屬性 = 使用者輸入
  #自行定義方法
  def getname(self):
    print('get')
    return self._name  #得到私有屬性並回傳
  def setname(self,newname):
    print('set')  #將私有屬性設為使用者輸入
    self._name = newname  
  
  name = property(getname,setname)

city = Country('Taipei')
print(city.name)

city.setname('Taichung')
print(city.name)

print('---------------')
'''方法二、做用decorators
1.@property,定義getter 方法
2.@name.setter,定義setter 方法
'''
class Country():
  def __init__(self,newname):
    self._name = newname
    #私有屬性 = 使用者輸入
  @property
  def name(self):
    print('get')
    return self._name  #得到私有屬性並回傳
  @name.setter
  def name(self,newname):
    print('set')  #將私有屬性設為使用者輸入
    self._name = newname  
  

city = Country('Taipei')
print(city.name)

city.name = 'Taichung'
print(city.name)
#實際上還是可以直接存取_name(attribute)

#僅建立getter property
class Circle():
  def __init__(self,radius):
      self.radius = radius
  @property
  def diameter(self):
    return 2 *self.radius

c = Circle(5)
print(c.diameter)
c.diameter = 20  #無法直接定義參數值
#AttributeError: can't set attribute