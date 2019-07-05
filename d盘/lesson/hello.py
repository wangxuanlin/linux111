
name = "zhangsan"
age = 10
lesson = 'python'
print('{}{}{}'.format(name, age, lesson))




exit()
# 注释
# IDE

# 1 + 1

print(1 + 1)
print(234 + 123)
print(234 + 123 + 2)
print(234 + 123 + 1)

# 变量: 在程序执行过程中，其值会改变的量
n = 234 + 123
print(n)
n = 10
print(n)

# 注意事项：
# 变量名命名规则：
# 1、由字母、数字、下划线组成
#   且不能以数字作为开头
#   尽量只在特殊时候将下划线作为开头
# 2、不跟系统的名字重名
# 3、见名知意,首字母小写（驼峰原则...）
# 4、变量，必须先定义，后使用

# 1a = 10  # 错误的，数字不能开头
# print = 1  # 错误的，print是系统的内置函数名
print(1)  # 1(1)

# *a = 10

age = 10
print(age)

# 数据： 数据类型？？？
print(type(age))
print(type(10))

# int 整型： 十进制 、二进制、八进制、十六进制
# float 小数（浮点数）
# str  字符串
# 。。。

print(type(1.1))
a = 10
a = 1.1

print(type('hello'))

# int
# 操作：使用运算符
# + - * /
a = 10
b = 20

print(a + b, 10 + 20)
print(3 / 2)

# **  //
print(3 // 2)
print(3 ** 2)  # 9

# print('hello' + 1)  # str不能和int相加，需要转换
print('hell0' * 10)  # str * int 代表重复次数

print('=' * 20, '华丽的分割线')

# %  (特例：作为了解即可， 针对负数)
print(5 % 2)

# 基础题：
# 1、定义一个变量。用来存储我卡上有100块钱，到银行存了1000块钱，打印输出现在我卡上多少钱
# 开心 = '😊'
# print(开心)
money = 100
money = money + 1000
print(money)

# 2、班费有199块钱，买了30支笔，每支笔2.5元，买了5个杯子，5元一个，打印输出班费还剩多少钱？
money = 199
money = money - 30 * 2.5
money = money - 5 * 5
print(money)

# 3、使用运算符，求19的个位打印输出；求29的十位数字打印输出；189的每位数字输出；
#
print(19 % 10)
print(29 // 10)
print(189 // 100, 189 // 10 % 10)
print(189 % 100 // 10)
print(189 % 10)

# 提高题：
# 4、已知一个学生两科成绩：语文90；英语66；求该学生总成绩和平均成绩
chinese = 90
english = 66
s = chinese + english
avg = s / 2
print('总成绩:', s, '平均成绩:', avg)

# 5、已知正方形边长为4，求正方形周长和面积
a = 4
print('周长：', a * 4)
print('面积:', a ** 2)

# 6、已知一个圆半径为3.5，声明一个变量名为radius存储该圆半径，要求输出该圆的半径、周长和面积
radius = 3.5
pi = 3.14
print('圆周长:', 2 * pi * radius)
print('圆面积:', pi * radius * radius)
