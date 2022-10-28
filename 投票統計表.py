'''設計一個投票統計表，
包含計算各四位歌手3個地區投票數及總得票數，
最後顯示得票數和得票率(計算至小數2位)'''

if __name__ == '__main__':
    names = ['阿名', '小可', '老王', '大熊']
    for index, name in enumerate(names):
        print('name[{0:d}]:{1:s}'.format(index, name))
    votes = [[10, 20, 30], [50, 70, 80], [45, 34, 78], [56, 74, 93]]
    totalvotes = 0
    for personvotes in votes:  # 用單人票數帶出二維票數
        for vote in personvotes:  # 再把單人票數一一拆解
            totalvotes += vote
    print('參與投票人數:', totalvotes)
    data = {}
    for index, name in enumerate(names):
        man = {name: votes[index]}  # man字典{人名:票數}
        data.update(man)  # 將man字典更新到data字典
    print(data)
    '''comprehension 理解上述的迴圈
    data = {name:votes[index] for index,name in enumerate(names)}
    print(data)
    '''
    # dict.items()以列表返回可遍歷的(鍵, 值) 元組數組。
    for man in data.items():  # 用items()帶出man的每一個keys,values
        name = man[0]  # 每一個元素為[0_keys,1_values]
        scores = man[1]
        personsum = 0
        print(man)

        for score in scores:  # 用score帶出scores裡的每一筆票數
            personsum += score  # 將一筆票數加總
        print('{0:s}總票數為:{1:d}'.format(name, personsum))
        print('{0:s}得票率為:{1:.4f}%\n'.format(name, personsum / totalvotes))