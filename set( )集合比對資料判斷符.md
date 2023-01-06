    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}


### ---- & ----交集  AND

*  列印重疊的元素 a & b

![image](https://user-images.githubusercontent.com/112489587/210924591-67d7339e-4943-460f-aa4b-53d702ff9a21.png)


### ---- | ----聯集  OR

*  列印a,b全部元素,重疊只列印一次, a | b                 

![image](https://user-images.githubusercontent.com/112489587/210924618-73558d20-ebe7-46d0-ab99-4d02603763ae.png)


### ----「-」----差集 NOR 

* 計算在只有a才有的元素, a - b

![image](https://user-images.githubusercontent.com/112489587/210924644-1fa13248-286e-4a71-b17f-2aa2f2e8165c.png)

* 計算在只有b才有的元素, b - a

![image](https://user-images.githubusercontent.com/112489587/210924663-03c5e579-acde-4d19-b55d-f97a17afa2fb.png)


### ---- ^ ----對稱差集 XOR

* 只印出不重疊的元素, a ^ b

![image](https://user-images.githubusercontent.com/112489587/210924806-3ea29751-104d-437b-87c9-a2788b4e0208.png)

### ---- == ----等於

print('計算兩個set是否相等\n相同True \n,不同False     \n', a == b) 

![image](https://user-images.githubusercontent.com/112489587/210924847-653e0400-8d9c-4ffa-bee7-5dc0686de1c7.png)

### ---- != ----不等於

* 計算兩個set是否相等,相同False,不同True   a != b

![image](https://user-images.githubusercontent.com/112489587/210924861-63b84c83-c084-4855-b31f-9f0a60d16abd.png)

### ---- in ----是成員 in

* 測試指定元素是否 存在 集合中, a in b

![image](https://user-images.githubusercontent.com/112489587/210924875-57176903-91af-4f17-b32d-e3db3c30534f.png)


### ----not in ----

* 測試指定元素是否【不】存在 集合中, 2 not in b

![image](https://user-images.githubusercontent.com/112489587/210924889-d9e42c8a-2e2b-4801-8c12-81ae50bdece3.png)

