*  你提供的資料就以一筆資料方式加入到 list。     
*  一次只能加入一個資料。     
*  也可利用 【 + 】list 的方式於原本的 list 之後附加新的資料。      

        list1 = ['a','b','c']   
        len(list1)   
        
        out >> 3
        
        list1.append(['def','ghij']) #此陣列算一個字串長度
        
        out >> ['a', 'b', 'c', ['def', 'ghij']]
       
        len(list1)
        
        out >> 4
        print(list1[3])
        

* example       
    empty = []
    sum = 0
    for i in range(1,6):
        word = '請輸入第'+str(i)+'位學生的成績'
        num = int(input(word))
        empty.append(num)
        sum += num
    print('全班總成績為:',sum,'分平均為',sum/len(empty),'分')
    print('============')
* other idea        
    nums = 5
    scores = []
    sum = 0
    for i in range(5):
        i += 1
        print("請輸入第{0:d}位學生的資料:".format(i))
        scores.append(int(input()))

    for score in scores:
        sum += score

    ave = sum / nums
    print("全班總成績為:{0:d}分,平均為{1:.2f}分".format(sum, ave))
    print('============')

* example
sum =0
list1 = []
num = int(input('輸入購買件數:'))
for i in range(num):
    i += 1
    print('輸入第{:d}件商品的價格:'.format(i))
    list1.append(int(input()))

for pay in list1:
    sum += pay
print('全部商品總價為:',sum)   
print('============')
#others
if __name__ == '__main__':
    nums = int(input('輸入購買件數:'))
    products = list()
    count = 1
    sum = 0
    while(count <= nums):
        price = int(input('輸入第{:d}件商品的價格:'.format(count)))
        products.append(price)
        sum += price
        count += 1
    print('全部商品總價為:',sum) 
