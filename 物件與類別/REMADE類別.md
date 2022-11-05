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
