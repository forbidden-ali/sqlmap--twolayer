import os
import re 
import mysqlmap
import twolayer
import time

#ferror = open('error_log.txt',"a")
print list
os.mkdir('''G:\\py\\wooyunsites\\output\\erro_again''')
dirpath = "G:\\py\\wooyunsites\\output\\erro_again"
	
localfile = 'error_log.txt'
ff = open(localfile,"r+")
for fff in ff:
	if fff.find("com")!=-1 or fff.find("cn")!=-1:
		print 'target : '+fff
		try:
			fff = fff.split(' : ')[1]
			print fff
			mysqlmap.sqlmap_craw(fff.strip('\n'))
		except:
			print 'error_again:'+fff
				
os.system('''xcopy "C:\\Users\\nsfocus\\.sqlmap\\output" %s /e''' %dirpath)
os.system("move %s %s" %(localfile,dirpath))
os.system('''rd "C:\\Users\\nsfocus\\.sqlmap\\output" /s /q''')	
			
#os.system("python mail.py")
fp.close()
ff.close()
ferror.close()