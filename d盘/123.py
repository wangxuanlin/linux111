# a =[1, 2,3,4,5,6,6,3,4,5]
# a.sort()
# print(a)
# a ={1:23, 5:12, 2:12, 6:13}
# sorted(a, reverse= False)
# print(sorted(a, reverse= False))
# fruits = ['grape', 'raspberry', 'apple', 'banana']
# sorted(fruits)
# print(sorted(fruits))
# print(sorted(fruits, reverse=True))
# print(sorted(fruits, key=len))
# print(sorted(fruits, key=len, reverse=True))
# print(fruits.sort())
# print(fruits)
# print(sorted(fruits,key= str))
#
# #
# #
# import bisect
# import sys
# HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
# NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
# ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'
# def demo(bisect_fn):
#     for needle in reversed(NEEDLES):
#         position = bisect_fn(HAYSTACK, needle)
#         offset = position*'  |'
#         print(ROW_FMT.format(needle, position, offset))
#
#
# if __name__ == '__main__':
#     if sys.argv[-1] == 'left':
#         bisect_fn = bisect.bisect_left
#     else:
#         bisect_fn = bisect.bisect
#     print('DEMO:', bisect_fn.__name__)
#     print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
#     demo(bisect_fn)
# #
# #
# def grade(score, breakpoints=[60, 70, 80, 90], grades='fdcba'):
#     i = bisect.bisect(breakpoints, score)
#     return grades[i]
#
# print([grade(socre) for  socre in [33, 99, 70, 89, 90, 100]])
#
#
# import  random
# size = 7
# my_list = []
# for i in range(size):
#     new_item = random.randrange(size*2)
#     bisect.insort(my_list,new_item)
#     print('%2d  ->'%new_item, my_list)
#
# random.seed(1729)
# print(random.random())

# from array import array
# from random import random
# float = array('d', (random() for i in range(10**7)))
# print(float[-1])
# fp = open('floats.bin', 'wb')
# float.tofile(fp)
# fp.close()
# float2 = array('d')
# fp = open('floats.bin', 'rb')
# float2.fromfile(fp, 10**7)
# fp.close()
# print(float2[-1])
# print(float2==float)
# from collections.abc import Mapping
#
# my_dict = {}
# isinstance(my_dict, Mapping)
# print(isinstance(my_dict, Mapping))

tt = (1,2,(30,40))
print(hash(tt))
tf = (1, 2, frozenset((30, 40)))
print(hash(tf))
#
#
# a = dict(one = 1 , two = 2, three= 3)
# b = {'one': 1, 'two':2, 'three': 3}
# c = dict(zip(['one', 'two', 'three'],[1,2,3]))
# d = dict([('two', 2), ('one',1 ), ('three', 3)])
# e = dict({'three': 3, 'one': 1, 'two': 2})
# print(a == b == c == d == e)

# import  collections
#
# card = collections.namedtuple('card1', ['rank', 'suit'])
#
# class Frenchdeck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits ='♠️ ♥️ ♦️ ♣️'.split()
#
#     def __init__(self):
#         self.cards = [card(rank, suit) for suit in self.suits
#                       for rank in self.ranks]
#
#     def __len__(self):
#         return  len(self.cards)
#
#     def __getitem__(self, position):
#         return self.cards[position]
#
# a = Frenchdeck()
# print(tuple(a))

# def fun(n,a):
#     if n > 0:
#         a = a+ n
#         n = n - 1
#         return fun(n,a)
#     print(a)
#
#
#
#
#
#
#
#
# print(fun(100,0))

# def fun(n):
#     if n ==1 or n ==2:
#         return 1
#     else:
#         return fun(n -1) + fun(n-2)
#
# print(fun(5))
#
#
# list1 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# res = [
#     [7,4,1],
#     [8,5,2],
#     [9,6,3]
# ]
#
# new_list = []
#
# for a in range(len(list1)):
#     new_list.append([])
#
# for i in reversed(list1):
#     n = 1
#     for j in i:
#         new_list[n-1].append(j)
#         n += 1
#
# for i in new_list:
#     print(i)
#
#
#
#
#
#
# DIAL_CODES = [
#              (86, 'China'),
#              (91, 'India'),
#              (1, 'United States'),
#              (62, 'Indonesia'),
#              (55, 'Brazil'),
#              (92, 'Pakistan'),
#              (880, 'Bangladesh'),
#              (234, 'Nigeria'),
#              (7, 'Russia'),
#              (81, 'Japan'),
# ]
# d1 = dict(DIAL_CODES)
# print('d1:', d1.keys())
# d2 = dict(sorted(DIAL_CODES))
# print('d2:', d2.keys())
# d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))
# print('d3:', d3.keys())
# assert d1 == d2 and d2 == d3

from random import random
import time
methods = [dict.fromkeys,frozenset, list]
for m in methods:
    base_num = 1000
    nums = [base_num*10**i for i in range(5)]
    for j in nums:
        needles = [random() for __ in range(1000)]
        haystack = m(dict.fromkeys(random() for __ in range(j)))
        now = time.time()
        found = 0
        for n in needles:
            if n in haystack:
                found +=1
        last_time = time.time() - now
        print(last_time)
    print('-----------{}'.format('time'))
