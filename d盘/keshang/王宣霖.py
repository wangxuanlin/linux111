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
# i = ['12', '13', '33', '34']
# k = 0
# while k < len(i):
#     if '1' in i[0]:
#         i.remove(i[0])
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
# list1 = ['a', 'a', 'a','b', 'b', 'c', 'c', 'c', 'c', 'd', 'd']
# print('{}a,{}b, {}c, {}d'.format(list1.count('a'), list1.count('b'), list1.count('c'), list1.count('d')))











