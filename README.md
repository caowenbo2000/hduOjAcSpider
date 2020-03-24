# hduOjAcSpider
杭电oj的交题爬虫  
爬取csdn的博客然后在hduoj进行交题  
# 步骤:
1通过csdn内置搜索获取带有需要的关键词博客链接 这里最多获取三页  
2访问每一篇博客的链接获取所需要的html中匹配<code>xxxx</code>中的cpp代码  
3然后通过hdu的submit的页面post自己需要的代码 这里注意在http报头中要加入自己的cookies  
4拉取个人界面中找到本次所提交的题目 然后判定自己是否通过
# 介绍:
1.main.py是主函数  
2.spiper.py是功能函数  
### 目前ac了两百多道题目
# 效果  
在服务器上运行了20小时左右登上了首页
