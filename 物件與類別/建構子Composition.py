print('三個建構子相互呼叫')
class Bill:
  def __init__(self,des):
    self.des = des

class Tail:
  def __init__(self,length):
    self.length = length

class Duck:
  def __init__(self,bill,tail):
    self.bill = bill
    self.tail = tail
  #Duck class method
  def about(self):
    print('This man has a',bill.des,'bill and a',tail.length,'tail')

bill = Bill('【wide orange】')
tail = Tail('【long】')
duck = Duck(bill,tail)
duck.about()


print('子繼承,自創建構子和方法')
# parent class
class Parent:
    # parent class method
    def m1(self):
        print('Parent Class Method called...')
  
# child class inheriting parent class
class Child(Parent):
    # child class constructor
    def __init__(self):
        print('Child Class object created...')
    # child class method
    def m2(self):
        print('Child Class Method called...')

son = Child()
son.m1()
son.m2()

print('兩個建構子與自創方法')
class Component:
    # composite class constructor
    def __init__(self):
        print('Component class object created...')
    # composite class instance method
    def m1(self):
        print('Component class m1() method executed...')
  
class Composite:
    # composite class constructor
    def __init__(self):
        # creating object of component class
        self.obj1 = Component()
          
        print('Composite class object also created...')
    # composite class instance method
    def m2(self):
        print('Composite class m2() method executed...')
        # calling m1() method of component class
        self.obj1.m1()
  
  
# creating object of composite class
obj2 = Composite()
  
# calling m2() method of composite class
obj2.m2()