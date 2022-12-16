# Log檔

 
### 默認情況下 Python 的 logging模塊 將日誌打印到了標準輸出中，且只顯示了大於等於 warning 級別的日誌，    
### 這說明默認的日誌級別設置為 WARNING（日誌級別等級critical > error > warning > info > debug），  
### 默認的日誌格式為日誌級別：level級別:用戶:輸出消息。   

        logging.debug( ' debug message ' )          #計算或者工作的細節
        logging.info( ' info message ' )            #記錄一些用戶的增刪改查的操作
        logging.warning( ' warning operation ' )    #警告操作
        logging.error( ' error message ' )          #錯誤操作
        logging.critical( ' critical message ' )    #致命的錯誤直接導致程序出錯退出的

## logging.basicConfig()函數中可通過具體參數來更改 logging模塊 默認行為             
   
                        level：設置logger的日誌級別(大於等於這個參數的級別都會顯示) 
    logging.basicConfig( level=logging.INFO,                            
                    
                    指定handler使用的日誌顯示格式
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    
                    指定日期時間格式
                    datefmt='%Y-%m-%d %H:%M:%S',                    
                    
                    用指定的文件名創建FiledHandler，這樣日誌會被存儲在指定的文件中
                    filename='log.txt',
                    
                    文件打開方式，在指定了filename時使用這個參數，默認值為“a”還可指定為“w”。
                    filemode='w')

    stream：用指定的 stream 創建 StreamHandler 。
    可以指定輸出到 sys.stderr,sys.stdout 或者 
    文件(f = open('test.log','w'))，
    默認為 sys.stderr 。
    若同時列出了 【 filename 】 和 【 stream 】兩個參數，
    則 stream 參數會被忽略。


## 【format】參數中可能用到的格式化串：      
     %(asctime)s       字符串形式的當前時間。默認格式是“2003-07-08 16:49:45,896 ”。逗號後面的是毫秒(可用datefmt修改默認日期時間格式。) 
     % (filename)s     存成 log 檔的 txt 檔名
     % (lineno)d       輸出程式所在的代碼行
     % (levelname)s    日誌級別   critical > error > warning > info > debug
     % (message)s      輸出的訊息
     % (name)s         用戶的名字  默認名為 root

     % (levelno)s      數字形式的日誌級別
     % (pathname)s  調用日誌輸出函數的模塊的完整路徑名，可能沒有
     % (module)s       輸出函數的模塊名
     % (funcName)s     輸出函數的函數名
     % (created)f      當前時間，用UNIX標準的表示時間的浮點數表示
     % (relativeCreated)d 輸出日誌信息時的，自Logger創建以來的毫秒數
     % (thread)d 線程ID。可能沒有
     % (threadName)s 線程名。可能沒有
     %(process)d 進程ID。可能沒有

## 3.對象的配置    
    import logging
    創建一個log變數    ▉ logging.getLogger()
    logger = logging.getLogger()    
    設置顯示級別       ▉ setLevel(logging.級別)
    logger.setLevel(logging.DEBUG)  

    控製文件輸出的 log 檔   ▉ logging.FileHandler()
    fh = logging.FileHandler(' mylog.log ', encoding=' utf-8 ')  
                                            指定編碼可以解決中文亂碼問題

    控制屏幕輸出 顯示在Console     █ logging.StreamHandler()
    sh = logging.StreamHandler()

    創建 format (多個格式也可以)   █   logging.Formatter
    fmt = logging.Formatter(' %(asctime)s - %(name)s - %(levelname)s - %(message)s [line:%(lineno)d] ')

    log 檔格式  █  setFormatter()
    fh.setFormatter(fmt)
    
    可以設置寫入 log檔 的級別,不設置的話就默認用 log 對象設置的級別(一般全部級別的信息都寫進去)
    fh.setLevel(logging.WARNING) █  

    Console 格式
    sh.setFormatter(fmt) 
    
    可以設置 Console 的級別,不設置的話就默認用 log 對象設置的級別
    sh.setLevel(logging.WARNING)  
    
    【但是不能設置比 log檔 級別低，否則只會執行 log檔 的級別，
    比如：log檔 設置的級別是 WARNING，你這裡設置 INFO，級別沒有 WARNING 高，不會顯示】

    用logger 變數來綁定：log檔 , Console
    
    logger.addHandler(sh)   █  addHandler
    logger.addHandler(fh)
    
    logger.debug(' debug message ')         # 計算或者工作的細節
    logger.info(' info message ')           # 記錄一些用戶的增刪改查的操作
    logger.warning(' warning message ')     # 警告操作
    logger.error(' error message ')         # 錯誤操作
    logger.critical(' critical message ')   # 批判的直接導致程序出錯退出的
    
    
 ## 4.工作中的使用案例      
 
    import logging


    def init_log(data):
        
        log_id = data.get( " log_id " , None)   #從參數中獲取日誌id
        
        logger = logging.getLogger(str(log_id))   
        
        logger.setLevel(logging.INFO)   

        #避免重複生成新的logger，日誌多次寫入的問題
        #避免這種情況：第一條記錄寫一次，第二條記錄寫兩次，第三條記錄寫三次
        
        if  not logger.handlers:
            fh = logging.FileHandler( ' mylog.log ' , encoding= ' utf-8 ' )   
            
            fmt = logging.Formatter( ' %(asctime)s - %(name)s - %(levelname)s - %(message)s [line:%(lineno)d] ' )
             
            fh.setFormatter(fmt)
            
            # fh.setLevel(logging.WARNING) 
             
            logger.addHandler(fh)


    def write_log(data):
        
        log_id = data.get( " log_id " , None)   #從參數中獲取日誌id
        
        logger = logging.getLogger(str(log_id))   #根據log_id創建一個log對象
        
        #在需要打印日誌的地方，直接打印日誌即可，上面的init_log已經實例化完畢
        
        logger.error( "錯啦！" )



# 自動刪除功能
    通過 TimedRotatingFileHandler 可以把輸出重定向到文件，它會對比文件最後修改時間和當前時間，
    如果比設置的時候大，則會把當前文件加時間後綴備份，然後，新建一個進行Log。
    
    import logging
    from logging.handlers import TimedRotatingFileHandler


    def init_log(data):
        log_id = data.get( " log_id " , None)
        logger = logging.getLogger(str(log_id))
        logger.setLevel(logging.INFO)

        if  not logger.handlers:
            #這裡設置成 TimedRotatingFileHandler 
            #創建一個由時間控制的 log檔：每天生成一個 txt
                                           檔名                      單位           間隔週期     備分個數
            tfh = TimedRotatingFileHandler(filename= ' mylog.log ' , when= " D " , interval=1, backupCount=3 )                                                                             
            fmt = logging.Formatter( ' %(asctime)s - %(name)s - %(levelname)s - %(message)s [line:%(lineno)d] ' )
            tfh.setFormatter(fmt)
            logger.addHandler(tfh)

            filename： log檔名
            when：是一個字符串，用於描述滾動週期的基本單位，字符串的值及意義如下：
            S: Seconds
            M: Minutes
            H: Hours
            D: Days
            W: Week day (0 = Monday)
            midnight: Roll over at midnight
            interval: 滾動週期，單位由 when 指定，比如：when='D',interval=1，表示每天產生一個日誌文件；
            backupCount: 表示日誌文件的保留個數；

    def write_log(data):
        log_id = data.get( " log_id " , None)
        logger = logging.getLogger(str(log_id))
         #在需要打印日誌的地方，直接打印日誌即可，上面的init_log已經實例化完畢
        logger.error( "錯啦！" )
        
# 通過文件大小設置備份並刪除 
    使用RotatingFileHander對log的文件大小進行限制
    
    import logging
    from logging.handlers import RotatingFileHandler


    def init_log(data):
        log_id = data.get( " log_id " , None)
        logger = logging.getLogger(str(log_id))
        logger.setLevel(logging.INFO)

        if  not logger.handlers:
            # 創建一個由文件大小控制的 log檔
            # 文件大小最大為1MB，超過時自動備份，最多備份3個，超過三個刪除最早的記錄
            tfh = RotatingFileHandler(filename= ' mylog.log ' , maxBytes=1024 * 1024, backupCount=3 )
            fmt = logging.Formatter( ' %(asctime)s - %(name)s - %(levelname)s - %(message)s [line:%(lineno)d] ' )
            tfh.setFormatter(fmt)
            logger.addHandler(tfh)


    def write_log(data):
        log_id = data.get( " log_id " , None)
        logger = logging.getLogger(str(log_id))
         #在需要打印日誌的地方，直接打印日誌即可，上面的init_log已經實例化完畢
        logger.error( "錯啦！" )
