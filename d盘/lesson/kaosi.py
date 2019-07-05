
'''
9、编写一个函数，它接收一个字符串并返回一个删除了所有元音的新字符串。
例如， 字符串'This website for for losers LOL'，会变成'Ths wbst fr fr lsrs LL'
'''

def disemvowe(string):
    a = list(string)
    i = 0
    while i < len(a):
        if a[i] in 'aeiouAEIOU':
            a.remove(a[i])
            i = i - 1
        i += 1
    print(''.join(a))

disemvowe('This website for for losers LOL')




# '''
# 创建一个学生类（包涵 姓名、 性别、 年龄、 分数），
# 创建一个老师类（包含姓名、性别、 年龄、 课时费）
#
# '''
l = []

class Human:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


class Student(Human):
    def __init__(self, name, gender, age, grade):
        self.grade = grade
        super().__init__(name, gender, age)

    def students(self):
        s = {'学生名字': self.name, '性别': self.gender, '年龄': self.age, '成绩': self.grade}
        l.append(s)
        print('添加成功')

class Teacher(Human):
    def __init__(self, name, gender, age, fee):
        self.fee = fee
        super().__init__(name, gender, age)

    def terchers(self):
        t = {'老师名字': self.name, '性别': self.gender, '年龄': self.age, '课时费': self.fee}
        l.append(t)
        print('添加成功')

def list(l):
    print(l)
    a = 0
    b = 0
    for i in l:
        for key in i:
            if key == '成绩':
                a = a + i[key]
            elif key == '课时费':
                b = b + i[key]

    print('学生总成绩{},老师总费用{}'.format(a, b))


lisi = Student('lisi', 'nan', 10, 90)
lisi.students()
wang = Student('wangwu', 'nan', 10, 80)
wang.students()
xiaoming = Student('xiaoming', 'nan', 10, 70)
xiaoming.students()
xiaoyang = Student('xiaoyang', 'nan', 10, 80)
xiaoyang.students()
xiaohong = Student('xiaohong', 'nv', 10, 100)
xiaohong.students()
zz = Teacher('zz', 'nan', 30, 10)
zz.terchers()
aa = Teacher('aa', 'nan', 30, 20)
aa.terchers()
xx = Teacher('zz', 'nv', 25, 10)
xx.terchers()
dd = Teacher('dd', 'nan', 26, 10)
dd.terchers()
cc = Teacher('cc', 'nv', 26, 10)
cc.terchers()
list(l)

'''
有一只猴子， 一天，摘了很多的桃子回家， 口馋了，
当即吃了一半， 还不解馋，又多吃了一个；第二天，
吃剩下的桃子的一半，还不过瘾，又多吃了以一个，
以后每天都吃前一天的剩下的一半还多一个，到了第10天再
吃时就剩下一个桃子了。

'''
i = 0
n = 0
while i < 10:
    i += 1
    n = n * 2 + 1
print(n)





class Human:
    def __init__(self, name, number, money = 0):
        self.name = name
        self.number = number
        self.money = money

    def __str__(self):
        return '名字：{}， 电话：{}， 金额：{}'.format(self.name, self.number, self.money)


class Worker:
    def __init__(self, name):
        self.name = name

    def inputmenue(self):
        return int(input('选择菜单'))

    def addhuman(self, computer):
        number = int(input('输入电话号码'))
        human = computer.seacher(number)
        if human is None:
            name = input('输入名字')
            money = int(input('输入金额'))
            human1 = Human(name, number, money)
            return human1

    def removehuman(self, computer):
        number = int(input('输入电话号码'))
        human = computer.seacher(number)
        if human is not None:
            return human

    def xiugaimoney(self, computer):
        number = int(input('输入电话号码'))
        human = computer.seacher(number)
        if human is not None:
            money = int(input('输入金额'))
            return human, money


class Computer:
    l = []

    def __init__(self):
        self.worker = None

    def showmenue(self):
        print('1、添加卡片')
        print('2、删除卡片')
        print('3、充值')
        print('4、查看卡片')
        print('5、退出')
        n = self.worker.inputmenue()
        return n

    def seacher(self, number):
        for i in self.l:
            if i.number == number:
                return i

    def add(self):
        result = self.worker.addhuman(self)
        if result is not None:
            self.l.append(result)
            print('制作成功')

    def remove(self):
        result = self.worker.removehuman(self)
        if result is not None:
            human = result
            self.l.remove(human)

    def xiugai(self):
        result = self.worker.xiugaimoney(self)
        if result is not None:
            human = result[0]
            money = result[-1]
            human.money = human.money + money
            print('修改成功')

    def poweron(self, worker):
        self.worker = worker
        while True:
            n = self.showmenue()
            if n == 1:
                self.add()
            elif n == 2:
                self.remove()
            elif n == 3:
                self.xiugai()
            elif n == 4:
                for card in self.l:
                    print(card)
            elif n == 5:
                break


if __name__ == '__main__':

    zhangsan = Worker('张三')
    computer1 = Computer()
    computer1.poweron(zhangsan)