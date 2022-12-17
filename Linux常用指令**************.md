## 安裝 Ubuntu-64bit  虛擬環境
    
依照下列步驟,可以調整虛擬電腦的大小    
* 在 Terminal 輸入兩個指令  
1.    sudo apt update
2.    sudo apt install -y build-essential linux-headers-$(uname -r)
3.    裝置 >> 插入Guest Additions 映像
4.    點選光碟進入 資料夾 >> 右鍵打開 op in Terminal >> 輸入 ls >> 可以看到 AUTORUN.INF 輸入 ./autorun.sh
5.    將作業系統全部關掉 >> 右鍵點選右上角的電池 >> Power Off / Log Out>> Restart... 重新啟動

參考文獻: https://www.google.com/search?q=ubuntu+Guest+Additions+CD&sxsrf=ALiCzsZ3G4SseMP7XOwj-G7vcCMY1PqHRQ:1671201126122&source=lnt&tbs=qdr:y&sa=X&ved=2ahUKEwibuOGrrf77AhVkpVYBHafCBNkQpwV6BAgBEB8&biw=1538&bih=704&dpr=1.25#fpstate=ive&vld=cid:63749e53,vid:zdkl16oAS1k



# Linux 常用指令

### 1.線上查詢幫助命令

    help >> 查看Linux 內置命令的幫助

    ls   >> list , 列出目錄的內容及目錄的屬性信息

    cd	 >> change directory , 當前工作目錄切換到指定目錄

    cp	 >> copy , 複製文件或目錄

    mkdir >> make directories , 創建目錄

    mv	 >> move , 移動或重命名文件

    pwd	 >> print working directory , 顯示當前工作目錄的絕對路徑 

    rm	 >> remove , 刪除一個或多個文件或目錄

    rmdir >> remove empty directories , 刪除空目錄

    find  >> 查找目錄及目錄下的文件

    file  >> 顯示文件的類型

### 2.查看文件及內容處理命令

    cat  >> concatenate，用於連接多個文件並且打印到屏幕輸出或重定向到指定文件中

    more >> 分頁顯示文件內容。

    head >> 顯示文件內容的頭部。

    tail >> 顯示文件內容的尾部。

    cut  >> 將文件的每一行按指定分隔符分割並輸出。

    vi/vim >> 命令行文本編輯器。

### 3.文件壓縮及解壓縮命令

    tar >> 打包壓縮。oldboy

    unzip >> 解壓文件。

    gzip >> gzip 壓縮工具。

    zip >> 壓縮工具。

### 4.信息顯示命令

    uname >> 顯示操作系統相關信息的命令。

    hostname >> 顯示或者設置當前系統的主機名。

    dmesg >> 顯示開機信息，用於診斷系統故障。

    uptime >> 顯示系統運行時間及負載。

    du >> 計算磁盤空間使用情況。

    df >> 報告文件系統磁盤空間的使用情況。

    free >> 查看系統內存。

    date >> 顯示與設置系統時間。
