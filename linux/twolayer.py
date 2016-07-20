import urllib2, re, string
     
def grab(url, localfile):
    global f
    f = open(localfile,'a')
    num = 1
    while 1:
        getinfo(url)
        if response.find(r'<li class="next">') != -1:
            print 'continue'
            url = url+str(num+1)
            continue
        else:
            print 'yes'
            break
def getinfo(url):
    header = {}
    request = urllib2.Request(url, headers=header, )
    global response
    response = urllib2.urlopen(request).read()
    k = re.findall('<a href="(.+?)" class="inline-block info-table-a-inline-block" target="_blank" title="(.+?)">',response)
    for i in k:
        f.write('http://'+i[1]+'\n')