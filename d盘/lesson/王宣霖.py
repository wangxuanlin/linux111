# money = 100
# save = 1000
# print(money + save)
# money = 199
# pen = 2.5
# cup = 5
# print(money - pen * 30 - cup * 5)
# a = 19
# b = 29
# c = 189
# print(a % 10, b // 10, c // 100 , c // 10 % 10 , c  % 180)
# chinese = 90
# English =66
# print(chinese + English , ( chinese + English) / 2 )
# a = 4
# print(a * 4, a ** 2 )
# # r = 3.5
# # raduis = r
# # # l = r * 3.14 * 2
# # # s = r ** 2 *3.14
# # # print( raduis, l , s )
# raduis = 3.5
# r = raduis
# import math
# s = r ** 2 * math.pi
# l = r *2 * math.pi
# print('该圆半径：{}\n 该圆面积：{}\n 该圆周长：{}'.format(raduis, s, l))
# #如果想提升优先级可以使用小括号
# print(1 + 10 * 2 / 2 -5)
# print(3.0 / 5)
# print(3.0 // 5)
# print(a * 10)
# print(True + 3)
# print(False + 3)
# print('hello' > 'world')
# print('h' > str(1))
# year = int(input('请输入一个年份'))
# if (year % 4 == 0 and year % 100 != 0) or  year % 400 == 0:
#     print('这一年是闰年')
# else:
#     print('这一年不是闰年')
# import  keyword
# print(keyword.kwlist)
# n = 100
#
# while n < 200:
#     n +=1
#     if n % 3 == 0 and n % 4 == 0:
#         print(n)
#     else:
#         pass
# print('over')
# n = 9
# a = 0
# b = 0
# while n < 100:
#     n += 1
#     a = n // 10
#     b = n % 10
#     if a == b:
#         print(n)
#     else:
#         pass
# print('over')
#
# n = 0
# while n < 100:
#     n += 1
#     if n % 8 == 0:
#         print(n)
#     else:
#         pass
# print('over')
# n = 0
# while n < 100:
#     n += 1
#     if n // 10 % 6 == 0 or n % 10 / 6 == 1:
#         print(n)
#     else:
#         pass
# print('over')
# num = int(input('班级人数'))
# i = 0
# s = 0
# an = 0
# while i< num:
#     i += 1
#     chinese = float(input('语文成绩'))
#     s = s+ chinese
#     an = s / num
# print('语文总成绩{}\n''语文平均成绩{}'.format(s, an))
# print('over')
# n = 0
# a = 0
# while n < 10:
#     n += 1
#     num = float(input('输入数据'))
#     if a == 1:
#         a = num
#     if num > a:
#         a = num
#     else:
#         pass
# print(num)
# print('over')
# n = 0
# s =0
# while n <100:
#     n += 1
#     if n % 2 == 0:
#         s = s + n
#     else:
#         s = s - n
# print(s)
# n = 100
# while n < 999:
#     a = n // 100
#     b = n % 100 // 10
#     c = n % 100 % 10
#     if n == a ** 3 + b ** 3 + c ** 3:
#         print(n)
#     else:
#         pass
#     n += 1
# print('over')
# n = 0
# s = 0
# s1 = 0
# while n < 7:
#     n += 1
#     c = int(input('输入{}天的温度'.format(n)))
#     s = s + c
# s1 = s / n
# print('总温度{}''平均温度{}'.format(s, s1))
# x = int(input('输入一个正整数'))
# for i in range(0, x):
#     if i % 2 == 0:
#         print(i)
# else:
#     pass
# print('over')
# for i in range(100, 1000):
#     if i % 7 != 0 and i % 10 != 7:
#         if i // 100 != 7 and i % 100 // 10 != 7:
#             print(i)
#
# else:
#     pass
# print('over')
# for i in range(100, 1000):
#     if i % 7 != 0 and i % 10 != 7 and i // 100 != 7 and i % 100 // 10 != 7:
#         # if i // 100 != 7 and i % 100 // 10 != 7:
#             print(i)
#
# else:
#     pass
# print('over')
#
# def number(n):
#     k = 0
#     s = []
#     while k < n:
#         i = int(input('输入数据'))
#         s.append(i)
#         k += 1
#     s.reverse()
#     print(s)
#
#
# number(5)
# 第二题
# i = ['12', '13', '33', '34']
# k = 0
# while k < len(i):
#     if '1' in i[k]:
#         i.remove(i[k])
#         k = k - 1
#     k += 1
# print(i)
# list1 = [11, 22, 33, 1, 6, 4, 88, 44]
# i = 0
# a = 0
# while i < len(list1):
#     if 33 > list1[i]:
#         a = list1[i]
#         print(a)
#     i += 1
# list1 = ['11', '22', '33', '1', '6', '4', '88', '44']
# i = 0
# a = 0
# while i < len(list1):
#     if 33 > int(list1[i]):
#         a = list1[i]
#         print(a)
#     i += 1
# print(a)
# list1 = [1, 2, 1, 3, 2, 5]
# list2 = []
# for i in list1:
#     list1.count(i)
#     if list1.count(i) < 2:
#         list2.append(i)
# print(list2)
# def number(n):
# #     list1 =[]
# #     k = 0
# #     a = 0
# #     while k < n:
# #         k += 1
# #         i = int(input('输入数字'))
# #         list1 .append(i)
# #         a = max(list1)
# #     print(a)
# # number(5)
# import random
# list1 =random.sample(range(100, 201), 20)
# a1 = 0
# a2 = 0
# a3 = 0
# a4 = 0
# list2 = []
# a1 = max(list1)
# a2 = min(list1)
# for i in list1:
#     a3 = a3 + i
# a3 = a3 / 20
# for k in range(len(list1)):
#     a4 = a3  - k
#     list2.append(a4)
# print(a1, a2, a3, list2)
# from string import digits
#
# s = '0go08o32d'
# remove_digits = str.maketrans('', '', digits)
# res = s.translate(remove_digits)
# print(res.upper())
# string = '0go08o32d'
# l = ''
# l = list(string)
# i = 0
# while i < len(l):
#     if l[i]in '1234567890':
#         l.remove(l[i])
#         i = i - 1
#     i += 1
# print(''.join(l).upper())
# for s in string:
#     if s not in '1234567890':
#         l = l + s
# print(l.upper())
# string = 'dafdafkjskljpng'
# while 'png' in string:
#     string = string.replace('png', '')
# print(string)
# l = 'aaabbccccdd'
# count = 1
# i = 0
# l1 = ''
# while i < len(l) - 1:
#     if l[i] == l[i + 1]:
#         count = count + 1
#     else:
#         print('{}{}'.format(count, l[i]))
#         l1 = l1 + '{}{}'.format(count, l[i])
#         count = 1
#     i = i + 1
#
#
# print('{}{}'.format(count, l[i]))
# l1 = l1 + '{}{}'.format(count, l[i])
# print(l1)
# def clacode(card):
#     year = card[6 : 10]
#     month = card[10: 12].lstrip('0')
#     day = card[12: 14].lstrip('0')
#     gender = '女' if int(card[-2]) % 2 == 0 else '男'
#     return '{}年{}月{}日 {}'.format(year, month, day, gender)
# code = '111123311234532123'
# print(clacode(code))
#
# import wxl.func
# scores = {'语文': [], '数学':[], '英语':[]}
# while True:
#         n = wxl.func.showmen()
#         if 1 <= n <= 3:
#             wxl.func.calscore(n, scores)
#         elif n == 4:
#             print(scores)
#         elif 6 <= n <= 8:
#             wxl.func.name(n, scores)
#             print(scores)
#         elif n == 5:
#             break
# def showmen():
#     print('1、添加成员:')
#     print('2、根据成员编号查询成员信息:')
#     print('3、根据成员编号修改成员信息:')
#     print('4、移除某个成员')
#     print('5、查看所有成员')
#     print('6、退出')
#     menu = int(input('请选择:'))
#     return menu
# def calscore(s):
#     serial1 = int(input('输入编号'))
#     result = seahchstudents(serial1, s)
#     if result is not None:
#         print('输入信息：', result)
#         return
#     name = input('姓名')
#     age = int(input('年龄'))
#     telephonenumber = input('电话')
#     site = input('地址')
#     student ={'编号': serial1, '姓名': name, '年龄': age, '电话': telephonenumber, '地址':site}
#     s.append(student)
#     print(s)
#     return s
# def seahchstudents(serial1, s):
#     for student in s:
#         if student['编号'] == serial1:
#             print('查有此人')
#             return student
#         else:
#             print('输入信息')
#             return
# def showremove(s):
#     serial = int(input('输入编号'))
#     result = seahchstudents(serial, s)
#     if result is not None:
#         s.remove(result)
#         print('删除成功')
#     else:
#         print('删除不成功')
#
# def searchstudent(s):
#     serial = int(input('输入编号'))
#     result = seahchstudents(serial, s)
#     if result is not None:
#         print('1、修改电话')
#         print('2、修改地址')
#         n = int(input('输入选择'))
#         if n == 1:
#             phone = input('电话号')
#             result['电话'] = phone
#         elif n == 2:
#             site = input('地址')
#             result['地址'] = site
#         print('修改成功')
#     else:
#         print('无法修改')
# def showone(s):
#     serial = int(input('输入编号'))
#     result = seahchstudents(serial, s)
#     if result is not None:
#         print(result)
#     else:
#         print('查无此人')
# def showall(s):
#     print(s)
# if __name__ == '__main__':
#     students = []
#     a = calscore
#     while True:
#         n = showmen()
#         if n == 1:
#             a(students)
#         elif n == 2:
#             showone(students)
#         elif n == 3:
#             searchstudent(students)
#         elif n == 4:
#             showremove(students)
#         elif n == 5:
#             showall(students)
#         elif n == 6:
#             break
# def danjia(s):
#     name = input('输入商品名称')
#     money = int(input('商品单价'))
#     a ={'名称': name, '单价': money}
#     s.append(a)
#     print(s)
# def gouwuche(s, money):
#     money1 = 0
#     name = input('输入商品名称')
#     money = int(input('输入单价'))
#     number = int(input('输入购买数量'))
#     a = {'名字': name, '单价': money, '购买数量': number}
#     s.append(a)
#     for i in s:
#         k = i['单价']
#         g = i['购买数量']
#         money1 += k *g
#     if 0 < money1 < 500:
#         print(s, '总价:{}'.format(money1))
#     elif 500 <= money1 < 1000:
#         money1 = money1 -50
#         print(s, '总价:{}'.format(money1))
#     else:
#         money1 = money1 - 100
#         print(s)
#     money = money1
#     print(s, money)
#     return s,money
# def chazhao(s, name):
#     for i in s:
#         if i['名字'] == name:
#             print('商品找到')
#             return i
#         else:
#             print('添加商品')
#             return
#
# def tianjia(s):
#     name = input('商品名称')
#     i = chazhao(s, name)
#     if i is not None:
#         number = i['购买数量']
#         number += 1
#         return i
#     else:
#         money = int(input('输入单价'))
#         number = int(input('输入购买数量'))
#         a = {'名字': name, '单价': money, '购买数量': number}
#         s.append(a)
#     print(s)
#     return s
# def yichu(s):
#     name = input('商品名称')
#     i = chazhao(s, name)
#     if i is not None:
#         s.remove(i)
#         print('删除成功')
#     else:
#         print('无法删除')
#     return s
# def jiezhuang(s,money):
#     print(s, money)
# def showmen():
#     print('1、查看商品目录:')
#     print('2、查看当前购物车的商品信息:')
#     print('3、添加商品到购物车:')
#     print('4、移除指定商品')
#     print('5、结账')
#     menu = int(input('请选择:'))
#     return menu
#
#
# if __name__ == '__main__':
#     s = []
#     s1 = []
#     money2 = 0
#     while True:
#         n = showmen()
#         if n == 1:
#             danjia(s)
#         elif n == 2:
#             gouwuche(s1, money2)
#         elif n == 3:
#             tianjia(s1)
#         elif n == 4:
#             yichu(s1)
#         elif n == 5:
#             jiezhuang(s,money2)
#             break
#
#
# def showallinfo(goods):
#     """
#     显示所有商品信息
#     """
#     print('所有商品信息如下:')
#     for good in goods:
#         print('名称:{}, 单价:{}'.format(good['name'], good['price']))
#     print('*' * 30)
#
# def showshopingcarinfo(goods):
#     """
#     显示购物车信息
#     """
#     print('*' * 10, '购物车信息如下:')
#     s = 0
#     for good in goods:
#         if good['number'] > 0:
#             s = s + good['price'] * good['number']
#             print('名称:{}, 单价:{}, 数量:{}, 该商品总价:{}'
#                   .format(good['name'], good['price'], good['number'],
#                           good['price'] * good['number']))
#     if s == 0:
#         print('购物车是空的')
#     else:
#         print('购物车目前总价:', s)
#     return s
#
#
# def addgood(goods):
#     """
#     添加商品到购物车
#     1、输入商品名称，判定商品是否存在
#     2、如果存在，则默认将数量+1
#     3、如果不存在，则不能操作
#     """
#     showallinfo(goods)
#     name = input('输入商品名称:')
#     good = searchgood(name, goods)
#     if good is not None:
#         good['number'] += 1
#         print('添加成功')
#     else:
#         print('商品不存在，不能执行添加操作')
#
# def removegood(goods):
#     """
#     从购物车中移除商品
#     """
#     print('购物车中商品有')
#     showshopingcarinfo(goods)
#     print('*'* 20)
#     name = input('商品名称')
#     i = searchgood(name, goods)
#     if i is not None:
#         i['numbe'] -= 1
#         print('删除成功，当前商品剩余{}'.format(i['number']))
#     else:
#         print('无法删除')
#
# def searchgood(name, goods):
#     """
#     查询商品是否存在
#     """
#     for good in goods:
#         if name == good['name']:
#             return good
# def jiezhuang(goods):
#     s = showshopingcarinfo(goods)
#     money = s // 500 * 50
#     print('商品优惠{}, 需要支付{}'.format(money, s - money))
# def showmenu():
#     print('1、显示商品信息')
#     print('2、添加商品到购物车')
#     print('3、移除商品出购物车')
#     print('4、查看购物车')
#     print('5、结账退出')
#     n = int(input('请选择菜单:'))
#     return n
#
#
# if __name__ == '__main__':
#     goodslist = [
#         {'name': 'pen', 'price': 200, 'number': 0},
#         {'name': 'cup', 'price': 50, 'number': 0},
#         {'name': 'book', 'price': 20, 'number': 0}
#     ]
#     while True:
#         n = showmenu()
#         if n == 1:
#             showallinfo(goodslist)
#         elif n == 2:
#             addgood(goodslist)
#         elif n == 3:
#             removegood(goodslist)
#         elif n == 4:
#             showshopingcarinfo(goodslist)
#         elif n == 5:
#             jiezhuang(goodslist)
#             break
#
# class Student:
#     def __init__(self, name, gender, age, code, height, wight):
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.code = code
#         self.height = height
#         self.wight = wight
#     def shenggao(self):
#         s ={'姓名': self.name, '性别': self.gender, '年龄': self.age, '身份证号': self.code, '身高': self.height, '体重': self.wight}
#         print(s)
#     def bijiao(self,student):
#         if self.height > student.height:
#             print(self.height)
#         else:
#             print(student.height)
#
#
# student = Student('wangwu', 'nan', 15, 12222, 160, 50,)
# student1 = Student('lisi', 'nan',15, 122222, 170, 60)
# student.shenggao()
# student.bijiao(student1)
# class Teacher:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def introducename(self, student):
#         student.introduce()
#     def calculate(self, student):
#         difference = self.age - student.age
#         if difference > 0:
#             print('{}比老师小{}岁'.format(student.name, difference))
#         elif difference == 0:
#             print('{}跟老师同岁'.format(student.name))
#         elif difference < 0:
#             print('{}比老师大{}岁'.format(student.name, difference * -1))
#     def pet(self, phrase):
#         print('{}的口头禅是：{}'.format(self.name, phrase))
#
# teacher = Teacher('李宁', 30)
# teacher.introducename(student)
# teacher.introducename(student1)
# teacher.calculate(student1)
# teacher.pet('调皮')
# class Yuan:
#     def __init__(self,r):
#         self.r = r
#     def mianji(self):
#         import math
#         s = self.r ** 2 * math.pi
#         l = 2 * self.r* math.pi
#         print(s, l)
#         return s, l
#
# yuan = Yuan(2)
# yuan.mianji()
#
# class  loop:
#     def __init__(self, r1, r2):
#         self.r1 = r1
#         self.r2 = r2
#         area = 3.14 * r1 ** 2 - 3.14 * r2 ** 2
#         if area >= 0:
#             print('圆环的周长：{}，圆环的面积：{}'.format(2 * 3.14 * r1 + 2 * 3.14 * r2, area))
#         else:
#             print('圆环的周长：{}，圆环的面积：{}'.format(2 * 3.14 * r1 + 2 * 3.14 * r2, area * -1))
# r3 = loop(3, 4)
# def number(n):
#     for i in range(2,n):
#         if n % i == 0:
#             print('{}不是素数'.format(n))
#             break
#     else:
#         print('{}是素数'.format(n))
#
# number(15)
# number(2)
# def str(n):
#     isenglish = []
#     isnumber =[]
#     isspace = []
#     isother =[]
#     for i in range(len(n)):
#         if ord(n[i]) in range(65, 91) or ord(n[i]) in range(97, 123):
#             isenglish.append(n[i])
#         elif n[i] == ' ':
#             isspace.append(n[i])
#         elif ord(n[i]) in range(48, 57):
#             isnumber.append(n[i])
#         else:
#             isother.append(n[i])
#     print("有{}个数字，有{}个字母，有{}个空格， 有{}个字符".format(len(isnumber), len(isenglish), len(isspace), len(isother)))
# str('adafasd12  3312233')

# class Human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def eating(self):
#         print('吃饭')
#
# class Teacher(Human):
#     def __init__(self,name, age, gender, card, teache):
#         self.teache = teache
#         self.card = card
#         super().__init__(name, age, gender)
#
#     def teach(self):
#         print('授课')
#
# class Student(Human):
#     def __index__(self, name, age, gender, card, study, like):
#         self.card = card
#         self.study = study
#         self.like = like
#         super().__init__(name, age, gender)
#
#     def studys(self):
#         print('学习')
#
#     def likes(self):
#         print('{}'.format(self.like))
#
# class Educational(Human):
#     def __init__(self, name, age, gender, classe):
#         self.classe = classe
#         super().__init__(name, age, gender)
#
#     def study(self):
#         print('抓学习')
#
#     def sleep(self):
#         print('睡觉')
# class Leader(Human):
#     def __index__(self, name, age, gender):
#         super().__init__(name, age, gender)
#
#     def speek(self):
#         print('专属口头禅')
#
#     def meeting(self):
#         print('开会')
#
#     def mahjong(self):
#         print('打麻将')
#
#
#
# teacher1 = Teacher('李浩说', 30, '男', '1001', 'c')
# teacher1.eating()
# teacher1.teach()
# 2、# 2、写1个项目经理类.
#    属性: 姓名、 基本工资、项目分红(默认10000)、项目奖金.
#     行为: 介绍自己的方法. 叫xx 每月薪水是多少.
#
#    再写1个软件工程师类.
#    属性: 姓名、基本工资、项目奖金.
#    行为: 介绍自己的方法. 叫xx 每月薪水是多少.
# class Humane:
#     def __init__(self, name, gong, jiang):
#         self.jiang = jiang
#         self.name = name
#         self.gong = gong
#
#
# class Xiang(Humane):
#     def __init__(self, name, gong, jiang, fen =10000):
#         self.fen = fen
#         super().__init__(name, gong, jiang)
#
#     def monry(self):
#         return self.jiang + self.fen + self.gong
# class Ruan(Humane):
#     def __init__(self, name, gong, jiang):
#         super().__init__(name, gong, jiang)
#
#     def money(self):
#         return self.jiang + self.gong

# 3、设计一个”狗“类，包含属性（颜色、奔跑的速度m/s、性别、体重kg）
# 行为： 吃：(每吃一次，体重增加0.5kg，输出吃完后的体重)  、吠（叫）：（输出所有的属性）、跑：（每跑一次，体重减少0.5kg，输出速度和跑完后的体重）
# 设计一个"猫"类，包含属性（颜色、性别、体重）
# 行为：* 吠（叫）：输出所有的属性
# 1）根据上诉内容，提炼父类，派生子类
# 2）创建对象，调用狗的吃行为和跑行为
# class Animal:
#     def __init__(self, gender, weight, color):
#         self.gender = gender
#         self.weight = weight
#         self.color = color
#
#     def jiao(self):
#         print('叫', self.gender, self.color, self.weight)
#
#
#
# class Dog(Animal):
#     def __init__(self, run, gender, color, weight):
#         self.run = run
#         super().__init__(weight, gender, color)
#
#     def eating(self):
#         print(self.weight + 0.5)
#
#     def running(self):
#         print(self.weight - 0.5)
#
#
# class Sheep(Animal):
#     def __init__(self, weight, gender, color):
#         super().__init__(weight, color, gender)
# sheep = Sheep( 50,'白', 'nv')
# sheep.jiao()
# class Commoity:
#
#     def __init__(self,card, name, number, price):
#         self.card = card
#         self.name = name
#         self.number = number
#         self.price = price
#         self.money = self.price * self.number
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
#         return '商品编号：{}，名称：{}，单价：{}，数量：{}, 总价：{}'.format(self.card, self.name, self.price, self.number, self.money)
#
# class KU:
#     commoity = []
#
#     def chakan(self):
#         name = input('输入名字')
#         price = int(input('输入单价'))
#         card = input('输入编号')
#         number = int(input('输入数量'))
#         comm = Commoity(card, name, number, price)
#         self.commoity.append(comm)
#
#     def tianjia(self):
#         name = input('输入名字')
#         for i in self.commoity:
#             if name == i.name:
#                 i.number = i.number + 1
#                 return i.number
#
#     def maichu(self):
#         name = input('输入名字')
#         for i in self.commoity:
#             if name == i.name and i.number > 0:
#                 i.number = i.number - 1
#                 return
#             elif name == i.name and i.number < 0:
#                 print('库存不够')
#             else:
#                 print('没有该商品')
#
#     def xiugai(self):
#         name = input('输入名字')
#         for i in self.commoity:
#             if name == i.name:
#                 i.price = int(input('输入修改单价'))
#                 return i.price
#
#
#     def startinput(self):
#         while True:
#             print('1、添加商品')
#             print('2、添加指定商品')
#             print('3、卖出商品')
#             print('4、查看商品')
#             print('5、修改单价')
#             print('6、退出')
#             n = int(input('请选择:'))
#             if n == 1:
#                 self.chakan()
#             elif n == 2:
#                 self.tianjia()
#             elif n == 3:
#                 self.maichu()
#             elif n == 4:
#                 for i in self.commoity:
#                     print(i)
#             elif n == 5:
#               self.xiugai()
#             elif n == 6:
#                 break
#         print('结束')
#
#
# if __name__ == '__main__':
#     lsz = KU()
#     lsz.startinput()

#
# class Students:
#     def __init__(self, carde, name, age, chengji):
#         self.carde = carde
#         self.name = name
#         self.age = age
#         self.chengji = chengji
#
#     def __str__(self):
#         return '学号：{}，名字：{}，年纪：{}，成绩：{}'.format(self.carde, self.name, self.age, self.chengji)
#
#
# class Teacher:
#     def __init__(self, name):
#         self.name = name
#
#     def inputmenue(self):
#         return int(input('选择菜单'))
#
#     def tercher_addstudent(self, computer):
#         carde = input('输入学号')
#         student = computer.searchcarde(carde)
#         if student is not None:
#             print('不要添加，有此人信息')
#         else:
#             name = input('输入学生名字')
#             age = int(input('输入学生年龄'))
#             chengji = input('输入学生成绩')
#             student1 = Students(carde, name, age, chengji)
#             keys = tuple(computer.student.keys())
#             print('当前组有如下', keys)
#             key = ''
#             while key not in keys:
#                 key = input('输入组名')
#             return key, student1
#
#     def teacher_popstudent(self, computer):
#         carde = input('输入学号')
#         student = computer.searchcarde(carde)
#         if student is not None:
#             return student
#
#
# class Computer:
#     teachers = [Teacher('lwy'),
#                 Teacher('xiasisi')]
#     student = {'computer': [], 'math': [], 'chinese': [], 'star': [], 'python': []}
#
#     def __init__(self):
#         self.teacher = None
#
#     def showmenu(self):
#         print('1、添加一名学生到一个小组：')
#         print('2、删除一名学生：')
#         print('3、打印整个小组的信息，按学号排序：')
#         print('4、查看班级所有成绩和小组的平均成绩：')
#         print('5、筛选全班在某两个成绩直接的所有学生按年龄排列：')
#         print('6、退出')
#         return self.teacher.inputmenue()
#
#
#     def addstudent(self):
#         result = self.teacher.tercher_addstudent(self)
#         if result is not None:
#             self.student[result[0]].append(result[-1])
#         print('添加成功')
#
#     def popstudent(self):
#         result = self.teacher.teacher_popstudent(self)
#         if result is not None:
#             key = result[0]
#             student = result[-1]
#             self.student[key].remove(student)
#             print('删除成功')
#
#     def shuaixuanstudent(self):
#         for key, val in self.student.items():
#             if val is not None:
#                 a = 0
#                 b = 0
#                 m = 0
#                 for i in val:
#                     a = a + int(i.chengji)
#                     b = b + 1
#                     m = a / b
#                 print('{}组的总成绩：{}'.format(key, a))
#                 print('{}组的平均成绩：{}'.format(key, m))
#
#     def searchcarde(self, carde):
#         for key in self.student:
#             for i in self.student[key]:
#                 if i.carde == carde:
#                     return key, i
#         print('不存在')
#
#     def showallinfo(self):
#         print('*' * 10, '所有学生信息如下：')
#         for key, stus in self.student.items():
#             if len(stus) == 0:
#                 continue
#             print('{}组信息入下：'.format(key))
#             for stu in stus:
#                 print(stu)
#             print('*' * 30)
#     def login(self):
#         name = input('输入名字')
#         for teacher in self.teachers:
#             if teacher.name == name:
#                 return teacher
#
#     def poweron(self):
#         teacher = self.login()
#         if teacher is None:
#             print('登陆失败')
#             return
#         print('登陆成功，欢迎',
#               teacher.name)
#
#         self.teacher = teacher
#         while True:
#             n = self.showmenu()
#             if n == 1:
#                 self.addstudent()
#             elif n == 2:
#                 self.popstudent()
#             elif n == 3:
#                 self.shuaixuanstudent()
#             elif n == 4:
#                 self.showallinfo()
#             elif n == 5:
#                 pass
#             elif n == 6:
#                 break
#
#
# if __name__ == '__main__':
#     computer1 = Computer()
#     computer1.poweron()

import re

class Member:
    def __init__(self, name, telephone, box):
        self.name = name
        self.telephine = telephone
        self.box = box

    def __str__(self):
        n = '名字：{}， 电话：{}， 邮箱：{}'.format(self.name, self.telephine, self.box)
        return n


class Boss:
    def __init__(self, name):
        self.name = name

    def add_member(self,computer):
        name = input('输入名字')
        n = '^[A-Z]{5, 9}+$'
        member = computer.seachermember(name)
        if member is None:
            telephone = input('输入电话号')
            p ='^1[3|5|8][0-9]{9}$'
            telephone1 = re.match(p, telephone)
            box = input('输入邮箱')
            b = '^[A-Za-z]{5,9}*@[(163)|(123)]+([-.]\w+)*\.\w+([-.]\w+)*$'
            box1 = re.match(b, box)
            member1 = Member(name, telephone1, box1)
            return member1

    def pop_member(self):
        pass

    def show_member(self):
        pass


class Computer:
    d = {'A': [], 'B': [], 'C': [], 'D': []}

    def __init__(self):
        self.boss = None

    def addmember(self):
        pass

    def popmember(self):
        pass

    def seachermember(self, name):
        for key, value in self.d.items():

            pass




    def showmember(self):
        pass









