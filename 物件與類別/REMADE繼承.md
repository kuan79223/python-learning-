### 因為有繼承的關係，有父類別和子類別區分

    透過建立全新的類別，以便擴充現有的類別功能。  
![image](https://user-images.githubusercontent.com/112489587/200107841-111ed430-c794-4198-b5ff-56613dd70e0f.png)

    呼叫方法print_()時,程式自動會將實體的參考傳給參數self   
![image](https://user-images.githubusercontent.com/112489587/200107871-7f6457e5-e4c9-431c-81bc-48339e34fc0c.png)


    子類別透過覆寫更改父類別方法的功能   
![image](https://user-images.githubusercontent.com/112489587/200108383-27780faa-1dcb-4055-9c0e-dfb8c135fd48.png)


#### 實作__init__()就是覆寫父類別的__init__()

![image](https://user-images.githubusercontent.com/112489587/200109370-5537955b-1eb2-4cbd-90d1-cf2bff687b69.png)

![image](https://user-images.githubusercontent.com/112489587/200109569-275819d9-7dba-4d97-a875-a646f2792d12.png)

out >> ![image](https://user-images.githubusercontent.com/112489587/200109585-b555fe1a-caf9-4ed9-8212-55cf85e626d2.png)


### super( ).ˍˍinitˍˍ()繼承說明 
參考文獻 : https://ithelp.ithome.com.tw/articles/10222948

![image](https://user-images.githubusercontent.com/112489587/200110996-eaa96a90-3572-483f-b01f-452980a19ae7.png)

out >> ![image](https://user-images.githubusercontent.com/112489587/200111012-85dcff9a-f9e8-416f-a392-dde286f1127f.png)

### setter 和 getter 操作私有屬性
    
    這樣的方式也會讓使用者輕易把屬性替換掉
![image](https://user-images.githubusercontent.com/112489587/200111903-60dab0be-7c55-4c9c-93a5-80dbd7a05811.png)

    在屬性前加上[ _ ]轉換成私有屬性  
![image](https://user-images.githubusercontent.com/112489587/200111983-3fc118b2-58a0-4182-9dca-e4bb1757ac32.png)
    這樣雖然屬性變安全了，但是卻沒辦法取出
    
### 加上 get 和 set 方法來操作私有屬性：    
![image](https://user-images.githubusercontent.com/112489587/200112013-464c39bc-98ca-413a-8369-59b78de44ddd.png)

### Property
    透過 property 可以將該方法轉變成屬性的操作方式    
![image](https://user-images.githubusercontent.com/112489587/200112357-6924332d-27ea-4c31-bec2-48afe5d6c3b0.png)

    這樣的話使用者仍然可以透過 .driver 來查看屬性但不能直接複寫屬性
![image](https://user-images.githubusercontent.com/112489587/200112399-13f1f65f-3185-4106-81b9-af7d7ad77f71.png)

### setter and getter
![image](https://user-images.githubusercontent.com/112489587/200112805-e5afb24a-658f-4509-851e-90a7076c3993.png)

out >> ![image](https://user-images.githubusercontent.com/112489587/200112811-d391abdf-14c0-414c-89de-a25309458c53.png)

### 使用者也更容易透過 setter 方法來管理使用者輸入的值   
![image](https://user-images.githubusercontent.com/112489587/200112951-36b7cfb2-6251-4f76-b8cb-c73933b67bb5.png)
    判斷輸入不是字串,報錯      
![image](https://user-images.githubusercontent.com/112489587/200112959-fe9c708a-3c45-4925-a7ac-8a1beeda314a.png)

參考文獻: https://medium.com/bryanyang0528/python-setter-%E5%92%8C-getter-6c08a9d37d46



