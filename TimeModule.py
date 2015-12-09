#Time Module
import time;

#tick时间间隔是以秒为单位的浮点小数，每一个时间戳都是从1970年1月1日午夜
#流失了多少时间
ticks = time.time();#

print("Number of ticks since 12:00 am, January 1, 1970: ", ticks);

#时间元组Python函数有一个元组装起来的9组数字处理时间
localtime = time.localtime(time.time());
print("Local time is : ", localtime);
print(type(localtime));
print(localtime.tm_year);

#格式化输出
localtime = time.asctime(time.localtime(time.time()));
print("Local current time is ", localtime);

#获取某月的日历
import calendar

cal = calendar.month(2015, 12);
print(cal);
