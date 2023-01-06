      seasons = ['spring','summer','fall','winter']

      for index,element in enumerate(seasons):
         print('第{}個季節為:{}'.format(index+1,element))


![image](https://user-images.githubusercontent.com/112489587/210925431-a0a35835-fe7f-4e77-89ad-958398482cf8.png)




notebook = ['筆記電腦', '商用筆電']
phone = ['APPLE', 'ASUS', 'HTC'] 
home = [3, '冰箱', 2, '洗衣機']
All_3C = [notebook, phone, home]

####　將三個陣列引入陣列中形成２維陣列

![image](https://user-images.githubusercontent.com/112489587/210925781-47e1691d-847e-4264-ad8b-ee2b4fdb296f.png)


#### 建立一個2*3的二維陣列並初始化，
* 用來儲存2個學生各三科成績，
* 再以2層巢狀迴圈將所有成績顯示出來。

      if __name__ == '__main__':

       students = [[60,70,80],[67,54,89]]
       
       for index,student in enumerate(students):
           print(index,student)
           for i,score in enumerate(student):
               print('第{0:d}位學生第{1:d}科成績為{2:d}'.format(index+1,i+1,score))


![image](https://user-images.githubusercontent.com/112489587/210926107-f08e913c-f004-484f-970a-1ffe4e035aa9.png)

