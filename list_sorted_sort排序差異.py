#兩者差異:
#sorted( )
    #不會影響 list 本身結構，且可以輸出結果。
#sorted(list項目)。
#sorted( ) 可用來排序任何項目。**********
#sort( )
    #會影響 list 本身結構，
    # 且不可以於操作這個動作時進行輸出。
#list.sort( )
#sort( ) 只能用在list上排序。***********

letters = ['Nopqrs','Fghijk','Abcde']
print(sorted(letters))
letters = ['Nopqrs','Fghijk','Abcde']
letters.sort()
print(letters)

#ord 印出ASCII
letters = ['c','b','a','A']
print((ord('a'),ord('b'),ord('c'),ord('A')))  

a = [5,2,1,9,6]
print(sorted(a))
print(sorted(a,reverse=True)) #反向排序

#example
num = []
internum = int(input('輸入數值:'))
for i in range(internum):
    a = int(input('輸入第{0:d}數值:'.format(i+1)))
    num.append(a)
    
num.sort()
for i in num:
    print(i,end=' | ')
print('最小值:',num[0])

'''排序原則與參數
排序原則:
*數字則依照大小排序。
*字串則依照 ASCII 編碼順序進行排序。
排序原則與參數
可加入的引數名稱:
reverse=True
*有這個參數由大到小排序
*若沒有這個參數則由小到大排序
*key=len
依照 list 內元素字串長度進行排序
*key=str.upper
將 list 內元素轉換為大寫，再依照 ASCII 編碼順序進行排序
*key=str.lower
將 list 內元素轉換為小寫，再依照 ASCII 編碼順序進行排序'''
