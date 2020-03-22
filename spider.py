from urllib import request
from urllib import parse
import re
import webbrowser
import time
from fake_useragent import UserAgent
import requests
ua = UserAgent()
log = open('log.txt','a+')

def getCsdnUrl(problem_ ,page_):
    #循环搜索页
    for curpage in range(1,page_):
        #构造sourl链接
        myheaders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'User-Agent': ua.random}
        #360 好搜
        # target = 'https://www.so.com/s?ie=utf-8&fr=none&src=360sou_newhome&q=csdn+hdu+' \
        #          + problem_.__str__() \
        #          +'&pn='\
        #          + curpage.__str__()
        #csdn 搜索
        target = 'https://so.csdn.net/so/search/s.do?q=hdu+'\
                 +problem_.__str__()\
                 +'&p='\
                 +curpage.__str__()
        print('getSoUrl:'+target,file=log)
        print('getSoUrl:' + target)
        soreq = requests.get(url=target,headers=myheaders)#,proxies ={'http':"http://113.88.36.15:9000"})
        #sohtml = request.urlopen(soreq).read().decode('utf-8')
        sohtml = soreq.content.decode('utf8')

        #f=open("./out.html","w+")
        #打印请求request
        #print('headers:',myheaders)
        #print(sohtml,file=f)
        #webbrowser.open("./out.html")

        pattern = re.compile(r'https://blog.csdn.net/[^\s\?"]*')
        Resulturl = pattern.findall(sohtml)
        Resulturl = list(set(Resulturl))
        print(Resulturl,file=log)
        print(Resulturl)
        status = getcsdncode(Resulturl,problem_)
        if(status==1):
            return ;
        #f=open("./out.html","w+")
        #打印请求request
        #print('headers:',myheaders)
        #print(sohtml,file=f)
        #webbrowser.open("./out.html")

def getcsdncode(Csdnurl,proId):
    #循环搜索urllist
    for cururl in Csdnurl:
        myheaders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'User-Agent': ua.random}
        csdnreq = requests.get(url=cururl,headers=myheaders)
        csdnhtml = csdnreq.content.decode('utf-8')
        #print(csdnhtml)
        #f = open("./csdn.html", "w+")
        #print(csdnhtml)
        #webbrowser.open('./csdn.html')
        #处理网页,提取代码
        patternCode = r'<code class="language-cpp">([\s\S.]*?)</code>'
        acCodelist = re.findall(patternCode,csdnhtml)
        #for acCode in acCodelist:
        if len(acCodelist) >= 1:
            acCodelist[0]+='//'
            acCodelist[0]+=cururl
            parsecode(acCodelist[0],proId)
            status = getResult(proId)
            if status ==1:
                return 1;
    return 0;

def parsecode(acCode_,proId):
    #处理代码并且提交
    acCode_=acCode_.replace('&lt;','<')
    acCode_=acCode_.replace('&gt;','>')
    acCode_=acCode_.replace('&amp;','&')
    acCode_=acCode_.replace('&quot;','\"')
    print(acCode_,file=log)
    print(acCode_)
    submmitCode(acCode_,proId)

def submmitCode(acCode_,proId):
    #print(acCode_)
    target = 'http://acm.hdu.edu.cn/submit.php?action=submit'
    mycontent = {'check':'0',
                'problemid': proId.__str__(),
                'language':'0',
                'usercode':acCode_
                 }
    mydata = parse.urlencode(mycontent);
    #print(mydata)
    myheaders = {
        'Host':'acm.hdu.edu.cn',
        'Connection':'keep-alive',
        'Content-Length': len(acCode_).__str__(),
        'Cache-Control': 'max-age=0',
        'Origin': 'http://acm.hdu.edu.cn',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': ua.random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Referer': 'http://acm.hdu.edu.cn/submit.php?pid='+proId.__str__(),
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,ru;q=0.8',
        'Cookie': 'exesubmitlang=0; PHPSESSID=obdmj54f6m1cn6f2epighm9nf0'
    }
    requests.post(url=target,data = mydata,headers = myheaders)
    #print(hdures.status_code,file=log)
    #hduhtml = hdures.content
    #f = open("./hduoj.html", "w+")
    #print(hduhtml,file=f)
    #webbrowser.open(url='./hduoj.html')
    time.sleep(10)

def getResult(proId):
    target = 'http://acm.hdu.edu.cn/userstatus.php?user=caowenbo'
    hdureq = requests.get(url=target)
    hdureqhtml = hdureq.content.decode('gbk')
    str = 'p('+proId.__str__()+','
    index = hdureqhtml.find(str)
    if index == -1:
        print("dont find the string",file=log)
        print("dont find the string")
        return 0;
    index = index + 7
    if hdureqhtml[index] == '0':
        print("Didnt AC",file=log);
        print("Didnt AC")
        return 0;
    else:
        print('Ac',file=log)
        print("AC")
        return 1;