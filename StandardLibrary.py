#Python标准库概览
#操作系统接口
import os
cwd = os.getcwd();
print("Current work directory is ", cwd);

#shutil模块
import shutil
shutil.copyfile("f.txt", "b.txt");#复制文件
shutil.move("b.txt", "C:\\Users\\asus\\git\\Python_Study\\temp\\b.txt");

#文件通配符
#glob模块提供一个函数用于从目录通配符搜索中生成文件列表
import glob
print(glob.glob("*.py"));

#命令行参数
import sys
print(sys.argv);

#正则表达式
import re
result = re.findall(r"\bf[a-z]*", "which foot or hand fell fasttest");
print(result);

str = "i am too tired";
print(str.replace('too', 'to'));
