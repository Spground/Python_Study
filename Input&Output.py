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
