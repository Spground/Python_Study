
while 0:
    try:
        x = int(input('please enter a number:'));
    except ValueError:
        print("Oops! That was no valid number. Try again!");


#一个try可能对应多个except子句 同时一个except语句可以包含多个不同的特定的异常

import sys

try:
    f = open("mmm.txt");
    s = f.readline();
    i = int(s.strip());
except OSError as err:
    print("OS Error: {0}".format(err));
except ValueError:
    print("Could not convert data to integer");
except:
    print("Unexpected error:", sys.exc_info()[0]);
    raise;

try:
    f = open("f.txt");
    s = f.readline();
    i = int(s.strip());
except (OSError, ValueError) as err:#except可以处理多个异常同时，使用元组
    print("OS Error: {0}".format(err));
except:
    print("Unexpected error:", sys.exc_info()[0]);
    raise;

#raise语句抛出异常
#raise NameError('Hi There');

#使用raise将异常再次抛出
try:
    raise NameError('Hi There')
except NameError:
    print("An exception flew by!");
    #raise;

#用户自定义异常 必须直接或者间接继承自Exception
class MyError(Exception):
    def __init__(self, value):
        self.value = value;
    def __str__(self):
        return repr(self.value);

try:
    raise MyError(2*2)
except MyError as e:
    print("My Exception occurred value:", e.value);

#raise MyError("oops");

#finally字句
#try:
    #raise KeyboardInterrupt
#finally:
    #print("Goodbye, world!");

#预定义的清理行为 with关键字
#一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要了
#那么这个标准的清理行为就会被执行

for line in open('f.txt'):
    print(line, end='');#文件打开后，没有被关闭

with open("f.txt") as f:
    for line in f:
        print(line, end='');#with语句可以保证对象在使用完成以后
        #一定正确的执行清理的方法，就选中途出现问题
