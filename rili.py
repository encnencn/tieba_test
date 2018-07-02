import calendar

import datetime

cal = calendar.month(2018, 7)

print("以下输出2018年7月份的日历:")

print(cal)

i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)

# 打开一个文件
fo = open("foo.txt", "w")
fo.write("www.runoob.com!\nVery good site!\n")

# 关闭打开的文件
fo.close()

#读取文件
fo = open("foo.txt", "r+")
str = fo.read(20)
print ("读取的字符串是 : ", str)
# 关闭打开的文件
fo.close()

import os
#获取文件目录
print(os.getcwd())
os.remove("foo.txt")


document = open("testfile.txt", "w+");
print ("文件名: ", document.name)
document.write("这是我创建的第一个测试文件！\nwelcome!");
print (document.tell());
#输出当前指针位置
document.seek(os.SEEK_SET);
#设置指针回到文件最初
context = document.read();
print (context);
document.close();