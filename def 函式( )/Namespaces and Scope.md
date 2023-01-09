### 名稱代表的就是變數名稱，function名稱
   
   * 一個名稱空間內不可以有設定相同的名稱
   * 不同的名稱空間內可以設定相同的名稱，不會衝突

### function內的程式區塊就是建立一個function的名稱空間

* 主程式py(__ name __ )是 __ main __就是全域的名稱空間，在全域名稱空間內定義的變數稱為【全域變數】
* function內如果要改變全域變數的值，建議使用關鍵字「global 全域變數」
## 使用【  locals()  】,【  globals()  】


      animal = 'horse'
      
      def print_global():
        print('在函數裡輸出全域變數\n',animal)  

  
      if __name__ == '__main__:  
      
        print_global()
        print('直接輸出全域變數:',animal)   
      
      兩者輸出皆為   horse
*********************************************************
     
      animal = 'horse'  

      def change_and_print_global():
        print('在函數內交換並輸出全域函數:',animal)
        animal = 'cow'      

      if __name__ == '__main__':
      
         change_and_print_global()
         print('更換後的全域變數:',animal)
      
      輸出
      UnboundLocalError: local variable 'animal' referenced before assignment
      在不同區域使用相同變數名稱,會發生錯誤
*********************************************************

      animal = 'horse'  
      
      def change_local():
        animal = 'cow'
        print('定義在函數裡的變數: ',animal, id(animal))
        
      if __name__ == '__main__':
      
      change_local()    #區域變數與全域變數的位址不同
      print('定義在函數外的變數: ',animal, id(animal))


      定義在函數裡的變數: cow   139651167224304
      定義在函數外的變數: horse 139651167137712

*********************************************************
      
      在函數內使用 global 來改變區域變數 
      animal = 'horse'  

      def change_variable_global():
       
        global animal
        animal = 'cow'       
        print(animal)
        
      if __name__ == '__main__':
      
      change_variable_global()
      print(animal)
      
      在函數內更換全域變數
      cow 139651167224304
      cow 139651167224304

*********************************************************

      animal = 'horse'
      
      def p_local():
        animal = 'cow'
        print('區域變數:',locals())

      p_local()

      輸出    區域變數: {'animal': 'cow'}
      

## 變數影響的範圍

### 函數外的變數:

* 函數內可以顯示該變數內容
* 不屬於函數的區域內都可以使用

### 函數內的變數:

* 只在函數內產生效果，不會影響函數外的變數
* 若函數內沒有進行變數宣告而進行改變內容動作將會產生錯誤訊息



