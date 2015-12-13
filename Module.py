#Module in Python
#把定义放在文件中，为了一些脚本或者交互式的解释器实例使用，这个文件被称为模块
#模块是一个包含你自定义的函数和变量的文件，后缀名是.py
import sys
print("command line args is :");
for i in sys.argv:
        print(i);

print("Python path is ", sys.path);

import fibo

fibo.fib(100);#fib(100) will lead to an error, using mudule name prefix
print(fibo.fib2(100));

#module name ===> fibo.__name__
print("fibo module name is ", fibo.__name__);

#if you use a module frequently, just assign a variable intead of fibo.fib
wtf = fibo.fib2;
print("wtf(100) is :", wtf(100));

#模块除了方法定义以外可以包括可执行的代码，这些代码一般用来初始化这个模块
#这些代码在第一次导入时才会被执行，每一个模块都有各自独立的符号表，在模块内部为所有的函数当做全局
#符号表来使用

from fibo import fib, fib2#这种方式把所有的名字都导入进来
print("from fibo import fib, fib2");
fib(100);

#__name__属性
if __name__ == "__main__":
        print("Module程序自身在运行")
else:
        print("Module程序在另一模块中运行")

#dir(modulename)
print("all defined variable in fibo module is ", dir(fibo));
#print("all defined variable in fibo module is\n", dir(sys));

#dir()
print("dir() will return all defined variable including imported module : ", dir());

a = 5;
print("deinfed a :", dir());
del a
print("delete a :", dir());

#---------------------------------package---------------------------------------
#导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，那么
#在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
#引入cn/edu/dlut/echo.py
from cn.edu.dlut import *
echo.echome("dlut");


