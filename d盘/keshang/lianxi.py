# print(123 + 1234 + 12345 + 12345)
# a = int(input('长方形的长：'))
# b = int(input('长方形的宽：'))
# s =  a * b
# print('长方形的面积为：', s)
# l =  a * 2 + b * 2
# print('长方形的周长：', l)
# print('{:*>20}\n''{:*<20}'.format(s, l))
# import  math
# r = int(input('圆的半径为：'))
# l =  r * 2 * math.pi
# s  =  r ** 2 * math.pi
# print('圆的周长为：{:.0f}\n圆的面积为：{:.0f}'. format(l, s))
# print(type('hlleo'))
# a = 5
# b = 3
# print(a % b)
# print(a // b)
# a += b
# print(a)
# a -= b
# print(a)
# a *= b
# print(a)
# a /= b
# print(a)
# a **= b
# print(a)
# a //= b
# print(a)
# a = 20
# b = 10
# c = 0
# c = a + b
# print('1-c的值为：', c)
# c = a - b
# print('2-c的值为：', c)
# c = a * b
# print('3-c的值为：', c)
# c = a / b
# print('3-c的值为：', c)
# c = a ** b
# print('4-c 的值为：', c)
# c = a // b
# print('5-c的值为', c)
# c = a % b
# print('6-c的值为', c)
# a = 20
# b = 10
# c = 0
# if(a == b):
#     print('1-a等于b')
# else:
#     print('1-a不等于b')
# if(a != b):
#     print('2-a不等于b')
# else:
#     print('2-a等于b')
# if(a > b):
#     print('3-a大于b')
# else:
#     print('3-a小于b')
# if(a < b):
#     print('4-a小于b')
# else:
#     print('4-c大于b')
# age = int(input('请输入你家狗狗的年纪'))
# print('')
# if age < 0:
#     print('你在逗我')
# elif age == 1:
#     print('他的年龄是14岁')
# elif age == 2:
#     print('他的年纪是24岁')
# elif  age > 2:
#     humane = 22 +(age - 2) * 5
#     print('人类年龄：', humane)
# input('点击enter退出')
# v = '旅客尽快了解'
# v2 = '短发沙发上发呆'
# print('v[2]:', v[2])
# print('v2[1:5]', v2[1:5])
# a = int(input("请输入一个整数"))
# if a % 2 == 0 :
#     print('这个数是偶数')
# else:
#     print('这个数不是偶数')
# age = int(input('请输入你的年龄'))
# if  age >= 18:
#     print('你已经成年')
# else:
#     print('你没有成年')
# year = int(input('输入一个年份'))
# if  year % 4 == 0 and year % 100 != 0 or  year % 400 == 0:
#     print('这一年是闰年')
# else:
#     print('这年不是闰年')
# high = float(input('请输入你的身高'))
# wighr = float(input('输入你的体重'))
# BMI = wighr /(high ** 2)
# if BMI < 18.5:
#     print('过轻')
# elif 18.5 <= BMI <=25:
#     print('正常')
# elif 25 < BMI <= 28:
#     print('过重')
# elif 28 <= BMI <= 32:
#     print('肥胖')
# elif  BMI > 32:
#     print('严重肥胖')
# high = float(input('请输入身高'))
# if high < 1.2:
#     print('购买儿童票')
# else:
#     print('购买成人票')
#
# t = float(input('请输入温度'))
# if t < 15:
#     print('寒冷')
# elif 15 <= t <= 29:
#     print('正常')
# else:
#     print('炎热')
# age = int(input('请输入年龄'))
# print('成年' if age >=18 else '未成年')
# money = int(input('请输入薪资'))
# if money >=20000:
#     print('😄')
# elif  money >= 10000:
#     print( '一般')
# else:
#     print('😕')
# grade = float(input('请输入成绩'))
# if grade > 90:
#     print('奖励iphone8是一个')
# elif 70 <= grade <=90:
#     print('奖励小米一个')
# else:
#     print('处罚俯卧500个')
#
# age = int(input('请输入你的年龄'))
# if age < 4 :
#     print('免费')
# elif 4 <= age < 18:
#     print('3美元')
# elif 18 <= age <65:
#     print("10美元")
# else:
#     print('5美元')
# money = int(input('atm剩余的钱数'))
# money1 = int(input('你取的钱数'))
# if money1 % 100 != 0:
#     print('本机无法提供输入的面额')
# elif money < money1:
#     print('对不起，余额不足')
# elif:
#     money3 = money - money1
#     print('正在出钞，请从出钞口拿钱，atm机器剩余{}元'.format(money3))
# n = 100
# s = 0
# counter = 1
# while counter <= n:
#     s = s + counter
#     counter += 1
# print('i到{}的和为{}'.format(n, s))
# print('over')
# i = 0
# h = 0
# a = 0
# while i >= 0:
#     i += 1
#     n = float(input('输入{}个数'.format(i)))
#     if n != 0:
#         h = h + n
#     else:
#         print('运算结束')
#         break
# a = h / i
# print('和{}''平均数{}'.format(h, a))
# a = 0
# b = 0
# c = 0
# d = 0
# s = 0
# for i in range(1000, 5001):
#     a = i // 1000
#     b = i // 100 % 10
#     c = i % 100 // 10
#     d = i % 1000
#     s = a + b + c +d
#     if s % 5 ==0:
#         print(i)
#     else:
#         pass
# for i in range(3, 9):
#     if i % 2 == 0:
#         print(i)
#     else:
#         pass
# i = int(input('输入一个数'))
# s = 0
# a = 0
# b = 0
# c = 0
# d = 0
# e = 0
# while 10000 <= i <= 99999:
#      a = i // 10000
#      b = i % 10000 // 1000
#      c = i % 1000 // 100
#      d = i % 100 // 10
#      e = i % 10
#      break
# s = a + b + c + d + e
# print(s)
# n = input('输入一个数')
# s = 0
# for i in n:
#     s = s + int(i)
# print(s)
# a = int(input('矩形的长：'))
# b = int(input('矩形的宽：'))
# t =(a, b)
# for i in range(t[0]):
#     for o in range(t[1]):
#         print('*', end='')
#     print('*')
# b = int(input('矩形的宽：'))
# t = b
# for i in range(t):
#     for o in range(t - 1 - i ):
#         print('', end='')
#     for k in range(i+1):
#         print('*', end='')
#     print()
# n1=int(input("请输出要打印的层数"))
# for i in range(n1):
#     for j in range(n1-1 - i):
#         print(' ', end='')
#
#     for k in range(i + 1):
#         print('* ', end=' ')
#     print()
# for i in range(5, 0, -1):
#     print(i)
# x = int(input('输入一个正整数'))
# # for i in range(x):
# #     print(i * 2)
# x = int(input('输入一个正整数'))
# for i in range(0, 2 * x, 2):
#     print(i)
# for i in range (100, 1000):
#     if i % 7 != 0 and '7' not in  str(i):
#         print(i)

# a = int (input('输入一个正整数'))
# n = int (input('连续的次数'))
# s = a
# for i in range(n - 1):
#     a = a * 10 + a % 10
#     s = s + a
# print(s)
# a = int (input('输入一个正整数'))
# n = int (input('连续的次数'))
# s = a
# string = str(a)
# for i in range(n - 1):
#     a = a * 10 + a % 10
#     s = s + a
#     string = string + '+' + str(a)
# print(string, '=', s)
# numerator = 2
# denominator =1
# s = numerator / denominator
# string = '{}/{}'.format(numerator, denominator)
# for i in range(19):
#     numerator = numerator + denominator
#     denominator = numerator - denominator
#     print('{}/{}'.format(numerator, denominator))
#     s = s + numerator / denominator
#     string = string + '+' + '{}/{}'.format(numerator, denominator)
# print(string, '=', s)
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
# #     print('回到教室')
# qetwater(10, '百事可乐')
# def number(n):
#     for i in range(0, 101):
#         if str(n) in str(i):
#             print(i)
# number(6)
# number(1)
# number(9)
# number(8)
# def number(n):
#     s = 0
#     while n >0:
#         m = n % 10
#         s = s + m
#         n = n // 10
#     print(s)
#
#
# number(12)
# number(12345)

# def number(start, stop+1):
#     for i in range(start, stop+1):
#         if i % 2 == 0:
#             print(i)
# number(1, 10)
# def number(user,password):
#     i = 0
#     while i < 3:
#
#         n1 =int(input('输入用户名'))
#         n2 = int(input('密码'))
#         if n1 == user and n2 ==password:
#             print('登陆成功')
#             return
#         else:
#             print('登陆失败')
#         i +=1
#     print('over')
# number(12345, 12345)
# def  rectangle(long, wide):
#     for  i in range(long):
#         for o in range(wide):
#             print('*', end='')
#         print()
#
# rectangle(4, 5)
# def number(n):
#     a = n // 10 **(len(str(n))- 1)
#     b = n % 10
#
#     if a == b:
#         print('True', a)
#     else:
#         print('Flase', -1)
#     print('over')
# number(101)
#
# number(22)
# number(302)
# def number(n):
#     k = 0
#     a = 0
#     while k < n :
#         i = int(input('输入一个正整数'))
#         if i > a:
#             a = i
#         k += 1
#     print(a)
#
#
#
# number(5)
# l =[11, 22, 33, 44, 11, 11, 11, 99]
# # while 11 in l:
# #     l.remove(11)
# # print(l)
# # i = 0
# # while i < len(l):
# #     if 11 == l[i]:
# #         l.pop(i)
# #         i = i - 1
# #     i = i + 1
# # print(l)
# for v in l:
#     if v == 11:
#         l .remove(11)
# print(l)
# d = {'number': [11, 22, 33],
#      'name':'zhangsan',
#      'status': ((200, 'success'), (404,'notfound'))}
# # a = d.get('number')
# # b = a[2]
# # print(b)
# a = d .get('status')
# b = a[-1]
# c = b[-1]
# print(c)
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
#     'address': '成都'
# }
# # 通过key得到 student
# student = company['students']
# # student 是dict ，通过key得到遍历
# for key in student:
#     student1 = student[key]
#     # student1 是dict ，通过key得到遍历
#     for key2 in student1:
#         student2 = student1[key2]
#         # student2是dict ，通过key得到遍历
#         for student4 in student2:
#             print(student4)
# print(list(company.get('students').values()))
# print(company.get('teachers').get('测试')[0], company.get('students').get('Python').get('P1902')[0], company.get('address'))
# s = 0
# gard = {'语文': {'总成绩': (), '所有成绩': []}}
# gard1 = {'数学': {'总成绩': (), '所有成绩':[]}}
# gard2 = {'英语':{'总成绩':(), '所有成绩':[]}}
# gard4 = {}
# while True:
#     print('1、输入语文成绩')
#     print('2、输入数学成绩')
#     print('3、输入英语成绩')
#     print('4、显示所有成绩')
#     print('5、结束退出')
#     n = int(input('输入数字'))
#     if n == 1:
#         chinese = int(input('输入新增语文成绩：'))
#         s = s + chinese
#         gard['语文']['总成绩'] = s
#         gard['语文']['所有成绩'].append(chinese)
#         print(gard)
#     elif n == 2:
#         math = int(input('输入新增数学成绩：'))
#         s = s + math
#         gard1['数学']['总成绩'] = s
#         gard1['数学']['所有成绩'].append(math)
#         print(gard1)
#     elif n == 3:
#         englis = int(input('输入新增英语成绩：'))
#         s = s + englis
#         gard2['英语']['总成绩'] = s
#         gard2['英语']['所有成绩'].append(englis)
#         print(gard2)
#     elif n == 4:
#         gard4.update(gard)
#         gard4.update(gard1)
#         gard4.update(gard2)
#         print(gard4)
#     elif n == 5:
#         break
# def calscore(menu, s):
#     keys = tuple(s.keys())
#     key = keys[menu - 1]
#
#     score = int(input('请输入新增的{}成绩:'.format(key)))
#     s[key].append(score)
#     print('当前{}成绩:{}'.format(key, scores[key]))
#
#
# def showmenu():
#     print('1、输入语文成绩:')
#     print('2、输入数学成绩:')
#     print('3、输入英语成绩:')
#     print('4、显示所有成绩')
#     print('5、退出')
#     menu = int(input('请选择:'))
#     return menu
#
#
# if __name__ == '__main__':
#     import wxl.func
#     scores = {'语文': [], '数学': [], '英语': []}
#     while True:
#         n = wxl.func.showmen()
#         if 1 <= n <= 3:
#             calscore(n, scores)
#         elif n == 4:
#             print(scores)
#         elif n == 5:
#             break
# import wxl.func
# scores = {'语文': {'姓名':(),'成绩':()}, '数学':{'姓名': (),'成绩':()}, '英语':{'姓名':(),'成绩':()}}
# while True:
#         n = wxl.func.showmen()
#         if 1 <= n <= 3:
#             wxl.func.calscore(n, scores)
#         elif n == 4:
#             print(scores)
#         elif n == 5:
#             break
# def find(n, t):
#     for k in t:
#             if n == t[k]:
#                 print('找到了')
#                 break
# find(33,{'数字1': 11,'数字2': 22,'数字3': 33})

# class Student:
#     def __init__(self, name, height):
#         self.name = name
#         self. height = height
#     def cha(self, n, n1):
#         a = n1.height - n.height
#         print(a)
# zhangsan = Student('张三',166)
# lisi = Student('李四', 170)
# wangwu =Student('王五', 170)
# zhangsan.cha(lisi,wangwu)
# class Dog:
#     #构造函数
#     def __init__(self, name , weight):
#         self.name = name
#         self.weight = weight
#     def run(self):
#         a = self.weight - 0.1
#         self.weight = a
#         print(self.weight)
#     def eating(self):
#         a = self.weight + 0.1
#         self.weight = a
#         print(self.weight)
# dog = Dog('二哈', 60)
# dog.run()
# dog.run()
# dog.eating()
# def number(n):
#     a = abs(n)
#     print(a)
# number(-20)
# '''场景
# 创建一个狗类，具有体重，年龄， 颜色， 呢称等属性
# 可以进食、行走、 看门等动作
# 创建一个羊类， 具有身长、体重、年龄、颜色等属性，
# 可以进食、行走等动作'''
# class Dog:
#     def __index__(self, name, age, color, li, weight):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.li = li
#         self.weight = weight
#     def eating(self):
#         print('进食')
#     def xingzou(self):
#         print('行走')
#     def kanmen(self):
#         print('看门')
# class Sheep:
#     def __index__(self, height, weight, age, color):
#         self.height = height
#         self.weight = weight
#         self.age = age
#         self. color = color
#     def eating(self):
#         print('吃饭')
#     def xingzou(self):
# #         print('行走')
# class Human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
add = ('127.0.0.1', 41901)
server.bind(add)
print('jianting')
server.listen()
conn, addq = server.accept()
nsg = conn.recv(1460)
print(nsg)
print(addq)
print('jies')

# import socket
# client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server_addr = ('0.0.0.0', 41901)
# client.connect(server_addr)
# client.close()
# print('jieshu')

