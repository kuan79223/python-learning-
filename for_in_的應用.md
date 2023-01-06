#### 使用時機,讀取所有集合物件元素1次。(list,tuple,string,dictionaries,sets)
#### 使用時機,明確指定執行次數。

        score = ['chinese', 'math', 'english', 'nature']

    '''while loop 陣列長度-------------------------'''
    
        # current = 0
        # while current < len(score):
        #   print(score[current])
        #   current += 1
        
    '''字串陣列沒有 idx 代號, 需要宣告int變數---------'''
       
        # current = 0
        # for idx in score:
        #   print(score[current])
        #   current += 1
        
    '''clean code--------------------------------'''
    
    for idx in score:
        print(idx)

       
        # 字串每次取出一個字元
        
        # word = 'cat'
        # for i in word:
        #     print(i)

    dict = {'room': 123, 'season': 4, 'num': 50}

    # 取出 dict 的 key
    
    for key in dict.keys():
        print(key)
    
    # 取出 dict 的 value
    
    for value in dict.values():
        print(value)
    
    # 取出 dict 的 item
   
    for item in dict.items():
        print(item)

   
    dict = {'room': 'bed', 'ballroom': 'ball'}
    
#### 使用拆解法直接同時取出 key 和 value
    
    for key, value in dict.items():
        
        print('in the', key, 'has', value)






