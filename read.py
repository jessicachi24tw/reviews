with open('chicken.txt', 'r')as f:
	for line in f:
		print(line)
#把這檔案當作 as f #r讀取模式 ＃w讀寫模式 #加上with只要檔案走完，檔案自己關閉

data = []
with open('chicken.txt', 'r')as f:
	for line in f:
		data.append(line)
		print(data)
#檔案本身既有換行 ＃print本身也有換行 ＃把變數加入空清單證明\n

data2 = []
with open('chicken.txt', 'r')as f:
	for line in f:
		data2.append(line.strip())
print(data2)
#strip刪除換行\n