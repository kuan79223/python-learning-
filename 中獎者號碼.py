empty_tuple=()
city = '台北',
print(city)
citys = '台北', '台中', '高雄', '台南', '花蓮' 
print(citys)
a,b,c,d,e = citys
print(a,b,c,d,e)

#內容交換
password = 'wordfish'
icecream = 'tuttifuti'
password,icecream = icecream,password
print(password,icecream)

list1 = ['abc','bcsd','sfsf']
print(list1)
print(tuple(list1))

#example
if __name__ == '__main__':
    numbers = [12,32,53,64,57,86,27,38,69]
    names = ['n1','n2','n3','n4','n5','n6','n7','n8','n9']
    internum = int(input('輸入中獎者的編號:'))
    if internum in numbers:
        index = numbers.index(internum) #在list中尋找輸入編號的index
        name = names[index] #再從index編號尋找list中的字串
        print('中獎者姓名:',name)
    else:
        print('無此中獎號碼!')

        