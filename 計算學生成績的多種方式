#使用range()產一個範圍的數值list
#range()不會像list,tuple,set,dictionary先佔用大量記憶體空間
#語法:range(start, stop, step).
#如果省略start,只有stop,start預設為0
#如同slice,產生的值並不包含stop
#step預設值為1
i = 0
sum = 0
for i in range(1,6):
    num = int(input('輸入第'+str(i)+'位學生的成績:'))
    
    sum += num
print('全班總成績為:',sum,'分,平均為:',sum/5)

print('=====================')


sum = 0
students = 5
for i in range(students):
    score = int(input('請輸入第'+ str(i+1) +'位學生的成績:'))
    sum += score

print("全班總成績為:" + str(sum) + "分,平均分數為" + str(sum/students) + "分")



#小美是一位教師，請你以while迴圈方式為小美設計
# 一個輸入成績的程式，如果輸入負數表示成績輸入結束，
# 在輸入成績結束後,顯示班上總成績及平均成績。

count , sum = 0 , 0
while(True):
    count += 1
    n = int(input('輸入第'+str(count)+'位學生成績:'))
    if(n<0):
        break
    else:
        sum += n             #-1結束迴圈,此時count多1需減回
print('班上總成績',sum,'平均為','%.2f'%(sum/(count-1)))
print("===============================")


nums = 5
scores = []
sum = 0
for i in range(5):  #五位學生 
  i += 1            #i先+1 才不會以index 0輸出
  print('輸入第{0:d}位同學成績'.format(i))
  scores.append(int(input()))  #將每一次輸入加入scores串列中
for score in scores:  #用score 帶出scores串列值
  sum +=  score       
avg = sum / nums
print('全班總分為:{0:d}分,平均為{1:.2f}分'.format(sum,avg))
print("===============================")


total = person = score = 0
while (score != -1):
    person += 1  #每次人數加 1
    total += score  #每次 加輸入成績
    score = int(input('輸入第%d同學成績:' % person))
average = total / (person - 1)
#以-1結束,不算入人數,所以person -1
print('本班總分為%d , 平均成績為%d' % (total, average))

print('============================')


score = []
total = inscore = 0
while (inscore != -1):  #這個while計算學生數量
  inscore = int(input('輸入學生成績'))
  score.append(inscore)  #每一次執行輸入的data加入在score陣列中
print('共有%d位學生' % (len(score)-1)) #執行終止條件為-1,所以元素數目需扣回
for i in range(0, len(score)-1 ):    #這個for迴圈計算總分
  total += score[i]
average = total / (len(score)-1)     #average需貼齊for,否則會進入迴圈
print('本班總分%d分,平均成績%.2f分' % (total,average))
print('==============================')


#以串列方式計算學生成績
#亂數產生50位學生的成績,總分,平均
import random
students = [] #設定空的學生串列
for _ in range(50):  #50位學生
    scores = []  #設定空的分數串列
    for _ in range(5): #5個分數
  #分數串列美執行一次亂數50~100值,放在scores串列中
        scores += [random.randint(50,100)]
  #然後再將scores串列放入students串列裡
    students.append(scores)
studentId = 0 #預設學生人數 0 
for stu in students: #將學生內容印出
    studentId += 1 #每一次學生人數加一
    print('學生:',studentId) #印出全部學生
    print(stu)  #印出學生內容
    sum = 0 #預設總分為 0
    for score in stu: #將學生內容輸出給score變數
        sum += score#每次執行,sum接收學生成績
    print("總分為:",sum,"平均為:",sum/5)
    print()


