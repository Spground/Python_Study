import keyword
#******************************基础语法的练习***********************************

#字面字符串的级联
str = "this""is""String\n";
#r可以显示自然字符串
str0 = "this""is"r"String\n";
print(str);
print(str0);

#python中的变量不需要声明类型，他没有类型
#6个标准的数据类型Numbers数字 String字符串，List列表，Tuple元组，Sets集合 Dictionaries
#字典

#-------------------------------Numbers数字----------------------------------------
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
#-------------------------------Numbers数字-------------------------------------


#-------------------------------String字符串------------------------------------
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
#-------------------------------String字符串-------------------------------------


#---------------------------------List列表--------------------------------------
#List列表是Python中使用最频繁的数据类型
a = ['him', 25, 100, 'her'];
print(a);

#和字符串一样，列表是可以被索引和切片的，但是和字符串不一样的是列表中的的元素是可以改变的
a = [1, 2, 3, 4, 5];
a = a + [6, 7, 8];
print("a List supports add operation :", a);
a[0] = 9;
print("a List supports modified a given index element once operation :", a);
a[0] = 1;
a[6:8] = [];#delete element
a[0:1] = [0];
a[5] = [];
print("a List supports modified many given index element once operation :", a);
#---------------------------------List列表--------------------------------------


#---------------------------------Tuple元组------------------------------------
#元组与列表类似，不同之处在于元组的元素不能修改，元组写在小括号里面，元素之间用逗号隔开
#元素类型也可以不相同

a = (1994, 2015, "mis", 'cs');
print(a, type(a), len(a));

#同字符串类似，可以被索引，也可以被切片，字符串可以被看做是一个特殊的元组，且元组的元素
#也是不可以改变的
#a[0] = 1; error
a = ();#空元组
print("Empty tuple", a);
a = (20);#包含一个元素的元组
a = (20,);
print(a);

#元组的加操作
a, b = (1, 2, "aEnd"), (3, 4, "bEnd");
c = a + b;
print(c);

#string list 和 tuple属于sequence
#-------------------------------Tuple元组--------------------------------------------------

#--------------------------------Sets集合 --------------------------------------
#Feature:无序且不重复
#基本功能是进行成员关系测试和消除重复元素
#可以使用大括号或者set函数创建集合，但是注意创建一个空集合必须使用set()而不是{}
#因为{}是被用来创建一个空字典

#空集合的创建测试
empty = {};
print("we can use {} to create a empty set?", type(empty));#类型显示dict而非set
empty = set();
print("we can use set() to create a empty set?", type(empty));#类型显示set

student = {'Tom', 'Michel', "Lincon", "Tom"};
print("Duplicate student will be removed", student);
#判断一个元素是否在集合中
print("Tom is in student?", 'Green' in student);

#集合运算 并差交补
a = set('TomGreen');#the "TomGreen" will be splited into single letter
print(a);
b = set('TomDanny');

print("a - b is", a - b);#差
print("a | b is", a | b);#并
print("a & b is", a & b);#交
print("a ^ b is", a ^ b);#不同同时存在a b集合的元素 交集的补集
#--------------------------------Sets集合 --------------------------------------


#--------------------------------Dictionaries字典 --------------------------------------
#字典是非常有用的一种内置数据类型
#字典是一种映射类型，他是一个无序的键值对集合
#关键字必须是不可变类型也就是说list和包含可变类型的tuple不能做关键字
#在同一个字典中，关键字还必须互不相同

#创建空字典
empty = {};
tel = {'Jack':132, 'Tom':151, "Michel":110};
print(tel);
del tel['Jack'];
tel['Jimmy'] = 150;
print(tel);
print(tel['Tom']);
print("tel's unordered keys list is", list(tel.keys()));
print("tel's sorted keys list is", sorted(list(tel.keys())));#要对keys排序要保证keys的数据类型都一一样，不然会出错

#dict创建字典
tel = dict([('Tom', 110),("Green", 123)]);
print(tel);

tel = {x : x * 2 for x in {2,3,'352'}};#不知道这是什么鬼写法
print(tel);

tel = dict(Tom=110, Green=120);
print(tel);
#--------------------------------Dictionaries字典 ------------------------------
#总结[] list, () tuple, {} set, {} dict

#-----------------------------------Python注释-------------------------------------
#这是一个注释
print("Hello, World!");

'''
这是多行注释
这是多行注释
'''
"""
这也是多行注释
这也是多行注释
"""






