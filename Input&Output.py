#I/O
#python中两种输出值的方式：表达式语句 和 print()函数， 第三种是使用文件对象的write()
#函数，标准输出文件可以使用sys.stdout引用
s = "Hello, World";
print(str(s));
print(repr(s));#打印出来有单引号 'Hello, World'

#repr()可以不转义特殊字符,原样输出
hello = "Hello\n";
print(hello);
print(r"Hello\n");
print(repr(hello));

#repr()参数可以使任何对象
print(repr(('1', "2", (1, 2))));

#两种方式打印出平方立方表
#第一种方式
for x in range(1, 11):
        print(repr(x).rjust(2), repr(x*x).rjust(3), end=" ");
        print(repr(x*x*x).rjust(4));

#第二种方式

for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x));

#rjust() ljust() zfill()用法

print("abcdef".rjust(10));
print("abcdef".ljust(10));
print("abcdef".center(10));
print("abcdef".zfill(10));
print(str(5).zfill(10));

#format格式化输出
print("{0:03d}".format(2));
print("{0:03d}".format(20));
print("{0:03d}".format(123));
print("{0:0f}".format(2.2));

formatStr = "{0:2d} {1:2f} {2:2s}";
print(formatStr.format(10, 20, "200"));

print("{} and {}".format("I", "you"));

#format指定关键字参数
print("This is {food} and {fruit}".format(food = "milk", fruit = "apple"));
print("Hello, Welcome {1}, {middle}, {0}".format("Tom", "Georg", middle="Tony"));

import math
print("PI is {0:.3f}".format(math.pi));

#在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
        print("{0:10} ===> {1:10d}".format(name, phone));
#旧式格式化字符串
print("PI is %.3f"%math.pi);

#文件
#读写文件
#opne()将返回一个file对象 open(filename, mode)
f = open("f.txt", 'r+');
str = f.read();#read all content, read(size)
print("The content of the file is :", str);

#move file pointer to start
f.seek(0);
str = f.read(2);
print("The first 2 byte is :", str);

f.seek(0);
str = f.readline();
print("The first line is :", str);

#wirte
count = f.write("\n3.Hello, DUT!\n");
print("The count of char wrote is ", count);
f.close();

#seek(offset, from_what) from_what 0开头位置 1当前位置  2结尾位置

#-----------------------pickle模块----------------------------
#python的pickle模块实现了基本的数据序列和反序列化
#通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中，永久存储
#反之亦然
#基本接口 pickle.dump(obj, file, [, protocol])


#使用pickle模块将数据对象保存到文件
import pickle
obj = {'a':[1, 2.0, 3, 4+6j],
        'b':("string", u"Unicode string"),
       'c':None
       };
print(type(obj));

output = open('obj.pkl', 'wb');
pickle.dump(obj, output);
output.close();

#反序列化
pkl_file = open("obj.pkl", "rb");
aobj = pickle.load(pkl_file);
print("The type of loading obj is :", type(aobj));
print(aobj);
















