total = "item_one" + \
        ";item_two" + \
        ";item_three"
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
word = 'word'
setence = "这是个句子"
paragraph = """三个引号表示
一个句子"""
csdn = '''代码注释区
这里是第一行代码'''
print(total)
print(days)
print(word)
print(setence)
print(paragraph)
print(csdn)
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
print(counter)
print(miles)
print("name:"+name)
print("name:"+"name"[1:3])

tuple = ( 'xiaodong', 'xiaoyin' , 'xiaogang', 'xiaojie')
print(tuple[1:3])


dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
print(dict['one'])
print(dict[2])
print(9/2)
print(9//2)
print(2**8)
print(9%2)

if(True and False):
    print("true")
else:
    print("false")

if(True or False):
    print("true")
else:
    print("false")

if(not False):
    print("true")
else:
    print("false")

str1 ="we are friend"
str2 = str1
str3 ="we are friend"
str4 = str1[:]
print("str1:"+str1)
print("str2:"+str2)
print("str3:"+str3)
print("str4:"+str4)
print(str1==str2);print(str1 is str2)
print(str1==str3);print(str1 is str3)
print(str4 is str1)

a = ('name','phone')
b = a
print(a)
print(b)

print(b is a )
print(b == a )

b = a[:]
print(b is a )
print(b == a )

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print( (a + b) * c / d)

if(1==2):
    print("1==2")
elif(1==3):
    print("1==3")
elif(1==1):
    print("1==1")

if(1==2):
    print("1==2")
else:
    print("1==1")

if(1==1):print("oh my god")

count = 0
while(count<9):
    print("count:",count)
    count = count +1

print("退出循环")

#for循环遍历
for r in 'restaurant':
    print(r)

#通过索引序列迭代
books =['鲁滨逊漂流记','基督山伯爵','雪国']
for b in range(len(books)):
    print(books[b])

for num in range(2,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         print(num,'等于',i,'*',j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print( num, '是一个质数')

#break
print('break测试：')
n = 10
while n>0:
    print('n1:',n)
    if n==5:
        break
    n=n-1

#continue
print('continue测试：')
n = 10
while n>0:
    n = n - 1
    if n==5:
        continue
    print('n1:',n)
import math
#数学参数
print('数学参数：')
car =(10,11,9)
print('max(10,11,9):',max(car))

print('pi:',math.pi)

#字符串格式化 %s 格式化字符串  %d 格式化整数
print ("My name is %s and weight is %d kg!" % ('Zara', 21))

errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print(errHTML)

import time

#获取当前时间
localtime = time.localtime(time.time())

print("本地时间为 :", localtime)