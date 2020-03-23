import spider
#循环所有题目
problemStart = 1319
problemEnd   = 6000

cur = open('curproId.txt',mode='r+')
str = cur.read()
problemStart = int(str)
for Problem in range(problemStart,problemEnd):
    #搜索1页链接
    cur = open('curproId.txt', mode='w+')
    print(Problem,file=cur)
    cur.flush()
    spider.getCsdnUrl(Problem,2);