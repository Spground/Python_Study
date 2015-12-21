
#re.match(pattern, string, flag=0)函数 只匹配字符串的开始，匹配失败返回None

import re

str = "ggg.dlut.edu.www"
matchObj = re.match('www', str)#返回一个匹配对象
#print(matchObj.group())

#re.serach()扫描整个字符串并返回第一个成功的匹配
str = "www.dlut.edu.www"
searchObj = re.search('www', str)
print(searchObj.group())

line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) (.*)', line, re.M|re.I)

if searchObj:
   print("searchObj.group() : ", searchObj.group())
   print("searchObj.group(1) : ", searchObj.group(1))
   print("searchObj.group(3) : ", searchObj.group(3))
else:
   print("Nothing found!!")
