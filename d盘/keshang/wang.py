# # fsdfa
# # jhghjg
# # gjhjhk
# # kj
# #1由字母，数字，下滑线组成，且不能以数字开头，尽量只在特殊时候将下划线作开头
# #2不跟系统的名字重名
# #3见名知意 ，首字母小写（驼峰原则）
# #4 变量，必须先定义后使用
# print(123+234+123+456)
# n=123+234+123+456
# print(n+123)
# #hjkhjkadhsfjkh
# # khjkhjkhjk
# print(n*123*123)
# #数据：数据类型
# print(type(n))
# #int 整型：十进制，二进制，八进制，十六进制
# #float 小数（浮点数）
# #str 字符串
# print(type(1.1))
# a=12
# b=1.4
# print(a*b)
# print(type('hello'))
# #int
# #操作：使用运算符
# #+ — * ／
# a=10
# b=20
# print( a+b, 10+20)
# print( a / b ,a - b)
# # ** //
# print(3 ** 3)
# print( 3 // 2)
# # // 只取整数部分
# print( 'hello' + '1')
# #str不能和int相加
# print('20' * 20, '华丽的分割线')
# # % 余数 （特例：作为了解，   针对负数）
# print(5 % 2)
# #数据类型
# #str
# #定义：引号（单引号 ，双引号 ，三引号 ，三双引号）
# #区分；其他部分编程语言会认为单引号好代表字符
# #c语言中
# # char c ='c'
# #char * s = 'string'
# s = 'hello'
# s1 = "hello"
# s2 = """hello"""
# #转义字符
# print('\n')
# #原字符串  r R
# print('r\n')
# print('hello', end="2")
# print('正方形边长：4\n 面积： 4* 4')
# #字符串拼接
# #1、使用+，必须是str才可以
# string1 ='hello'
# string = 'wrold'
# name = string1 +string
# print(name)
# name = 'zhangsan '
# age = 10
# lesson = 'python'
# print('我叫张三，今年10岁，学习python')
# print('我叫'+name)
# print('今年'+ str(age)+'岁' )
# print('学习'+lesson)
# print('我叫' + name + '今年' + str(age)+ '岁' + '学习' + lesson  )
# #2、格式化输出 %
# print('我叫%s,今年%d岁 ，学生%s' % (name,age, lesson))
# #3、fromat 推荐使用lesson
# dea ='我叫{} 今年{}，学习{}'. format(name, age, lesson)
# print(dea)
# a = 4
# s = a * 4
# l = a ** 2
# print("正方形的面积{},周长{}". format(s, l))
# #详细使用format
# #【数字；特殊限制】
# #{} 数据依次放入占位地方
# #「数字对应的数据进行填充
# print('w我叫{1},今年{1},学习{1}'. format(name, age, lesson))
# #{: 对齐方式}
# #[:填充>列宽]
# #><左右对齐 ^剧中
# a = 'dfadfafd'
# b = 'dfasdfsfa'
# c = ' dfsfafasfa'
# print('{:*>20},{:#<20},{:#^20}'.format(a, b, c))
# #{:.s数字f}
# print('{:.2f}'.format(1.234566444))
# #思考： 其他数字限定
#
# #二进制 八进制 十进制 十六进制
# print('=' * 30, 'input:')
# #input
# name = input('请输入：')
# print('你输入的名字:', name)
# #备注；
# #1 input输入的数据需要接收
# #2、inout输入的数据类型是str
# #尝试； 输入半径。显示圆面积
# r = int(input('圆的半径：'))
# import math
# s = r ** 2 * math.pi
# l = r * 2 * math.pi
# print('圆的面积为{}，圆的周长{}'.format(s, l))
# #2、输入商品单价和数量，求商品总额
# price = float(input('输入商品单价'))
# number = int(input('输入商品数量'))
#
# print('商品总额：', price *number)
# #思考： input录入多个数据， 并提取使用？？？
# #提示 : tuple , eval() 或者str分割
# print('=' * 22, 'int')
# # int 二进制（0b）、八进制(0o)、十进制、十六进制(0x)
# n = 123
# n1 = 0b101011
# print('{:b}'.format(n))
# print('{:x}'.format(n))
# print('{:o}'.format(n))
# #复合运算符：+= -= *= 、\= 、**=、\\=
#
#
#
# # < > <= >=
# print(1 < 0)
# print(1 >0)
# print(1 <= 0 )
# print(1 == 1)
# print(1 != 0)
# # 数量类型 ： bool （ture ,false）
# #注意： == 不嫩用于浮点数判断
# #练习 ：输入一个整数，判断是否是3的倍数
# n = int(input('输入一个整数：'))
# print(n % 3 == 0)
# #str比较时：按照ascii表进行比较
# # 遇到第一跟不相同的字符时，结束比较
# s = 'aza'
# s1 = 'aba'
# print(s > s1)
# # bool 比较
# print( True + 1)
# print(True >1)
# # 备注：关系运算符，计算后结果为bool类型
# #逻辑运算符 ：and or  not
# #and
# print(1<2 and 5 < 8)
# print(1>2 and 5 < 8)
# print(1<2 and 5 > 8)
# print(1>2 and 5 > 8)
# # 结论 ：逻辑与 运算符；
# # 表达式1 and 表达式 2
# # 一个表达式为false即为false
# # 同时为true即为true
# print(1 < 2 and 'x' > str(1))
# #or : 一个为true 即为true
# print(1<2 or 5 < 8)
# print(1<2 or 5 < 8)
# print(1<2 or 5 < 8)
# print(1<2 or 5 < 8)
# #not
# #单元运算符（单目运算符）
# print(not 1)
# print(not 1 > 2)
# #非0即为true；非空即为true
# #0即为false ；空即为false
# # 输入一个100以内的正整数，查看是否含6
# a = int(input('请输入一个100以内的正整数：'))
# b =  a % 10
# c =  a // 10
# print(b == 6 or c == 6)
# #s成员运算符： in
# print("h" in 'hello')
# print('1' in '12345')
# #了解的运算符：按位运算符
# # & (按位与)
# # |（按位或）
# # ^（按位异或0
# #  >>（左移）
# #  <<（右移）
# # if
# # if之前的语句
# # if 条件判断：
# #     条件判断为真需要执行的语句
# #if之后的语句
# #备注
# #1、冒号是英文输入
# #2、冒号下一行必须缩进 ，如果暂时没想好语句 ，可用pass暂用
# #3、if之后的语句不能缩进
#
# money = int(input('输入一个金额'))
# if money >= 400:
#     money *= 0.85
#     print('实际支付{}元'.format(money))
# else:
#     money *= 0.95
# #注意：else 后面紧跟冒号（没有表达式）
#  #
#     print('实际支付{}元'.format(money))
# h = float(input('输入一个身高（米）'))
#
# if h >= 1.5:
#     print('购买成人票')
# elif h >= 1.2 and h < 1.5:
#     print('购买儿童票')
# else:
#     print("不用买票")
# if money >= 1000:
#     money *= 0.75 -50
#     print('实际支付{}元'.format(money))
# elif money >= 400:
#     money *= 0.85
#     print('实际支付的{}元'.format(money))
# else:
#     money *= 0.95
#
#     print('实际支付{}元'.format(money))
# grade = float(input('输入一个成绩'))
# if 85 <= grade <= 100:
#     print('A')
# elif 70 <= grade <=84:
#     print('B')
# elif 60 <= grade <= 69:
#     print('c')
# else:
#     print('D')
# exit(): 代表文件结束
# 循环
# print("编号1")
# print("编号2")
# print("编号3")
# print("编号4")
# print("编号5")
# print("编号6")
# print("编号7")
# print("编号8")
# print("编号9")
# print("编号10")
# while  : while之前的语句
#           while判定条件
#               条件为真需要执行的语句们（重复性的代码）
#               while之后的语句
# n =  0
# while n < 10:
#     n +=1
#     print("编号{}".format(n))
# print('over')
#注意点：
# 1 、循环增量、循环条件、循环体。
# 2、 冒号， 缩进
# 3、避免死循环
# n = 0
#
# while n < 100:
#     n += 1
#     print('编号', n)
# print('over')
# n = 0
# while n < 100:
#     if n % 2 == 0:
#         print(n)
#     else:
#         pass
#     n += 1
# print('over')
# n = 100
# s = 0
# while n > 0:
#     s = s  + n
#     n -= 1
# print('1到100的和{}'.format(s))
# print('over')
# a = 0
# s = 0
# while a < 10:
#     a += 1
#     n = int(input('请输入成绩'))
#     if n < 0:
#         a -= 1
#     else:
#         s = s + n
# print('{}个成绩的总和{}'.format(a, s))
# print('over')
#tuple(s): 元组：元素的组合
#取得元素，通过索引（下标、角标）
#语法：元组名称【索引】
#索引从0开始
#print（t[8]）indexerror: tuple index out
#注意：当只有一个元素时 ，逗号不能省略
#元组中的元素是不能修改的（不支持）
#下标可以是负数(但注意越界问题)
#【index】
#[start: end: step]
#右开区间（end是取不到）
# a = 0
# s = 0
# t = ('语文', '数学', '英语', '物理', '化学', '生物')
# while a < 6:
#     a += 1
#     n = int(input('请输入{}成绩'.format(t[a])))
#     if n < 0:
#         a -= 1
#     else:
#         s = s + n
# print('{}个成绩的总和{}'.format(a, s))
# print('over')
# 循环
# break： 之后语句不会再进行了，只能影响一个while（终止本层循环，不管该层循环break之后还剩多少语句或次数，都不再执行）

# continue:终止本次循环
#该次之后都语句不再执行，但继续下次循环
# t = (11, 12, 13, 14, 15)
# i = 0
# while i < len(t):
#     if t[i] == 11:
#         print('找到了')
#         break
#         print('i')
#         i += 1
# print('over')
#while - else
# t = (11, 12, 13, 14, 15)
# i = 0
# while i < len(t):
#     if t[i] == 11:
#         print('找到了')
#         break
#         print('i')
#         i += 1
# else:
#     print('找不到')
# print('over')
# count = 0
# while count < 3 :
#     password = int(input('请输入{}次密码'.format(count + 1)))
#     if password == 123456:
#         print('登陆成功')
#         break
#     count +=1
# else:
#     print('登陆不成功')
# print('over')
# for i in 'helleo':
#     print(i)
# t = (11, 22, 33)
# for i  in t:
#     print('i')
# t = (11, 22, 33, 44, 55, 66)
#
# for i in t:
#     if i == 11:
#         print('成功找到')
#         break
# else:
#     print('meizhaod')
# print('over')
#rang() 范围
#range(stop)默认从零开始
#range(start, stop, 【-step】)step默认为1
# for i in range(0, 101):
#     print(i)
# for i in range (-3, 100, 2):
#     print(i)
#tuple : 补充
# t = 11 ,22
# print(t)
# t1 ,t2 = 11, 22
# print(t1, t2)
#双层循环执行次数
#=外层循环次数 * 内层循环次数
# year, month, day = eval(input('输入年，月，日'))
# t = (31, 28, 31, 30, 31, 30, 31, 31,30, 31, 30, 31)
# days = 0
# i = 0
# while i < month - 1:
#     days = days + t[i]
#     i += 1
#     if year % 4 ==0 and year % 100 != 0:
#         if month > 2:
#             days =days + 1
# days = days + day
# print('天数{}'.format(days))


# i = 0
# while i < 6:
#     j = 0
#     while j < 6 - i:
#         print("*", end='')
#         j = j + 1
#     i = i + 1
#     print()
# i = 0
# while i < 6:
#     k = 0
#     while k < i:
#         print(' ', end='')
#         k += 1
#     j = 0
#     while j < 6 - i:
#         print("*", end='')
#         j = j + 1
#     i += 1
#     print()
# i = 0
# while i < 6:
#
#     # 空格
#     k = 0
#     while k < 5 - i:
#         print(' ', end='')
#         k = k + 1
#     # * 号
#     j = 0
#     while j < 1 + i:
#         print('*', end='')
#         j = j + 1
#
#     i = i + 1
#     print()
#
# 函数
# 定义 ： def 函数名（参数列表）：
#               函数体
#注意：
# 1、def 不能省略
# 2、函数命名原则等同与变量命名原则
# 3、参数列表可以唯恐， 称为无参函数， 但（）不能省略。
# 4、冒号，缩进
# 5、函数只有在调用时， 才会执行
# 调用语法
# 函数名（实际参数列表）
#如果参数列表为空 ，（）不能省略，否则不能调用函数
# 形参 ：（形式参数），定义函数时的参数
# 实参 ： （实际参数），调用函数时的参数
# 注意 ：
# 1、形参一般只能是变量， 除非凤娥符（*）
# 2、实参是一个确定的值 ， 可以是表达式、变量 。。。。。。。。
# def qetwater():
#     print('拿钱')
#     print('出门到全市')
#     print('挑水')
#     print('付钱')
#     print('回到教室')
# qetwater()
# print('开开心心敲代码')
# print('。。。。。。')

#
# def qetwater(money):
#     print('拿钱{}'.format(money))
#     print('出门到全市')
#     print('挑水')
#     print('付钱')
#     print('回到教室')
# a = 10
# qetwater(a)
# qetwater(10)
# qetwater(100 + 0.1)

# def daying(n):
#     print('helloworld\n' * n)
#
# daying(5)
# def myorint(n):
#     for i in range(n):
#         print('helloworld')
# myorint(10)
# def qetwater(n, water = '农夫山泉'):
#     print('拿{}钱'.format(n))
#     print('出门到全市')
#     print('挑{}'.format(water))
#     print('付钱')
#     print('回到教室')
#
# qetwater(10, '百事可乐')
# def number(n):
#     a = 0
#     for i in range(n+1):
#         a = i + a
#     print(a)

# number(10)
# number(100)
# number(1000)
# number(50)

# def number(start, stop):
#     a = 0
#     for i in range(start, stop+1):
#        a = i + a
#     print(a)

# 函数体 ： 包涵函数执行的代码即返回值
# 1、如果有返回值， 使用return进行返回
# 2、函数执行过程中， 遇到return, 则函数结束
# 3、当没有值返回， 但也想提前结束函数时， 也可以使用return
# 4、函数中没有return时， 默认在函数结尾存在retur none
# 5、 多值返回时， 使用逗号分隔，默认为tuple类型


# def number(start, stop):
#     a = 0
#     for i in range(start, stop+1):
#        a = i + a
#     return  a
# s = number(1, 50) / 3
# print(s)

# def qetwater(n, water = '农夫山泉'):
#     print('拿{}钱'.format(n))
#     print('出门到全市')
#     print('挑{}'.format(water))
#     print('付钱')
#     print('回到教室')
#     return '一瓶豪华的' + water
# result = qetwater(100)
# print(result)
# import wxl.func
# print(wxl.func.number(5))
# import math as m
# print(m.pi)

# list

# l = list()
# print(l)
# l1 = list('hello word')
# print(l1)
#
# #增加
# l2 = [11, 22, 33, 44]
# l2.append(55)
# print(l2)
# #append只能追加一个元素
# # 当 insert的index大于范围， 默认在末尾
# # index如果是负数，超过范围，这默认放在首位
# l2.insert(0, 55)
# print(l2)
# l2.extend((88, 99))
# print(l2)
# l = list()
# for i in range(10):
#     n = int(input('输入一个数'))
#     l.append(n)
# print(l)
#
# #删除
# l2 = [11, 22, 33, 44, 11, 11, 11, 99, 11]
# i = 0
# while i < len(l2):
#     if 11 == l2[i]:
#         l2.pop(i)
#         i = i - 1
#
#     i = i + 1
#
# print(l2)


#修改
# l2 = [11, 22, 33, 44]
# c = l2.count(11)
# print(l2)
# i = l2 .index(11)
# i = l2.index(1, 11, 3) 范围内不存在 则出现异常
# temp = [11, 22, 33]
# l1 =[temp, 44, 55]
# # 思考1 ：如果将temp【-1】 = 99
# # 请问； l1中是否会把33 也改成99
# # # 请问 ： l2中是否会把33也改成99
# # l2 = l1.copy()
# # print(l1)
# # print(l2)
# import copy
# l3 = copy.deepcopy(l1)
# print(l3)
# #查询
#str
# a = 'hello word'
# # print('a.capitaliza():', a.capitalize())
# print(a.upper())    # 所有字符转化为大写
# print(a.lower())    #所有字符转化为小写
# print(a.swapcase()) #交换转化
# print(a.title())    #单词首字母大写
# 1、首字符会转换成大写，其余字符会转换成小写。
# 2、首字符如果是非字母，首字母不会转换成大写，会转换成小写。
# str.center(width[, fillchar]) 函数：
# 1、如果 width 小于字符串宽度直接返回字符串，不会截断:
# 2、fillchar 默认是空格
# 3、fillchar 只能是单个字符
# str = 'www.baidu.com'
# print('str.center():', str.center(40,'*'))
# print('str.center():', str.center(4, '*'))
# print('str.center():', str.center(40))
# print('str.center():', str.center(40,'!'))
#count: 符号也算元素
# str = 'www.baidu.com'
# print('str.count(o):', str.count('o'))
# print('str.count(o):', str.count('o', 1, 11))
# str = '王宣霖'
# str_1 = str.encode('UTF-8')
# str_2 = str.encode('GBK')
# print(str)
# print('1的编码：', str_1)
# print('2的编码：', str_2)
# print('1的编码：', str_1.decode('UTF-8', 'strict'))
# print('2的编码：', str_2.decode('GBK', 'strict'))
# a = 'hello word'
# print(a.replace('hello', 'hehe'))  #全部替换，没输入替换几次的情况下
#切割
# s = '2019/3/3'
# print(s.split('/', 1))
# l = s.rsplit('/') #从右往左切割
# #合并
# print('-'.join(l))
# 查询
# s ='www.baidu.com'
# print(s.find('b', 0, 11)) #没找到返回-1
# print(s.index('baidu'))
# print(s.startswith('www'))
# print(s.endswith('com'))
#格式
# a = 'hello word'
# print(a.ljust(20, '&'))
# print(a.rjust(20, '&'))
# # strip
# s =' hhhh '
# print(s.strip())
# print(s.rstrip("*"))
# print(s.lstrip('*'))
# 内置函数： print input eavl ord chr sum max min help bin oct
# 思考 ： 向上取整 ，向下取整
# dict
# 思考： namedtupie
#from cllections import nametuple
#1  、字典的定义， 字典是以键值对形式存储的。
#2、键值对必须成对出现（k : value）
#3、键值对之间使用逗号作为分隔， 一个键值对是一个字典中的元素
#4、key不能重复, key尽量是字符串，不能变
# 5、字典通过key取值
# l = [11, 22, 333,444]
# peron = {'name':'wangxuanlin',
#          'age': 30}
#取值
# d = {'one': 1}
# print(d['one'])  # key 不存在时， 产生异常
# print(d.get('one')) # key 不存在时， 返回none
# for x in d :
#     print(x, d[x])
# print(list(d))  # 只能拿到key组成的list
# print(d.keys())
# for key in d.keys():
#     print(key, d[key])
# for value in d.values():
#     print(value)
# student ={'name':'zhangsan', 'age': 10}
# student1 ={'name': 'lisi', 'age': 20}
# student2 ={'name': 'wangwu', 'age':30}
# l =[student, student1, student2]
# #求和
# s = 0
# for i in l :
#     print(i.get('age'))
#     s = s + i.get('age')
# print(s)
# students = []
# s = 0
# while True:
#     print('1、输入学生')
#     print('2、显示所有成绩')
#     print('3、结束')
#     n = int(input('输入数字'))
#     if n == 1:
#         name = input('输入姓名：')
#         age = int(input('输入年龄：'))
#         student ={'name':name, 'age':age}
#         students.append(student)
#     elif n == 2:
#         for i in students:
#             s = s + i.get('age')
#         print(students, s)
#     elif n == 3:
#         break

# d = {'one': 1}
# d['one'] = 2    #当key存在时是修改操作
# d ['three'] = 3     #当key不存在时是添加操作
# print(d)
# scores = [11, 22 ,33, 11, 33, 55, 66, 77]
# scoredic ={'a':[], 'b':[], 'c':[]}
# for score in scores:
#     if score >= 50:
#         scoredic.get('a').append(score)
#     elif score >= 20:
#         scoredic.get('b').append(score)
#     else:
#         scoredic.get('c').append(score)
# print(scoredic)
#数据与函数
# def changenumber(n):
#     # n = 11
#     n[0] = 0
#     print(n)
# x = [10, 20]
# changenumber(x)
# print(x)
# dict其他函数
# 删除
# d = {'one': 1, 'two': 2}
# d.clear()
# for t in d.items():
# 删除
# d.pop('one')
# print(d.popitem())     #当dict为空时，产生异常。
# print(d)
# d.setdefault('two', 2)      # key不存在时添加
# print(d)
# def saveinfo(**kwargs):
#     print(kwargs)
# saveinfo(name = 'zhangsan', age = 10)
# studic = {'one': 1}
# saveinfo(**studic)
# def func1(a, b, c, d):
#     fnunci = [11, 22, 33, 44]
# # 查询
# print(11 in d)
# # 新增遍历方式
# l =[11, 22, 33]
# for i , v in enumerate(l):
#     print(i, v)
# def showmen():
#     print('1、添加成员:')
#     print('2、根据成员编号查询成员信息:')     #函数名记录着函数的地址
#     print('3、根据成员编号修改成员信息:')      #用一个变量来记录这个函数名
#     print('4、移除某个成员')                   #则也可以通过这个变量来调用该函数
#     print('5、查看所有成员')
#     print('6、退出')
#     menu = int(input('请选择:'))
#     return menu
# a = showmen()
# a()
# def funci():
#     money = 100
#     def getmoney():
#         nonlocal money
#         money = 20
#         print(money)
#     def save():
#         global  money
#         money = money + 1000
#         print(money)
#     return getmoney, save #返回的是元组 ,函数是可以嵌套函数的，函数用return返回。
#
#
# print(money)
# print(money)
# lambda : 匿名函数
# lambda 参数：返回值
# map
# l =[10, 20, 30, 40, 50, 60]
# result = map(lambda x : str(x), l)
# print(l)
# print(result)
# print(list(result))
# filter
# l = [1, 2, 1, 3, 5, 2]
# print(list(filter(lambda x: l.count(x) == 1, l )))
# import time
# def timeit(fn, *args, **kwargs):
#     start = time .time()
#     ret = fn(*args, **kwargs)
#     print(time.time() -start)
#     return ret
# def sleep(n):
#     time.sleep(n)
# timeit(sleep, 3)
# import time
# def timeit(fn):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         ret = fn(*args, **kwargs)
#         stop = time.time()
#         print(stop - start)
#         return ret
#     return wrapper
# @timeit
# def sleep(n):
#     time.sleep(n)
# # sleep = timeit(sleep)
# sleep(3)
# class 类 ：泛指一切具有相同属性的事物
# 对象： 类的具体化
# python : 多继承
'''class 类名
        类别（包涵数据和函数）
 注意：
1、类名 书写同变量名书写方式， 但首字母大写
            '''
# 新式类、 经典类
# class person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def eating(self):
#         print('{}吃饭'.format(self.name))
#         self.shangwang()
#     def shangwang(self):
#         print('上网')
#
# zhangsan = person('zhangsan', 10, '男')
# zhangsan.eating()
# print(zhangsan)
# lisi = person('lisi', 12, '男')
# print(lisi)
# luyis = person('露易丝', 12, '女' )
# print(luyis)
# class Teacher:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def Like(self, like):
#         print('{}喜欢:'.format(self.name), like)
#     def Someonelike(self):
#         print("{}喜欢打代码".format(self.name))
# teacher = Teacher('lisi', 30)
# teacher.Like('打代码')
# class Teacher:
#     def __init__(self, name, age, teach):
#         self.name = name
#         self.age = age
#         self.teach =teach
#     def dianming(self, Students):
#         print('点名：')
#         n = input('姓名')
#         hasattr(Students, self.name)
#         Students.Jieshao()
# class Students:
#     def __init__(self, name, age, xingbie, number):
#         self.name = name
#         self.age = age
#         self.xingbie = xingbie
#         self.number = number
#     def Jieshao(self):
#         student = {'姓名': self.name,'年龄': self.age, '性别': self.xingbie,'电话': self.number}
#         print(student)
# studnt = Students('王五', 10, '男', 1222)
# # studnt.Jieshao()
# # teacher =Teacher('lisi', 30, '书写')
# # teacher.dianming()
# company = {
#     'name': 'rimi',
#     'teachers': {'测试': ['李老师', '江老师'],
#                  'Python': ['胡老师'],
#                  'Java': ['程老师', '张老师']},
#     'students': {
#         'Python': {'P1901': ['张三', '李四'],
#                    'P1902': ['王老五']},
#         '测试': {'C1901': ['老赵']}
#     },
#     'address': '成都'}
# teachers = company['students']
# for k in teachers:
#     for a in teachers[k]:
#         for i in teachers[k][a]: #for in 只能拿到key， 不能拿到key值
#             print(i)

from collections import namedtuple
# t = [11, 22, 33, 44, 55, 66, 77, 88]
# print(t[3: 8: 4])
# print(t[::7])
# d = {'a': ['ada', 'ab'], 'z': ['zhang', 'zhang'], 'l': ['li', 'ji']}
# l = []
# # print(list(d.values()))
# # for i in d:
# #     for k in d[i]:
# #         l.append(k)
# # print(l)
# # for index, key in enumerate(d):
# #     print(index, key)
# from collections import OrderedDict
# d = OrderedDict()
#
# '''场景
# 创建一个狗类，具有体重，年龄， 颜色， 呢称等属性
# 可以进食、行走、 看门等动作
# 创建一个羊类， 具有身长、体重、年龄、颜色等属性，
# 可以进食、行走等动作'''
# class Animal:
#     def __init__(self, age, weight, color):
#         self.age = age
#         self.weight = weight
#         self.color = color
#
#     def eating(self):
#         print('进食')
#
#     def xingzou(self):
#         print('行走')
# class Dog(Animal):
#     def __init__(self, name, age, color, li, weight):
#         self.name = name
#         self.li = li
#         super().__init__(weight, age, color)
#     def kanmen(self):
#         print('看门')
# class Sheep(Animal):
#     def __init__(self, height, weight, age, color):
#         self.height = height
#         super().__init__(weight, color, age)
# sheep = Sheep(100, 50, 1, '白')
# print(sheep)
# '''场景2：
# 创建一个老师类，姓名、身份证号、地址、授课内容
# 老师可以授课、吃饭
# 创建一个工程师类，姓名、身份证号、 地址、 开发语言
# 工程师可以做研发、 吃饭'''
# class People:
#     def __init__(self, name, card, address):
#         self.name = name
#         self.card = card
#         self.address = address
#
#     def eating(self):
#         print('吃饭')
#
#
# class Teacher(People):
#     def __init__(self, name, card, address, teach='a'):
#         self.teach = teach
#         super().__init__(name, card, address)
#
#     def teach1(self):
#         print('授{}的课'.format(self.teach))
#
#
#
# class Programmer(People):
#     def __init__(self, name, card, address, exploit='python'):
#         self.exploit = exploit
#         super().__init__(name, card, address)
#
#     def yanjiu(self):
#         print('用{}研究'.format(self.exploit))
# teacher = Teacher('lisi', 1222222, 123333, 'python')
# teacher.eating()
# teacher.teach1()

#
# class Free(Teacher, Programmer):
#     pass
#
#
# free = Free('自由人', 1222222, 12222, 'python')
# print(Free.mro())   #'能拿到多级层的数据连'
# class People:
#     def __init__(self, name, card, address):
#         self.name = name
#         self.card = card
#         self.address = address
#
#     def eating(self):
#         print('吃饭')
#
#
# class Teacher(People):
#     def __init__(self, name, card, address, **kwargs):
#         self.teach = kwargs.get('teach')
#         super().__init__(name, card, address)
#
#     def teach1(self):
#         print('授{}的课'.format(self.teach))
#
#
#
# class Programmer(People):
#     def __init__(self, name, card, address, **kwargs):
#         self.exploit = kwargs.get('exploit')
#         super().__init__(name, card, address)
#
#     def yanjiu(self):
#         print('用{}研究'.format(self.exploit))
# teacher = Teacher('lisi', 1222222, 123333, teach = 'a')
# teacher.eating()
#
#
# class Free(Teacher, Programmer):
#     pass
#
#
# free = Free('自由人', 1222222, 12222, exploit = 'c')

# import time
# # 装饰器
#
# def func1(temp):
#     def func2():
#         t1 = time.time()
#         temp()
#         t2 = time.time()
#         print(t2 - t1)
#     return func2
#
# @func1  # saying = func1(saying)
# def saying():
#     print('saying')
#
# # saying = func1(saying)
# saying()
# def caltime(flag):
#     def func1(temp):
#         def func2(*args, **kwargs):
#            t1 = time.time()
#            r = temp(*args, **kwargs)
#            t2 = time.time()
#            if flag == True:
#                 print(t2 - t1)
#            else:
#                 print('😊', t2 - t1)
#                 return r
#
#         return func2
#     return func1
#
# @caltime(flag=True)  # saying = caltime(saying)
# def saying():
#     print('saying')
#
# @caltime(flag=False)
# def myabs(n):
#     if n < 0:
#         return -n
#     return n
#
# # saying = func1(saying)
# # saying()
# print(myabs(-1))
# '''
# public: 公开的
# protecte ：受保护的
# private: 私有的
# '''
#
#
# class Good:
#     def __init__(self, price):
#         self._price = 0  # 新增一个_price的字段
#         self.price = price
#
#     @property
#     def price(self):
#         return self._price
#
#     @price.setter
#     def price(self, price):
#         if price < 0:
#             price = 0
#
#         self._price = price
#
#     def des(self):
#         print('描述')
#
#     def __str__(self):
#         return str(self.price)
#
#
# good1 = Good(100)
# good1.price = 1000
# print(good1.price)
#
# print(dir(Good))
# print(dir(good1))


#类限制
# class Person:
#     __slots__ = ['name', 'age', 'dog']
#
#     def __init__(self, name, age, dog):
#         self.name = name
#         self.age = age
#         self.dog = dog
#
#     def ying(self):
#         print('gou')
#
#     def cat(self):
#         print('mao')
#
#
# han = Person('zhangsan', 10, 3)
# han.ying()
# han.cat()
#类属性



# 生成器，

#
#生成式
# l = (x for x in range(1, 100) if x % 2 == 0)
# print(l)
# print(next(l))
# print(next(l))
# for i in range(10):
#     print(next(l)
# class Myclass:
#     def __init__(self):
#         self.number = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.number += 1
#         print(self.number)
#         if self.number == 10:
#             raise  StopIteration



# a = Myclass()

# next(a)

# re.py

# import re
# string = input('输入')
# p = 'a'
# print(re.match(p, string))

# f = open('')
# print(f.read())
# f.close()
#
#
# 异常处理

# try:
#     n = int(input('输入数字'))
#     print(10 / n)
#
# except ValueError as e:
#     print('ValueError', e)
#
# except ZeroDivisionError:
#     print('除数为零')
#
# else:  #无异常执行的语句
#     print(n)
#
# finally:  #不管异常是否产生， 都会执行语句
#     print('over')


# 断言
# assert 1 < 2
#
#
#
import xlrd, xlwt


#读取：

# book = xlrd.open_workbook('/Users/admin/Desktop/studentsbooks.xlsx')
# # 如果excel表跟当前py文件同目录，则不需要书写路径
# # 直接输入文件名就可以类
# book1 = book.sheet_by_index(0)
# # book2 = book.sheet_by_name('sheet名称')
# # book1names = book.sheet_names()
#
# #第三步， 得到整行、或者整列、 或者一个cell的数据
#
# print(book1.row(0))
# print(book1.row_values(0))
# print(book1.row_types(0))
#
# # 得到行数
# print(book1.nrows)
# 得到列数
# print(book1.ncols)
#
#
# #新建:
#
# # 第一步新建excle表
#
# newbook = xlwt.Workbook
# #新建工作表
#
#
# newsheet = newbook.add_sheet('学生表')
#
# # 写入内容
#
# newsheet.write(0,0 , 'helloworld')
#
# # 保存内容
#
# newsheet.save('学生通讯录.xls')


#冒泡排序：
#
##趟数= 个数 - 1

#

i = 0
d = [66, 55, 44, 11, 33, 22]
while i < len(d) - 1:
    j = 0
    while j < len(d) - i - 1:
        if d[j] < d[j + 1]:
            d[j], d[j + 1] = d[j + 1], d[j]
        j = j + 1
    i = i + 1


print(d)






