- 👋 Hi, I’m @kuan79223
- 👀 I’m interested in ...learning ,ponder
- 🌱 I’m currently learning C and C++ and Python.
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...kuan79223@gmail.com

<!---
kuan79223/kuan79223 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->


#  enumerate
#建立一個2*3的二維陣列並初始化，
#用來儲存2個學生各三科成績，
#再以2層巢狀迴圈將所有成績顯示出來。
if __name__ == '__main__':
    students = [[60,70,80],[67,54,89]]
    #enumerate(sequence, [start=0])
    for index,student in enumerate(students):
        print(index,student)
        for i,score in enumerate(student):
            print('第{0:d}位學生第{1:d}科成績為{2:d}'.format(index+1,i+1,score))


