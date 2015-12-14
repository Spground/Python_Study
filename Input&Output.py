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
