#python面向对象
#类
#类变量：类变量是在整个实例化的对象中是公用的，类变量定义在类中且在函数体外
#类变量通常不作为实例变量使用

#数据成员：类变量或者实例变量用于处理类及其实例对象相关的数据

#方法重写：

#实例变量：定义在方法中变量

#继承

#实例化

#方法

#对象：通过类定义的数据结构实例，对象包括两个数据成员（类变量和实例变量）和方法

class Student:
        '所有学生的基类'
        sCount = 0#类变量，类似于java的静态变量，属于整个类的，而非实例的

        def __init__(self, name='undefined', age=0):
                self.name = name#实例变量
                self.age = age
                Student.sCount += 1

        def displayStudentCount(self):
                print("The total count of student is ", Student.sCount)

        def displayStudent(self):
                print("Name: {0}, Age: {1}".format(self.name, self.age))

        def __del__(self):
                print("I am destroying...")

s = Student('Tom', 22)
print(Student.sCount)
#print(Student.age) 类Student没有age这一类属性
print("Instance's attr age is ", s.age)

s.displayStudentCount()
s.displayStudent()

#属性访问
print("Instance's attr can be accessed by obj.attr :", s.age, s.name)

#删除属性后再增加属性
del s.age
s.age = 10
s.displayStudent()

#使用函数方式访问属性
#getattr(obj, name[, default])
#hasattr(obj, name)
#setattr(obj, name, value)
#delattr(obj, name)

print(hasattr(s, 'age'))
print(getattr(s, 'age', 0))

#python内置属性
#—__dict__：类的属性 包含一个字典 由类的数据属性组成
#__doc__：类的文档字符串
#__name__：类名
#__module__：类定义所在的模块
#__bases__:类的所有父类构成元素，包含一个由所有父类组成的元组

print("__doc__", Student.__doc__)
print("__dict__", Student.__dict__)
print("__module__", Student.__module__)
print("__bases__", Student.__bases__)

#python的gc, 引用计数器来跟踪使用中的对象有多少引用

s = Student()
s1 = s
s2 = s

print(id(s), id(s1), id(s2))
del s
del s1
del s2
#删除所有的对象引用后，对象被gc回收，__del__被调用


#类的继承注意事项

class Father:
        sFather = 1000
        def __init__(self):
                print("I am in father's constructor")

        def f(self):
                print("I am in f()")

        def fun(self):
                print("it's so fun, ---father")

class Son(Father):
        def __init__(self):#子类的构造函数不会显示的调用父类的构造函数
                print("sFather is ", Father.sFather)
                Father.__init__(self)#显示调用父类的方法
                print("I am in son's constructor")

        def fun(self):
                Father.fun(self)#调用父类方法
                print("is's so fun, ---son")

son = Son()
son.f()
son.fun()

print("Son is subclass of Father? ", issubclass(Son, Father))
print("son instance is a instance of Son or it's superclass?", isinstance(son, Son))
print("son instance is a instance of Son or it's superclass?", isinstance(son, Father))

#基础的重载方法
#__init__(self) __str__(self) __del__(self) __repr__(self) __cmp__(self)

#类属性和方法
#类的私有属性
#__private_attr, 不能在类外部被使用或者直接访问， 在类内部使用self.__private_attr访问


#类方法与对象方法与静态方法
class Demo:
        __secretCount = 0
        publicCount = 12

        def __init__(self):
                pass
        
        def instanceFunc0(self):
                print("static private global var can be accessed by ClassName.__varName or self.__varName", Demo.__secretCount, self.__secretCount)
                print("I am in public instance Func")
        def instanceFunc1(self):#public实例方法
                self.instanceFunc0()#在实例方法中访问公共实力方法
                self.__privateInstanceFunc()#在实例方法中访问私有的实例方法
                Demo.__staticFunc()#在实例方法中访问私有类方法
                Demo.staticFunc()#在实例方法中访问公共类方法
                pass
        def __privateInstanceFunc(self):#私有的实例方法
                print("I am in private instance Func")
                pass

        
        def staticFunc():#public function 
                print("i am public static Func")
                pass
        def __staticFunc():#private function
                print("i am private static Func")
                pass

        #static method
        @staticmethod
        def publicStaticMethod():
                print("i am publicStaticMethod")
                pass
        @staticmethod
        def __privateStaticMethod():
                print("i am in __privateStaticMethod")
                pass

        #class method
        @classmethod
        def publicClassMethod(cls):
                print(cls)
                pass
        
         
#静态方法
Demo.publicStaticMethod()
#Demo.__privateStaticMethod() 私有的静态方法访问不了

#类方法
Demo.publicClassMethod()

#对象方法
d = Demo()
d.instanceFunc1()

print(Demo.__dict__)

#太混乱了 没搞明白




