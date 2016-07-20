import os
import re 
import mysqlmap
import time

targets = 'list1.txt'
fp=open(targets,"r+")		
list=fp.readlines()
ferror = open('error_log.txt',"a")
print list

for i in list:
	i = i.split('----')
	url = "http://www.5118.com/subdomains/"+i[1].strip('\s')+"/"
	os.mkdir('''/root/sqlmap-dev/output/'''+i[0])
	dirpath = "/root/sqlmap-dev/output/"+i[0]
	localfile = i[0]+'.txt'
	#try:
		#twolayer.grab(url, localfile)
		#time.sleep(10)
	#except:
		#print 'error : '+i[1]
		#ferror.write(i[1]+'\n')
	ff = open(localfile,"r+")
	for fff in ff:
		if fff.find("com")!=-1 or fff.find("cn")!=-1 or fff.find("tw")!=-1:
			print 'target : '+fff
			try:
				mysqlmap.sqlmap_craw(fff.strip('\n'))
			except:
				ferror.write("sqlmap_error : "+fff)
				
	os.system('''mv -f /root/.sqlmap/output/* %s'''%dirpath)
	os.system("mv %s %s" %(localfile,dirpath))
os.system("python mail.py")
fp.close()
ff.close()
ferror.close()
