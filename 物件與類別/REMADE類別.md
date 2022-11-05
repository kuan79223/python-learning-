## 使用class定義類別  
  * 變數, 稱為屬性(instance attribute)  
  * 函式, 稱為方法(instance method) 

####  建立簡易類別  
![image](https://user-images.githubusercontent.com/112489587/200101917-f141b1e4-853e-4bbf-894e-47fb9077eff8.png)

####  建立一個有自訂初始化功能的類別  
  
  * 引數self代表是呼叫這個實體的參考  
![image](https://user-images.githubusercontent.com/112489587/200101983-481e5070-9cfb-4cdc-a346-6606b6d3f626.png)

#### 建立一個有屬性name  
![image](https://user-images.githubusercontent.com/112489587/200102128-9a09db35-f8ea-4711-bfd0-3d55f45765fa.png)

####  hunter = Person('NAME')
* 尋找Person類別
* 在記憶體內建立實體
* 呼叫Person類別內的__init__(self,name), 將引數字串'NAME'傳遞給參數name
* 儲存'NAME'儲存至實體的name屬性內
* 傳出這個實體的參考
* 將參考儲存至hunter變數

* __init__方法不是一定要實作的  
  name屬性在Person定義的類別內的存取，
  必需使用self.name,但當建立真實的實體後必需使用參考名稱.name 


### 以字典的方式印出類別方法的初始化.ˍˍdictˍˍ
![image](https://user-images.githubusercontent.com/112489587/200110210-971cec90-7598-4c84-ad93-666682cd30ac.png)
out >> 
![image](https://user-images.githubusercontent.com/112489587/200110235-a5512ec7-d61e-496e-bbb7-57841c55e31c.png)

#### 在主程式初始化類別方法 
![image](https://user-images.githubusercontent.com/112489587/200110283-65bdb1e0-3e00-4341-b33d-e8639a5c1cfe.png)

#### 解開dictionary成為引數名稱=value,引數名稱=value 

![image](https://user-images.githubusercontent.com/112489587/200110421-2b651463-7524-4f58-afb3-8fa0920b3eda.png)



    
