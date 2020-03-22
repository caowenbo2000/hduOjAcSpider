import spider
#循环所有题目
problemStart = 1156
problemEnd   = 6000

noexitlist = {1125,1126,1127,1132,1135,1136,1137,1138,1139,1167,1168,1169,1184,1185,1186,1187,1188,1189,1190,1191,1192,1193}

for Problem in range(problemStart,problemEnd):
    #搜索1页链接
    if Problem in noexitlist:
        continue
    spider.getCsdnUrl(Problem,2);