# Introduce
可以想像你現在手上有一本電子英漢字典，當你輸入英文單字的時候， 就可以查得到它的唯一翻譯。 

    ○ 你所關心的英文單字與翻譯之間有著 一對一 的關係:
        你輸入的英文單字，就叫做 Key
        而得到的翻譯，就叫做 Valu
    ○ 一個 Dictionary 是一群 Key : Value 配對的集合
        資料結構是由 key:value 所組成。
        key 不能夠重複，否則會被後面的結果蓋過去。
        可輸入 key 找尋您要找出來的值。
        如果輸入的 key 不存在，那就會出現錯誤訊息。

![image](https://user-images.githubusercontent.com/112489587/198812667-9e641c30-35d3-48d2-a71d-b249e9d5e0a6.png)

![image](https://user-images.githubusercontent.com/112489587/198812675-274d5433-53c2-4f48-90ba-077ccfb2b054.png)

# 建立字典

![image](https://user-images.githubusercontent.com/112489587/198812912-f6cec82c-2af5-4197-af6c-b3f5763ab003.png)

![image](https://user-images.githubusercontent.com/112489587/198812920-d2341b5d-bd5f-4420-8cd4-9076cec19289.png)



# 複製字典的方法

![image](https://user-images.githubusercontent.com/112489587/198813071-6e23517e-ff1e-4f68-9eb2-0b5a8f02f766.png)

![image](https://user-images.githubusercontent.com/112489587/198813084-01d9bd3f-a5e7-48ad-a493-63e4dd8c1da4.png)


********keys() and values()********

#key 不能於程式內改變:
    可以用數字、字串或者 tuple
    不可以使用 list
#如何找出所有的 key 與 value
    可以透過 dict1.keys( ) 這個方法找出所有的 key
    可以透過 dict1.values( ) 這個方法找出所有的 value
dict1 = {'a':300,'b':400,'c':200}
print(dict1['a'])
print(dict1.keys())
print(dict1.values())

#新增與修改
    #新增一筆資料
        #請將 key 與 value 儲存至一個變數內
        #透過 dict.update(新增的資料) 這個方法的方式就可以新增
#元素可否變更:
    #以 = 指派方式指派給 key 就可以變更資料

add_dic = {'d':800}
add_dict = {'e':60,'f':40}
dict1.update(add_dic)
print(dict1)
print(dict1['d'])
#一次增加多個key,value
dict1.update(add_dict)
print(dict1)


#沒有key就新增
nums={1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
nums[6] = 'six'
print(nums)

#有key就更新
nums[6] = 'SIX'
print(nums)


#刪除動作可分【刪除資料】、【清除所有項目】與【刪除字典】三種:
    del dict[key] 刪除某一個 key 的資料
    dict.clear( ) 清除所有項目
    del dict 刪除字典

dict1 = {'a':100,'b':200,'c':300}
del dict1['c']
print(dict1)
nums = {1: 'one',2: 'two',3: 'three',4: 'four',5: 'five'}
del nums[1] #直接以項目的方式讀取位置
print(nums)
dict1.clear()  
print(dict1)

del nums
print('one' in dict1.values())
#關於 key 的判斷
#請以 (key in dict1.keys( )) 方式進行判斷
    #存在傳回 true
    #不存在傳回 false
print('c' in dict1)

first = {'a':1,'b':2}
second = {'b':'apple'}
first.update(second)
print(first)


