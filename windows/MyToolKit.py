import os
import re 
import mysqlmap
import twolayer
import time

targets = 'list1.txt'
fp=open(targets,"r+")		
list=fp.readlines()
ferror = open('error_log.txt',"a")

print list
for i in list:
	i = i.split('----')
	url = "http://alexa.chinaz.com/default.aspx?domain="+i[1].strip('\n')
	os.mkdir('''G:\\py\\wooyunsites\\output\\'''+i[0])
	dirpath = "G:\\py\\wooyunsites\\output\\"+i[0]
	localfile = i[0]+'.txt'
	try:
		twolayer.grab(url, localfile)
		time.sleep(10)
	except:
		#print 'error : '+i[1]
		ferror.write(i[1]+'\n')
	ff = open(localfile,"r+")
	for fff in ff:
		if fff.find("com")!=-1 or fff.find("cn")!=-1:
			print 'target : '+fff
			try:
				mysqlmap.sqlmap_craw(fff.strip('\n'))
			except:
				ferror.write("sqlmap_error : "+fff)
				
	os.system('''xcopy "C:\\Users\\nsfocus\\.sqlmap\\output" %s /e''' %dirpath)
	ff.close()
	os.system('''move %s %s''' %(localfile,dirpath))
	os.system('''rd "C:\\Users\\nsfocus\\.sqlmap\\output" /s /q''')	
			
os.system("python mail.py")
fp.close()
ferror.close()