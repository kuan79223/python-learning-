#使用@staticmethod
#靜態類別方法可以不用參數

class Person():
    @staticmethod
    def say():
      print("You can't step twice into the same river.")

Person.say()