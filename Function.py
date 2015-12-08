#Python函数学习
#----------------------------------------------------------------------------
#不带return相当于返回None

def printMe( str ):
        print(str);
        return;

#函数调用  
printMe("Hello, Python!");

#-------------------------------引用传递-----------------------------------------------
#所有参数在python中都是按照引用传递，如果在函数中修改了参数
#那么原来的参数也改变了

def changeList( myList ):
        myList.append(5);
        print("函数内myList is ", myList);
        return;

mList = [1, 2, 3, 4];
print("调用函数前 mList is ", mList);
changeList(mList);
print("调用函数后 mList is ", mList);

#-------------------------------参数---------------------------------------------
#正式参数的类型：必备参数、命名参数、缺省参数、不定长参数

#必备参数省略

#命名参数和函数调用密切相关，可以跳过传入的参数或者乱序传入
def printName( name = "undefined", age = "-1"):
        print(name, age, end="  ");
        return;

printName(age = 23, name = "Tom");#乱序传入

printName();#省略参数

printName(name = "Tom");

#不定长的参数
def printInfo(string, *vartuple):
        print("The first param is ", string, "\n");
        for var in vartuple:
                print(var);
        return;

printInfo("Good");
printInfo("Good", "Bad", "Ted", "Breed");


#匿名函数
#lamda [arg1 [, arg2, ....]]:expression

add = lambda x, y : x + y;
print("5 + 3 is ", add(5, 3));

#变量和局部变量
#定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
#局部变量只能在其被声明的函数内部访问，
#而全局变量可以在整个程序范围内访问。调用函数时，
#所有在函数内声明的变量名称都将被加入到作用域中





