  # 預設參數
  一般的定義方法就不多說了，直接來看有預設值的參數：  
  
  ![image](https://user-images.githubusercontent.com/112489587/198842494-df855d83-372c-4bbe-8f66-54110a1858fa.png)

  預設參數的用處通常是實作函式重載用的，可以使一個函式在接受引數時更有彈性， 
  而要注意的語法問題是：  
  預設參數在函式定義時一定要放在非預設參數的後面。      
   
  但如果我們想實作無限版的 plus() 函式呢？總不可能一直增加預設參數吧！    
  這時候我們可以用「*」來將引數收集到一個 tuple 中。  
  
 # 收集至 Tuple  
  ![image](https://user-images.githubusercontent.com/112489587/198859882-b4928a73-67f5-4270-9e64-d1b311aa86a1.png)

  透過 * 收集的引數會被放到一個 tuple 中，所以我們可以使用 for 來對它進行迭代。
  
  
#  關鍵字引數 Keyword Argument
  在呼叫 print() 時，我們有時會指定 sep 參數做為分隔輸出的字元，  
  或是使用 end 參數來更改最後的換行字元。  
  像這樣不用理會參數的真正順序，而只要給定名字然後指定值的情況，就是在使用關鍵字引數。  
  如果我們要指定的參數太多而造成版面不簡潔的話，  
  可以考慮使用「**」來拆解一個裝有參數名與值的 dict。  
  
### 拆解 dict  
  ![image](https://user-images.githubusercontent.com/112489587/198860068-8a3e2a99-91ec-4bbc-8f45-2bebd39557c5.png)
  
  上面是在處理呼叫時引數太多的問題，但如果在定義函式時，參數就太多了呢？

### 收集至 Dict
 雖然我們可以用上面的單星號來收集到一個 tuple 中，  
 但這樣哪能知道第幾個元素代表什麼、也無法隨心所欲的選擇參數傳入了。  
 這時我們就可以再次利用 ** 以及 dict 「具名」的性質來定義函式： 

![image](https://user-images.githubusercontent.com/112489587/198860491-78547fcd-fc3c-4d9a-90a9-d028f0b96ca1.png)

注意第 2~5 行，我們還可以順便給定預設值，這不就跟一開始的預設參數一樣了嗎？

![image](https://user-images.githubusercontent.com/112489587/198860522-50e6cd00-ac6c-4b93-bd1d-333b12ab8741.png)

# * 與 ** 雙管齊下
*和 ** 都很方便，但用了 * 就不能指名；而用了 ** 就一定要指名，好像有點美中不足。
  其實我們可以將這兩個合併起來使用，
  就如同我們常看到的一樣，可以接受任意引數： 

![image](https://user-images.githubusercontent.com/112489587/198860793-94be09be-9063-4fef-aee8-c37668f77e1b.png)

唯一要注意的是，* 一定要在 ** 的前面，而呼叫函式時有名字的也一定要在沒名字的後面。  
這種集大成的寫法通常會在 Decorators 時使用，讓 Decorators 可以接受參數數量不同的函式。 

# * 的其它用法

可以在定義函式時使用單獨的 * 來做為非指名參數和指名參數（唯-關鍵字引數，Keyword-Only Arguments）的區隔，底下這個範例結合了最上面的預設參數：   

![image](https://user-images.githubusercontent.com/112489587/198861160-6f096bf2-5550-4ebc-8a61-0bcbbc7b4182.png)

在傳入引數時，在 * 後面的（kw1 和 kw2）一定要以關鍵字引數（指名）傳入    
這個寫法可以限制使用者一定要指名傳入引數，而不是依賴原本的順序 

## 超級集大成  
我們可以將 *args、分隔用的 *、以及 ** kwargs 一起使用：    

![image](https://user-images.githubusercontent.com/112489587/198861341-8fd5e98e-f7b9-4efc-82c6-a5cac9a2fbc3.png)

*args 同時扮演了原本和分隔的角色。

