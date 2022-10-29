dict1 = {'水瓶座':'1月','雙魚座':'2月','牡羊座':'3月'}

###### key 存在########
#沒有傳入value預設值,返回 key 對應的 value
print(dict1.setdefault('水瓶座'))
print(dict1.get('水瓶座'))      #-----------
#有傳入value預設值,返回 key 對應的 value 
print(dict1.setdefault('雙魚座','12月'))
print(dict1.get('雙魚座','12月'))

#---------字典內容不會改變---------
#---------------get不會改變字典內容

###### key 不存在#########
#沒有傳入value預設值,字典內沒有這個 key ,返回None,新建element入字典 (key:None)
print(dict1.setdefault('金牛座'))
print(dict1.get('金牛座'))
print(dict1)

#有傳入value預設值,字典內沒有這個 key,返回預設值,在字典新建 (key:預設值)
#----------新建字典----------
print(dict1.setdefault('雙子座','5月'))
#---------------get不會改變字典內容
print(dict1.get('巨蟹座','6月'))

print(dict1)

