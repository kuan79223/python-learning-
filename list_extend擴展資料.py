#如果引號括起來的字串有 [ ] 
# 將會拆解成好幾個資料。
#可以把其他 list 加入到這個 list 內，
# 擴展多個欄位。
list1 = ['a','b','c']
print(len(list1))
list1.extend(['def','ghij']) #此陣列拆解成2個字串
print(list1)
print(len(list1))
print(list1[3])
print('==========')

citys = ['台北', '台中', '高雄']
citys.append('台南')
print(citys)
citys.extend('台南')
print(citys)
citys = ['台北', '台中', '高雄']
others = ['花蓮','台東']
citys.append(others)
print(citys)
citys.extend(others)
print(citys)

#entend  視同  +=
citys = ['台北', '台中', '高雄']
others = ['花蓮','台東']
citys += others
print(citys)