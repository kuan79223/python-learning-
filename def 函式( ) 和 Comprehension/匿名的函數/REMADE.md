#### 定義和呼叫函數
![image](https://user-images.githubusercontent.com/112489587/199970165-062532bb-2e22-4517-965c-96154715d06b.png)
out >> 43


#### 將函數當作參數
![image](https://user-images.githubusercontent.com/112489587/199970096-18e26120-e731-4eb0-aeba-458191ae3289.png)
out >> 43

#### 有引數的函數
![image](https://user-images.githubusercontent.com/112489587/199970209-5fc6ef43-31c5-46b5-96ef-24c87b218f9d.png)
out >> 14

#### 沒有限定參數的數量
![image](https://user-images.githubusercontent.com/112489587/199970254-579489c3-35a4-4580-88e2-af62c1b33fb8.png)
out >> 10

#### Inner Functions
![image](https://user-images.githubusercontent.com/112489587/199970315-83018308-50db-4b65-b069-34d4b78aeb83.png)
out >> ![image](https://user-images.githubusercontent.com/112489587/199970679-ca522d0a-9c78-465f-a005-7ea2e219b209.png)




#### Closures
![image](https://user-images.githubusercontent.com/112489587/199970764-52789843-f3b9-40dd-b063-6e2eb2ca9e4a.png)
![image](https://user-images.githubusercontent.com/112489587/199970842-9b0d6bcb-8d4a-4ca5-9c41-a1d02b620b50.png)

# 匿名的函數 
### lambda 語法定義匿名函數
  不需要定義函數名稱的，只需要用運算式或表達分析語法。  
  Python 使用 lambda 語法定義匿名函數。    
  匿名函數是一個表達式/計算式，並不是一個執行流程區塊。 
  匿名函數可以出現在一般函數不允許的地方，例如像 list 內部或函數 呼叫參數的位置。 
  
### 匿名函數說明
    1.匿名函數會自動返回計算式結果，一般函數必須進行規劃設計才能返回。
    2.匿名函數用於一個計算式的處理，而一般函數可以做更多複雜的事情。
    3.匿名函數語法:
      * lambda 參數: 運算式,資料來源
      * 參數-可能是多個值
      * 資料來源-於第一個之後的都是資料來源，這裏得對應資料輸入

![image](https://user-images.githubusercontent.com/112489587/199973237-7b185aa2-3fb9-4197-9139-af5977bae1a0.png)
out >> wwwpppmoze


#### 匿名函數可用於 list 內，可以快速的處理各種數值計算結果，傳入資料與得到回應。
#### 匿名函數可用於條件分析表達上。

![image](https://user-images.githubusercontent.com/112489587/199974352-8f0bfc2f-55bf-4777-b555-f64bd49d61a9.png)

out >> 
![image](https://user-images.githubusercontent.com/112489587/199974421-3fe47134-c979-4804-87d8-c0b3b33a44b3.png)
  與一般宣告函數的差異: 
![image](https://user-images.githubusercontent.com/112489587/199974900-a95d9288-4ec7-4b1c-935e-40ede8ba9a0b.png)

#### 匿名函數可用於條件分析表達上
![image](https://user-images.githubusercontent.com/112489587/199975687-52139ce4-be43-4297-8cfe-d6938344fd7f.png)

out >> 9996   9996

![image](https://user-images.githubusercontent.com/112489587/199978542-a41ded0c-a0d1-4d33-94ea-ad6a27d89013.png)
out >> False  True

#### 匿名函數用於 for 迴圈
![image](https://user-images.githubusercontent.com/112489587/199981798-9fe297e7-9953-43b7-b54e-bcfd274e5cc8.png)

![image](https://user-images.githubusercontent.com/112489587/199982056-94d0e3bf-a5f2-4496-aff0-054a877786b7.png)

out >> ![image](https://user-images.githubusercontent.com/112489587/199982126-6b36ea06-65ae-4c2e-a8f8-2f346297b1a0.png)

## map 與 filter
  1.用法:map(function, sequence)  
  2.將複合性資料逐一取出項目再傳入到 function 操作，最後以 list 作為回傳值。  
  3.filter( ) 函數用於過濾 list，過濾掉不符合條件的元素，返回由符合條件元素組 成的新 list。  
  4.filter 接收兩個參數，第一個為函數，第二個為 list，list 的每個元素作為參數   
    傳遞給函數進行分析，然後返回 True 或 False，最後將返回 True 的元素放 到新list中。  
    
   ![image](https://user-images.githubusercontent.com/112489587/199985260-1408487b-75f8-4e1a-b48b-5527b9775827.png)

out >> ![image](https://user-images.githubusercontent.com/112489587/199985312-3d6aa0ab-2345-4648-b1f7-64039cad92ee.png)

### map
![image](https://user-images.githubusercontent.com/112489587/199987479-5b0db687-d6a6-44d7-884d-fd69dcba9495.png)

out >> ![image](https://user-images.githubusercontent.com/112489587/199987524-a0496c50-0534-4d10-bc17-3691cbaaa623.png)

### filter
![image](https://user-images.githubusercontent.com/112489587/199990458-dd7bc38e-457b-47a1-93ef-ee5fd6d09f3c.png)

out >> ![image](https://user-images.githubusercontent.com/112489587/199990682-8eef1973-b808-49b9-bdae-bc54545565e9.png)
