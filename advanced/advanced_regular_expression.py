
#re.match(pattern, string, flag=0)函数 只匹配字符串的开始，匹配失败返回None

import re

str = "ggg.dlut.edu.www"
matchObj = re.match('www', str)#返回一个匹配对象
#print(matchObj.group())

#re.serach()扫描整个字符串并返回第一个成功的匹配
str = "www.dlut.edu.www"
searchObj = re.search('www', str)
print(searchObj.group())

line = "Cats are smarter than dogs"

searchObj = re.search( r'(.*) are (.*?) (.*)', line, re.M|re.I)

if searchObj:
   print("searchObj.group() : ", searchObj.group())
   print("searchObj.group(1) : ", searchObj.group(1))
   print("searchObj.group(3) : ", searchObj.group(3))
else:
   print("Nothing found!!")

str = "12-55555 kom Tim street 25-56986"
obj = re.search(r"\d{2}-\d{5}", str)
print(obj.group(0))

#re.match()和re.search()的区别
#re.match只匹配字符串的开始，如果字符串不符合正则表达式，则匹配失败函数返回None，而
#re.search()匹配整个字符串，直到找到一个匹配

str = "Cats is smarter than dogs"
obj = re.match(r'dogs', str, re.M|re.I)
if obj:
   print("match--->", obj.group())
else:
   print("No match")

obj = re.search(r'dogs', str, re.M|re.I)
if obj:
   print("search---->", obj.group())
else:
   print("No match")

#检索和替换
#re.sub
#re.sub(pattern, rep1, string, max=0)
phone = "2004-959-959 # this is a phone number "
num = re.sub(r'#.*$', "", phone)
print(num)

num = re.sub(r'\D', "", phone)
print(num)

#正则表达式修饰符号-可选标志
#re.I 匹配大小写不敏感
#re.L
#re.M 多行匹配，影响^和$
#re.S 使.匹配包括换行符的所有字符
#re.U 根据Unicode字符集解析字符，这个标志影响\w \W \b \B
#re.X

#字母和数字表示他们本身 多数字母和数字前加一个\会拥有不同的含义
def show(r, str):
   obj = re.search(r, str)
   print(obj.group())
   pass


#\d 数字 {n} 重复n次 {n, m}n - m次重复
str = "i am 0411-84701131, addr is  7#202"
r = r'\d{4}-\d{8,9}'
show(r, str)

#^字符串开头 $字符串结束 .任意字符 *0或多次 +匹配1或多次连续的
r = r'^.*$'
show(r, str)

r = r'(\d+)'
show(r, str)

#? 等价于{0,1}0次或1次匹配 
r = r'ad(dr)?'
show(r, str)

#(patter)的用法
str = "mood zood tood"
r = r'(f|z)ood'
show(r, str)

#email的匹配
str = "958340585_ASDS@11.com"
r=r'^[\w]+@[a-z0-9]+\.[a-z]+$'
show(r, str)

#手机号码
str = "12345678900"
r = r"^\d{11}$"
show(r, str)

#座机号码xxx-xxxxxxxx 或者xxxx-xxxxxxx
str = "0411-23563230"
r = r"^\d{3,4}-\d{7,8}$"
show(r, str)

#MAC地址
r=r"^([a-f0-9A-F]{2}-){5}[a-f0-9A-F]{2}$"
str = "AA-01-AA-22-56-aa"
show(r, str)


