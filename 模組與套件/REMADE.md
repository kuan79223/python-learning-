    可透過import引用其他檔案，就可以使用其他檔案內的類別與函數進行功能擴充。 
    模組就是一個python檔案，模組名稱就是一個檔案名稱 
    Python檔案命名時不要與其他已知模組名稱相同，名稱相同時預設呼叫自己的檔案。  
    
# import模組語法

  1.import 模組   
  2.import 模組 as 新模組名稱  
  3.from 模組 import 模組內方法  
  4.不建議 from 模組 import *，易造成名稱衝突  
  
  
#### 亂數模組
    數值
![image](https://user-images.githubusercontent.com/112489587/200015134-1d69a1f6-fcd9-4bb7-83a7-dc90c4f44c1d.png)

out >> ![image](https://user-images.githubusercontent.com/112489587/200015201-5def7eb8-40d9-43cc-b301-4323f78325cb.png)

    字串
![image](https://user-images.githubusercontent.com/112489587/200017223-b79d1660-6bb5-49b1-9a9b-60afcbcdf06f.png)

out >> ![image](https://user-images.githubusercontent.com/112489587/200017313-7b90948c-ca6a-45bb-a90b-836d8ad9178f.png)


#### 數學函數
    這些函數必須引用 math 模組:
![image](https://user-images.githubusercontent.com/112489587/200017704-2200aa11-1b01-4f8f-84e6-01d97d495d66.png)

![image](https://user-images.githubusercontent.com/112489587/200020285-d22ad189-7516-44ec-a8d4-1ec899c1e6c0.png)

out >> 80.46    
out >> 80   
out >> 81   


#### 自訂模組
    report.py當作模組
![image](https://user-images.githubusercontent.com/112489587/200099399-be68bdf6-d395-400d-ae33-4d0756860f21.png)
    main.py主程式引用report.py模組
![image](https://user-images.githubusercontent.com/112489587/200099432-d716e4b3-119a-4dd1-bfc7-c885e53bb6a6.png)

out >> ![image](https://user-images.githubusercontent.com/112489587/200099445-7924dccb-5630-4124-b636-34d189f97637.png)


#### class定義函數__name__
    module.py模組
![image](https://user-images.githubusercontent.com/112489587/200099724-980cf661-070b-452c-aae8-cd08d1ee6e99.png)

    main.py
![image](https://user-images.githubusercontent.com/112489587/200099730-a993602b-7ab5-4289-9d00-0faf6cf87bd9.png)

out >> ![image](https://user-images.githubusercontent.com/112489587/200099736-96d42897-7422-4408-ba46-977e8e6c44d1.png)


## 自製套件
    套件內可以有多個模組。 
    套件名稱是資料夾名稱。 
    建立一個叫做 happy 的資料夾，裡面放了一個 __ init __.py 的空檔案。    
    每個套件裡都必須存在 __ init __.py 這個檔案，執行初始化的動作，python3版本也可以不用設定
    __ init __.py 可以是空的，也可以放一些變數或程式在裡面。 
    happy 的資料夾內放了一個 __ init __.py 的空檔案，請加入一個名為 my_mod.py 檔案，其內容為:   
    
    創立一個名為sources資料夾,創建daily.py與weekly.py兩個模組
![image](https://user-images.githubusercontent.com/112489587/200100700-363a6f07-3716-464b-b829-d53a0490320f.png)

    daily.py模組
![image](https://user-images.githubusercontent.com/112489587/200100914-21ca78d4-e335-461a-b3de-1cc79a5673c9.png)

    weekly.py模組
![image](https://user-images.githubusercontent.com/112489587/200101015-492c677a-2eda-4474-9160-a5cb45021888.png)

    main.py主程式
![image](https://user-images.githubusercontent.com/112489587/200101103-75164f84-9653-4bf4-8c28-81e67901b62f.png)

    out >>  
![image](https://user-images.githubusercontent.com/112489587/200101114-4a1dbd44-649e-4144-9777-9c9842cd5c81.png)

