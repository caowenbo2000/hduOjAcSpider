import requests
target = 'http://acm.hdu.edu.cn/userstatus.php?user=caowenbo'
hdureq = requests.get(url=target)
hdureqhtml = hdureq.content.decode('gbk')
str = 'p('+'100123'+',';
index = hdureqhtml.find(str)
print(index)
#print (hdureqhtml[index + 7])