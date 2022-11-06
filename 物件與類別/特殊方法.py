class Word():
	def __init__(self, text):
		self.text = text
	
  #判斷兩變數字母是否一樣
	def equals(self, word2):
		return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')

print(first.equals(second))

#特殊方法
class Word():
	def __init__(self, text):
		self.text = text
	
	def __eq__(self, word2):
		return self.text == word2.text

first = Word('ha')
third = Word('eh')
print(first.__eq__(third))
print(first)  #顯示記憶體
# Table 6-1. Magic methods for comparison  
# __eq__(self, other) self==other  
# __ne__(self, other) self!=other  
# __lt__(self, other) self<other  
# __gt__(self, other) self>other  
# __le__(self, other) self<=other  
# __ge__(self, other) self>=other  


# Table 6-2. Magic methods for math  
# __add__(self, other)  
# __sub__(self, other)   
# __mul__(self, other)   
# __floordiv__(self, other)   
# __truediv__(self, other)  
# __mod__(self, other)  
# __pow__(self, other)  

# Table 6-3. Other, miscellaneous magic methods  
# __str__(self) str(self)  
# __repr__(self) repr(self)  
# __len__(self) len(self)  
print('---------------')
#Example:
class Word():
	def __init__(self, text):
		self.text = text
		
	def __eq__(self, word2):
		return self.text.lower() == word2.text.lower()
		
	def  __str__(self):
		return self.text 
	
	def __repr__(self):
		return Word('self.text')
    #可以輸出引數
first = Word('ha')
print(first)
