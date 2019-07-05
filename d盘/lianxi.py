# a = 10
# b = 25
# if( a == b ):
#     print('a>b')
# else:
#     print('a<=b')
# if( a != b ):
#     print('a=b')
# else:
#     print('a不等于b')
# if( a > b  ):
#     print('a>b')
# else:
#     print('a<=b')
# if( a < b ):
#     print("a<b")
# else:
#     print('a>=b')
# if( a >= b ):
#     print("a>=b")
# else:
#     print('a<b')
# a = 10
# b = 23
# c = 0
# c += a
# print('c=', c)
# c /= b
# print('c=', c)
# c *= b
# print('c=', c)
# c -= a
# print('c=', c)
# c //= b
# print('c=', c)
# c %= b
# print('c=', c)
# c **= a
# print('c=', c)
# a = 60
# b = 13
# c = 0
# c = a & b
# print('c=' ,c)
# c = a ^ b
# print('c=' ,c)
# c = a | b
# print('c=' ,c)
# c = ~ a
# print('c=' ,c)
# c = a >> 2
# print('c=' ,c)
# c = a << 2
# print('c=' ,c)
# print(True + 3)
# print(False + 3)
# print('aaz' > 'aba')
# print("今天星期：几"
#       "我叫：什么"
#       "我来自:哪里")
# s = input('输入：helloworld');
# print('你输入的内容是:', s)
# def money(save):
#     money1 = 100
#     money1 = money1 + save
#     print(money1)
#
# money(1000)

# def money(a , b):
#     money1 = 199
#     money1 = 199 - 2.5 * a - 5 * 5
#     print(money1)
#
# money(30, 5)
# def numbeir(n):
#     n1 = 0
#     n2 = 0
#     n3 = 0
#     while n > 9:
#         if 10 < n < 20:
#             n = n % 10
#         elif 20 < n <100:
#             n = n // 10
#         elif n > 100:
#             n1 = n // 100
#             n2 = n % 100 //10
#             n3 = n % 10
#             break
#     print(n, n1, n2, n3)
# numbeir(19)
# numbeir(29)
# numbeir(189)
# # def garde(chinesee, english):
#     s = chinesee + english
#     p = s / 2
#     print(s, p)
# garde(90, 66)
# def square(a):
#     s = a * a
#     l = a * 4
#     print(s, l)
# square(4)
# def circle(radius):
#     import math
#     s = radius ** 2 * math.pi
#     l = 2 * radius * math.pi
#     print(radius, s, l)
# circle(1.5)
# def trigon(a, b, c):
#     if a + b < c or a - b >c:
#         return False
#     elif a == b :
#         print('等腰三角形')
#         return
#     elif a == b and b == c:
#         print('等边三角形')
#         return
#     else:
#         print('普通三角形')
#         return


# trigon(3, 3, 5)
# import 和 include 的区别 """" 和《》的区别
# ""先找路径再去找系统的， 《》不去找路径
# # a = range(1, 1001)
# list1 = [1, 2, 3, 4, 9, 6, 7, 8, 9, 10]
# a = sum(list1)
# print(a)
# def number(n, s):
#     keys = tuple(s.keys())
#     key = keys(n - 1)
#     a = int(input('输入{}的成绩'.format(key)))
#     s[key].append(a)
#     print('{}的成绩{}，总成绩{}'.format(key, a, sum(s[key])))
# def has():
#     print('1、输入语文成绩:')
#     print('2、输入数学成绩:')
#     print('3、输入英语成绩:')
#     print('4、显示所有成绩')
#     print('5、退出')
#     n = int(input('输入数字'))
#     return n
# def calscore(menu, q, s, ls):
#     n1 = q.append(input('请输入学生名字：'))
#
#     keys = tuple(s.keys())
#     key = keys[menu - 1]
#
#     score = int(input('请输入学生{}成绩:'.format(key)))
#     s1 = s[key].append(score)
#     ls.setdefault(n1, s1)
#     print('当前{}学科成绩如下:\n{}'.format(key, scores[key]))
#
#
# def display(x, y):
#     print('*' * 10 + '所有学科成绩如下:')
#     k1 = ('语文', '数学', '英语')
#     for i in range(3):
#         print('学科{}成绩如下：'.format(k1[i]))
#         for j in y:
#             print('姓名{}, 分数{}'.format(j, x[j][i]))
#
#
# if __name__ == '__main__':
#     scores = {'语文': [], '数学': [], '英语': []}
#     name = []
#     listscore = {}
#     while True:
#         n = showmenu()
#         if 1 <= n <= 3:
#             calscore(n, name, scores, listscore)
#         elif n == 4:
#             display(listscore, name)
#         elif n == 5:

# dict1 = {'Name': 'Zara', 'Age': 7};
# dict2 = {'Name': 'Mahnaz', 'Age': 27};
# dict3 = {'Name': 'Abid', 'Age': 27};
# dict4 = {'Name': 'Zara', 'Age': 7};
# dict = {'Name': 'Runoob', 'Age': 7}
#
# print ("Value : %s" % dict.items())
# confusion = {}
# # confusion[1] = 1
# # confusion['1'] = 2
# # confusion[1] += 1
# #
# # sum = 0
# # for k in confusion:
# #     sum += confusion[k]
# #
# # print(sum)
# newStuId = 0
# newStuName = ""
# newStuAge = ""
#
#
# class Student:
#     def __init__(self, stuName, stuAge):
#         global newStuId
#         newStuId += 1
#         self.stuId = newStuId
#         self.stuName = stuName
#         self.stuAge = stuAge
#
#
# # 系统管理类
# class Sys:
#     def __init__(self):
#         pass
#
#     # 显示系统菜单
#     def show_menu(self):
#         print("=" * 10)
#         print("1添加用户信息")
#         print("2查看用户信息")
#         print("0退出系统")
#         print("=" * 10)
#
#     # 输入学生信息
#     def getinfo(self):
#         # global newStuId
#         global newStuName
#         global newStuAge
#         # newStuId = input("请输入学号：")
#         newStuName = input("请输入姓名：")
#         newStuAge = input("请输入年龄：")
#
#     # 添加学生信息
#     def addstu(self):
#         s = Student(newStuName, newStuAge)
#         students[newStuId] = s
#         print("学号：%s\t年龄：%s\t姓名：%s" % (students[newStuId].stuId, students[newStuId].stuName, students[newStuId].stuAge))
#
#     # 查看学生信息
#     def findstu(self):
#         findId = int(input("请输入要查询的学号："))
#         if findId in students.keys():
#             print("学号：%s\t年龄：%s\t姓名：%s" % (
#             students[newStuId].stuId, students[newStuId].stuName, students[newStuId].stuAge))
#         else:
#             print("查无此人")
#
#     # 退出系统
#     def exitstu(self):
#         exit()
#
#
# # 创建系统对象
# sys = Sys()
# # 定义一个容器来存储学生信息
# students = {}
# while True:
#     sys.show_menu()
#     choice = int(input("请输入要执行的操作："))
#     if choice == 1:
#         sys.getinfo()
#         sys.addstu()
#     elif choice == 2:
#         sys.findstu()
#     elif choice == 0:
#         sys.exitstu()
#     else:
#         print("输入有误，重新输入。")

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
#         number = i['购买数量'] + 1
#         i['购买数量'] = number
#         print(s)
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
#     for i in s:
#         k = i['单价']
#         g = i['购买数量']
#         money+= k * g
#         if 0 < money < 500:
#             print('总价:{}'.format(money))
#         elif 500 <= money < 1000:
#             money = money - 50
#             print('总价:{}'.format(money))
#         elif money > 1000:
#             money = money - 100
#     print('商品列表：{},总价：{}'.format(s,money))
#
#
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
#             jiezhuang(s1, money2)
#             break
# counter = 100
# miles =1000.0
# name = 'bob'
# print(name)
# print(miles)
# print(counter)
# s = 'abcdfe'
# print(s[1: 5])
# str = 'hello world'
# print(str)
# print(str[0])
# print(str[2: 5])
# print(str[2:])
# print(str * 2, end ='')
# print(str + 'the')
# list = ['runoob', 786, 2.23, 'john', 70.2]
# thelist = [123, 'john']
# print(list)
# print(list[0])
# print(list[1: 3])
# print(list[2:])
# print(thelist * 2)
# print(list + thelist)
# tuple = ()
# tinytuple = (123, 'john')
# print(tuple)
# # print(tuple[0])
# # print(tuple[1: 3])
# # print(tuple[2:])
# print(tinytuple * 2)
# print(tuple + tinytuple)
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
# class Commodity:
#     def __init__(self, cord, name, number, money):
#         self.cord = cord
#         self.name = name
#         self.number = number
#         self.money = money
#
#     @property
#     def zonge(self):
#         return self.money * self.number
#     def __str__(self):
#          return '编号：{}，名字：{}，数量：{}，单价：{}，总价：{}'\
#              .format(self.cord,
#                      self.name,
#                      self.number,
#                      self.money, self.zonge)
#
#
#
# commodity = Commodity('1001', 'pen', 10, 20)
# print(commodity)

# class Good:
#     def __init__(self, code, name, price, number):
#         self.code = code
#         self.name = name
#         self.price = price
#         self.number = number
#
#     @property
#     def sumprice(self):
#         return self.price * self.number
#
#     def __str__(self):
#         return '编号:{}, 名字:{}, 单价:{}, 数量:{}, 总价:{}'\
#             .format(self.code, self.name,
#                     self.price, self.number,
#                     self.sumprice)
#
#
# good1 = Good('101', '方便面', 10, 20)
# print(good1)

# class Student:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code
#         self.point = None
#
#     @property
#     def age(self):
#         return 2019 - int(self.code[6:10])
#
#     @property
#     def birthday(self):
#         return '{}年{}月{}日'.format(
#             self.code[6: 10],
#             self.code[10: 12].lstrip('0'),
#             self.code[12: 14].lstrip('0')
#         )
#
#     def calpoint(self, student2):
#         point1 = self.point
#         point2 = student2.point
#
#         point_x = (point1[0] - point2[0]) ** 2
#         point_y = (point1[-1] - point2[-1]) ** 2
#
#         return (point_x + point_y) ** 0.5
#
#
# stu1 = Student('zhangsan', '110101200009099898')
# stu2 = Student('lisi', '110101200009079090')
#
# stu1.point = (1, 1)
# stu2.point = (2, 2)
# print(stu1.calpoint(stu2))
# class Student:
#     def __init__(self, name, number):
#         self.name = name
#         self.number = number
#
#     def __str__(self):
#         return '姓名：{}，电话：{}'.format(self.name, self.number)
#
# class Teacher:
#
#     student = []
#
#     def tianjia(self):
#         name = input('输入学生：')
#         number = input('输入电话')
#         students = Student(name, number)
#         self.student.append(students)
#
#     def sanchu(self):
#         name = input('输入学生：')
#         for stu in self.student:
#             if name == stu[name]:
#                 self.student.remove(name)
#             else:
#                 pass
#
#     def startinput(self):
#         while True:
#             print('1、添加学生')
#             print('2、删除学生')
#             print('3、显示学生')
#             print('4、退出')
#             n = int(input('请选择:'))
#             if n == 1:
#                 self.tianjia()
#             elif n == 2:
#                 self.sanchu()
#             elif n == 3:
#                 for stu in self.student:
#                     print(stu)
#             elif n == 4:
#                 break
#         print('录入结束')
#
# if __name__ == '__main__':
#     lwy = Teacher()
#     lwy.startinput()
#
# class Commoity:
#
#     def __init__(self,card, name, number, price):
#         self.card = card
#         self.name = name
#         self.number = number
#         self._price = 0
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

# class Good:
#     def __init__(self, barcode, name, price, count):
#         self.barcode = barcode
#         self.name = name
#         self.price = price
#         self.count = count
#     @property
#     def sumprice(self):
#         return self.price * self.count
#
#     def __str__(self):
#         return '商品编号：{}，名称：{}，单价：{}，数量：{}'.format(self.barcode, self.name, self.price, self.count)
#
#
# class People:
#     def __init__(self, name):
#         self.name = name
#
#     def inputmenue(self):
#         return int(input('选择菜单'))
#
#     def seller_addgood(self,computer):
#         barcode = input('输入商品编号')
#         good = computer.searchgood(barcode)
#         if good is not None:
#             count = int(input("输入需要增加对数量"))
#             return good, count
#         else:
#             name = input('输入商品名称')
#             price = int(input('输入新商品单价'))
#             count = int(input('输入新商品数量'))
#             newgood = Good(barcode, name, price, count)
#             return newgood
#
#     def seller_sellgood(self, computer):
#         barcode = input('输入商品编号')
#         good = computer.searchgood(barcode)
#         if good is not None:
#             count = int(input('输入卖出商品'))
#             return good, count
#
#
#     def seller_editgood(self, computer):
#         barcode = input('输入商品编号')
#         good = computer.searchgood(barcode)
#         if good is not None:
#             price = int(input('商品价格'))
#             return good, price
#
#
# class Computer:
#     goods = []
#
#     def __init__(self):
#         self.seller = None
#
#     def showmenue(self):
#         print('1、添加商品')
#         print('2、卖出商品')
#         print('3、修改商品单价')
#         print('4、查看库存')
#         print('5、退出')
#         n = self.seller.inputmenue()
#         return n
#
#     def addgood(self):
#         # '''1、售货员输入商品编号
#         #         2、计算机进行查找，并将找到的结果返回给售货员
#         #         3、如果商品存在，这输入商品数量给计算机，计算机对商品数量进行修改
#         #         4、如果商品不存在，这售货员输入单价、数量给计算机，计算机对商品进行添加'''
#         result = self.seller.seller_addgood(self)
#         if isinstance(result, Good):
#             self.goods.append(result)
#             print('新增成功')
#         else:
#             good = result[0]
#             count = result[-1]
#             good.count = good.count + count
#             print('数量添加成功')
#
#     def searchgood(self, barcode):
#         for good in self.goods:
#             if good.barcode == barcode:
#                 return good
#
#     def reducegood(self):
#         result = self.seller.seller_sellgood(self)
#         if result is not None:
#             good = result[0]
#             count = result[-1]
#             if count >= good.count:
#                 print('出售大于库存，卖出当前库存{}'.format(good.count))
#             else:
#                 good.count = good.count - count
#                 print('卖出{}，还剩{}'.format(good.count, count))
#
#     def editgood(self):
#         result = self.seller.seller_editgood(self)
#         if result is not None:
#             good = result[0]
#             price = result[-1]
#             good.price = price
#             print('修改成功')
#
#
#     def showallinfo(self):
#         pass
#
#     def poweron(self, seller):
#         self.seller = seller
#         while True:
#             n = self.showmenue()
#             if n == 1:
#                 self.addgood()
#             elif n == 2:
#                 self.reducegood()
#             elif n == 3:
#                 self.editgood()
#             elif n == 4:
#                 for good in self.goods:
#                     print(good)
#             elif n == 5:
#                 break
#
#
# if __name__ == '__main__':
#     zhangsan = People('张三')
#     computer1 = Computer()
#     computer1.poweron(zhangsan)
import math
# while 1:
#     n = int(input('输入一个数'))
#     print('%d =' % n, end=' ')
#     while n > 1:
#         for i in range(2, n +1):
#             if n % i == 0:
#                 n = int(n / i)
#                 if n == 1:
#                     print('%d' % i, end='')
#                 else:
#                     print('%d' % i, end='*')
#                 break
#     print()

# a = 0
# for i in range(1, 101):
#     for j in range(1, i):
#         if i % j == 0:
#             a = a + j
#     if i == a:
#         print(i)
# 1、 思考：将四个工作表中的内容，合并到一个excel中？？？
# 2、如何将一个文件夹下的所有excel合并到一个excel
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def __str__(self):
#         return self.name + '' + str(self.age)
#
#
# s1 = Student('zhangsan', 10)
# s2 =Student('lisi', 10)
# s3 =Student('wanglaowu', 20)
# s4 = Student('lisi', 5)
# l = [s1, s2, s3, s4]
#
# newl = sorted(l, key=lambda x: (x.name, x.age))
#
# for stu in newl:
#     print(stu)
# a = 3
# b = 2
# c =1
# print(a > b)
# print((a > b ) == c)
# print(b + c < a)
# # print(c = a > b)
# from dis import dis
#
# def money(a):
#     money1 = 199
#     money1 = 199 - 2.5 * a - 5 * 5
#     print(money1)
#
#
# dis(money)
# def gen1():
#     l = list()
#     for i in range(10):
#         l.append(i)
#     return l
# print(gen1())
# from math import hypot
# class vector:
#     def __init__(self, x=0, y = 0):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return 'vector({}{})'.format(self.x, self.y)
#
#     def __abs__(self):
#         return hypot(abs(self))

# for i in range(1, 256):
#     if str(i**2)==str(i**2)[::-1]:
#         print(i)
from threading import Thread
from threading import Lock
num  = 0
#实际上面cpu是执行了 counts*10的次数
#操作系统会随时把你的程序切换出来，保证你的系统不卡
# 1、执行次数过多
# 2、执行时间过长
# counts = 10000000
# lock = Lock()
# def add():
#     global num
#     global counts
#     for i in range(counts):
#         lock.acquire()
#         num += 1
#         lock.release()
# def minus():
#     global num
#     global counts
#     for i in range(counts):
#         lock.acquire()
#         num -= 1
#         lock.release()
#
# def mians():
#     f1 = Thread(target=add)
#     f2 = Thread(target=minus)
#     f1.start()
#     f2.start()
#     f1.join()
#     f2.join()
#

# add()
# minus()
# print(num)
# if __name__ == "__main__":
#     mians()
#     print(num)

# 查看字节码
# import dis
# num = 0
# def add():
#     global num
#     num += 1
# print(dis.dis(add))
# # 源代码
# from concurrent.futures import ThreadPoolExecutor
# from threading import Thread
# from threading import Lock, RLock
# #偏函数
# from functools import partial
# from  concurrent.futures import as_completed
# import asyncio
# lock = RLock()
# #初始化线程 并且规定线程数量
# num = 0
# counts = 1000000
# def add():
#     global num
#     global counts
#     for i in range(counts):
#         lock.acquire()
#         num += 1
#         lock.release()
# def minus():
#     global num
#     global counts
#     for i in range(counts):
#         lock.acquire()
#         num -= 1
#         lock.release()
#
# pools =ThreadPoolExecutor(max_workers=20)
# function_list =[add, minus]
# pool =list()
# for i in function_list:
#     pool.append(pools.submit(i))
# for i in as_completed(pool):
#     i.result()
# #注意传递参数和普通的不一样 submit接收不了两个参数
# print(num)
#
# import socket
#
# def address(addr):
#     ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     ss.bind(addr)
#     ss.listen()
# for i in range(1000, 10000):
#     if str(i) == str(i * 9)[::-1]:
#         print(i)


# E = []
# G = []
#
# for i in range(2, 61):
#     b = 0
#     for j in range(1, i):
#         if i % j == 0:
#             b = b + j
#     if b > i:
#         G.append(i)
#     elif b == i:
#         E.append(i)
# print(E, G)


# try:
#     while 1:
#         dict_sent = {}
#         string = input()
#         string = string.replace(',',' ').replace('.', ' ')
#         string = string.lower()
#         string = string.split()
#         string.sort()
#         for item in string:
#             dict_sent[item] = dict_sent.get(item, 0)+ 1
#         dict_sent = sorted(dict_sent.item())
#         for i in dict_sent:
#             print('%s:%s' % i)
# except:
#     pass



from collections import namedtuple
Card = namedtuple('Card',['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)]+ list('JQKA')
    suits = 'spades diamods clubs hearts'.split()
    def __init__(self):
       self.card = [Card(rank, suit)for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return  len(self.card)
    def __getitem__(self, position):
        return  self.card[position]

beer =  FrenchDeck()
print(len(beer))
print(beer[0])
from math import hypot

class Voctor:
    def __init__(self, x=0 , y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Vector{}{}'.format(self.x, self.y)
    def __abs__(self):
        return hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Voctor(x, y)
    def __mul__(self, other):
        return Voctor(self.x*other.x, self.y*other.y)


v1 = Voctor(0,1)
v2 = Voctor(2,3)

v3 = v1*v2
print(v3)
