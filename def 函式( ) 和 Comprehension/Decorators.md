###### 修改已經有的function功能，但不需要更改到裏面原本的內容程式碼    
  一個decorator是一個function, 這個function有一個參數，    
  可以利用參數傳入其它function,然後傳出其它修改過的function   
  
* *args 和 **kwargs
* Inner functions
* Functions 當作引數

![image](https://user-images.githubusercontent.com/112489587/198862001-b6d0bcc7-0746-4a6a-86d9-26f9568bc759.png)

#### 手動傳遞function當作參數

![image](https://user-images.githubusercontent.com/112489587/198861833-280b9eaf-8cc5-4739-80b7-83dd0a581702.png)


![image](https://user-images.githubusercontent.com/112489587/198861972-afbd6038-ca06-4df9-9547-b4d057677b14.png)

![image](https://user-images.githubusercontent.com/112489587/198861978-25de3e56-ff30-4b09-9fdc-86111999e0f8.png)

#### 另一種傳遞function當作參數的寫法,使用 @

![image](https://user-images.githubusercontent.com/112489587/198866141-4950dee2-0cd8-40ac-8ab4-207fd1cb732a.png)


#### 也可以傳遞一個function給多個decorator

![image](https://user-images.githubusercontent.com/112489587/198866599-08e80fe5-0eca-4f73-beb1-529caebc02b4.png)

#### 同時使用2個decorator

![image](https://user-images.githubusercontent.com/112489587/198866632-ca992ac2-e450-4f59-8853-f252a164092f.png)

![image](https://user-images.githubusercontent.com/112489587/198866639-59c3841f-9a29-47a1-aee9-0d942a0706ea.png)

#### 改變decorator的順序

![image](https://user-images.githubusercontent.com/112489587/198867210-c326c766-ac78-46e6-b501-7ffb07985854.png)

![image](https://user-images.githubusercontent.com/112489587/198867223-83e2ff8a-282c-47e0-846a-d2650614d635.png)
