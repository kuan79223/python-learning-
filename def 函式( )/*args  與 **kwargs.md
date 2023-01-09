#### 預設參數
    有預設值的參數：  
  
        def add(a, b, c=None):
        result = a + b + (c if c else 0)
        print(result)

        add(1, 2, 3)
        
        輸出    6

  * 預設參數的用處通常是實作函式重載用的，可以使一個函式在接受引數時更有彈性， 
  * 而要注意的語法問題是：  
    預設參數在函式定義時一定要放在非預設參數的後面。      
   
  * 實作無限版的 plus() 函式
    用「*」來將引數收集到一個 tuple 中。  
  
 #### *收集至 Tuple  
 
      def plus(*nums):
        for i in nums:
          print(i)

      plus(10)

      輸出  10
      透過 * 收集的引數會被放到一個 tuple 中，所以我們可以使用 for 來對它進行迭代。
  
  
###  關鍵字引數 Keyword Argument
  * 在呼叫 print() 時，我們有時會指定 sep 參數做為分隔輸出的字元，  
    或是使用 end 參數來更改最後的換行字元。  
  * 像這樣不用理會參數的真正順序，而只要給定名字然後指定值的情況，就是在使用關鍵字引數。  
  * 如果我們要指定的參數太多而造成版面不簡潔的話，  
    可以考慮使用「**」來拆解一個裝有參數名與值的 dict。  
  
#### 拆解 dict  

      原輸出語法
      print('hello', 'world', sep='#', end='\n\n')

      拆解成 dict
      dict = {'sep': '#', 'end': '\n\n'}
      print('hello', 'world', **dict)
  
      輸出  hello#world
      
      上面是在處理呼叫時引數太多的問題，但如果在定義函式時，參數就太多了

### **收集至 Dict

 * 雖然我們可以用上面的單星號來收集到一個 tuple 中，  
   但這樣哪能知道第幾個元素代表什麼、也無法隨心所欲的選擇參數傳入了。  
 * 這時我們就可以再次利用 ** 以及 dict 「具名」的性質來定義函式： 


          def fun(**settings):
            print(settings)

          fun(name='sky', attack=100, hp=500)

          輸出   {'name': 'sky', 'attack': 100, 'hp': 500}
          
          我們還可以順便給定預設值

### 在函式裡給定預設值 setdefault

      def fun(**settings):
      settings.setdefault('name', 'sky')
      settings.setdefault('attack', 100)
      settings.setdefault('defense', 0)
      settings.setdefault('hp', 500)
      print(settings)

      fun()
      
      輸出   {'name': 'sky', 'attack': 100, 'hp': 500}
      
# * 與 ** 一起使用

* *和 ** 都很方便，但用了 * 就不能指名；
  而用了 ** 就一定要指名，好像有點美中不足。
* 其實我們可以將這兩個合併起來使用，
  就如同我們常看到的一樣，可以接受任意引數： 
  唯一要注意的是，* 一定要在 ** 的前面，
  而呼叫函式時有名字的也一定要在沒名字的後面。  
  這種集大成的寫法通常會在 Decorators 時使用，
  讓 Decorators 可以接受參數數量不同的函式。 


      def fun(a, *args, kw1, **kwargs):
        print(a, args, kw1, kwargs, sep=' # ')


      fun(1, 2, 3, 4, 5, kw1=6, g=7, f=8, l=9)
      
      輸出   1 # (2, 3, 4, 5) # 6 # {'g': 7, 'f': 8, 'l': 9}


### * 的其它用法

* 可以在定義函式時使用單獨的 * 來做為非指名參數和指名參數（唯-關鍵字引數，Keyword-Only Arguments）的區隔，底下這個範例結合了最上面的預設參數：   
     
      def fun(a, b=20, *, kw1, kw2=40):
        print(a, b, kw1, kw2)


      fun(1, 2, kw1=3, kw2=4)
      輸出   1 2 3 4
      fun(10, kw1=30)  
      輸出   10 20 30 40

      在傳入引數時，在 * 後面的（kw1 和 kw2）一定要以關鍵字引數（指名）傳入    
      這個寫法可以限制使用者一定要指名傳入引數，而不是依賴原本的順序 

   




