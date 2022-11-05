class Person():
    def __init__(self,name,age=40,height=180,weight=70):
       #attribute
       self.name=name
       self.age=age
       self.height=height
       self.weight=weight

#繼承
class Student(Person):
    def __init__(self,name,**kwargs):
        print(kwargs)
        #呼叫父類別的initializer
        super().__init__(name,**kwargs)

s1 = Student("robert",age=50,height=179,weight=47)

print(s1.__dict__)

#增加property getter 和 setter
class Student(Person):
    def __init__(self,name,id='1111',**kwargs):
        print(kwargs)
        #呼叫父類別的initializer
        super().__init__(name,**kwargs)
        self.__id = id #__代表不可讀 寫

    #定義id,可以 讀
    @property
    def id(self):
      return self.__id

    @id.setter
    def id(self,num):
      if len(num) == 5:
        self.__id = num
      else:
        self.__id = '1111'

s1 = Student('name',id=12345,age=50,height=179,weight=50)
print(s1.id)

print(s1.__dict__)