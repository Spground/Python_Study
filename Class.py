#python的类继承机制是多继承
#子类可以覆盖基类中的方法

#类对象支持两种操作，属性引用 和 实例化

class Complex:
        def __init__(self, real, imag):
                self.r = real;
                self.i = imag;

#__init__构造方法

x= Complex(3, 2.5);
print("The type of x", type(x));
print("x is ", x.r, x.i);

#类的方法 使用def关键字定义个方法 与一般函数不一样
#类方法必须包含参数self,且为第一个参数
class people:
        #定义基本属性
        name = "";
        age = 0;
        #定义私有属性
        __weight = 0;

        def __init__(self, n, a, w):
                self.name = n;
                self.age = a;
                self.__weight = w;

        def speak(self):
                print("{0} is speaking: i am {1} years old".format(self.name, self.age));

p = people('Tom', 10, 30);
p.speak();

#------------------------继承--------------------------
#class ChildName(BaseName):
#若是基类中有相同的方法名，而在子类使用的时候没有指定 从左到右去搜索，即先搜索子类

class student(people):
        grade = "";
        def __init__(self, n, a, w, g):
                #调用父类的构造方法
                people.__init__(self, n, a, w);
                self.grade = g;

        #覆写父类的方法
        def speak(self):
                print("{0} is speaking: i am {1} years old， and i am in grade {2}".format(self.name, self.age, self.grade));
s = student('ken', 20, 60, 3);
s.speak();

#从左到右搜索方法
class Father1:
        def f(self):
                print("I am f() in Father1");

class Father2:
        def f(self):
                print("I am f() in Father2");

class Child(Father1, Father2):
        pass;

c = Child();
c.f();

#类属性和方法
#私有属性 俩下划线开头 __a, 不能再类外部使用或被直接访问 ，在内部使用时，self.a
#类的私有方法 __fname()， 不能在类的外部调用 在类的内部使用self.fname();
#类的专有方法：
#__init__()构造函数
#__del__析构函数
#__repr__打印，类似于toString()
#__len__获得长度
#__add__ __sub__ __mul__ __div__ __mod__ __pow__
#__cmp__ 比较
#__call__函数调用

#--------------------------python的oo细节--------------------------


