# pcckage: wxl
# func. py
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
# if __name__ =='__main__':
#     number(5)
#上课代码
# 一种方式：import  路径
#
#精确引入： （）
# def showmen():
#     print('1、输入语文成绩:')
#     print('2、输入数学成绩:')
#     print('3、输入英语成绩:')
#     print('4、显示所有成绩')
#     print('5、退出')
#     print('6、修改语文下的某个人成绩')
#     print('7、修改数学下的某个人成绩')
#     print('8、修改英语下的某个人成绩')
#     menu = int(input('请选择:'))
#     return menu
# def calscore(menu, s):
#     keys = tuple(s.keys())
#     key = keys[menu - 1]
#     name = input('姓名')
#     score = int(input('请输入新增的{}成绩:'.format(key)))
#     student = {'姓名': name, '成绩': score}
#     s[key].append(student)
#     print('{}学科，成绩如下'.format(key))
#     for stu in s[key]:
#         print(stu['成绩'],end = ' ')
#     print()
# def name(menu, s):
#     keys = tuple(s.keys())
#     key = keys[menu - 6]
#     name1 = input('姓名')
#     for stu in s[key]:
#         if stu['姓名'] == name1:
#             score1 = int(input('输入修改成绩'))
#             # studentt ={'姓名': name1, '成绩': score1}
#             # s[key].append(studentt)
#             stu['成绩'] = score1
#             break
#         else:
#             print('查无此人')
# def money(n):
#     save = int(input('输入存入的金额：'))
#     n = save + n
#     print('卡内的金额：{}'.format(n))
#     return n
# if __name__ =='__main__':
#     money(100)
# def money1(n):
#     numberpen = int(input('输入笔购买的数量：'))
#     numbercup =  int(input('输入杯子购买的数量：'))
#     n  = n - numbercup * 5 - numberpen *2.5
#     print(n)
#     return n
# if __name__ =='__main__':
#     money1(199)
# def chengji(s):
#     chinese = int(input('输入语文成绩：'))
#     englis = int(input('输入英语成绩'))
#     a = {'语文成绩': chinese,'英语成绩': englis}
#     chengji = chinese + englis
#     ping = chengji / 2
#     s.append(a)
#     print(s, '\n', '成绩：', chengji, '平均成绩：', ping)
#     return s
# if __name__ =='__main__':
#     s = []
#     chengji(s)
#
# def s(a):
#     l = a * 4
#     s = a ** 2
#     print(l, s)
# if __name__ =='__main__':
#     s(4)
# def yuan(radius):
#     import math
#     s = radius ** 2 * math.pi
#     l = 2 * radius* math.pi
#     print('圆面积{}, 圆周长{}, 圆半径{}'.format(s, l, radius))
#
# if __name__ =='__main__':
#     yuan(3.5)
# def year(n):
#     if n % 4 == 0 and n % 100 != 0:
#         print(n, '是闰年')
#     else:
#         print(n, '不是闰年')
# if __name__ =='__main__':
#     year(2012)
# def number(n):
#     if n % 2 == 0:
#         print(n, '是偶数')
# if __name__ =='__main__':
#     number(8)