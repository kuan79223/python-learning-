from sources import daily, weekly
#引用sources資料夾內的daily.py與weekly.py模組
print("Daily forecast:", daily.forecast()) 
#drily.py模組內的forecast函數

print("Weekly forecast:")
#使用enumerate抓取weekly.py模組函數內的串列
for number, outlook in enumerate(weekly.forecast(),1):
                            #index從1開始
	print(number, outlook)

