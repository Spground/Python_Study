import keyword
#基础语法的练习

#字面字符串的级联
str = "this""is""String\n";
#r可以显示自然字符串
str0 = "this""is"r"String\n";
print(str);
print(str0);

#python中的变量不需要声明类型，他没有类型
#6个标准的数据类型Numbers数字 String字符串，List列表，Tuple元组，Sets集合 Dictionaries
#字典

#Numbers数字 包含int float bool complex
aInt = 20;
bFloat = 5.5;
cBool = True;
dComplex = 4 + 3j;
print(type(aInt), type(bFloat), type(cBool), type(dComplex))

#乘法与乘方
a = 2 * 2;
b = 2 ** 3;
print(a, b);

#除法得整 和 得浮点数
#得浮点数
a = 5 / 4;
#得整数
b = 5 // 4;
print(a, b);


#String字符串
#字符串可以用单引号和双引号括起来， 同时使用反斜杠来转义字符，前面接r或者R可以忽略转义
str = '单引号字符串'
str0 = "双引号字符串"
print(str, str0);

str = r"C:\some\name"
print("r忽略转义字符", str)

#字符串的加法和乘法（重复）
str = "a" + "b";
str0 = str * 2;
print(str, str0);

#字符串的索引方式 第一种从左到右即从0开始增加   第二种从右边到左即从-1开始减少
#没有单独的字符类型， 一个字符就是长度为1的字符串

word = "Python"
print(word[0], word[-6]);

#字符串切片 子串clip 下标形式[头下标：尾下标] 范围是前闭后开
word = "ilovepython"
print(word[1:5]);#输出结果是love
print(word[:]);#输出结果是全部
print(word[5:])#从第5到尾部全部
print(word[-10:-6]);#结果是love 公式成立 p + (-n) = length; p为整数表达的索引 n为负数表达的索引

#字符串的值不能改变 即word[0] = 'm';将报错
#word[0] = 'm';








