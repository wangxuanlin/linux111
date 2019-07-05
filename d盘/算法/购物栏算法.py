# def combine(s, n):
#     def _iterator(collector, s, i, c, n, data=None):
#         if c >= n:
#             collector.append(list(data))
#             return
#
#         for x in range(i, len(s)):
#             data.append(s[x])
#             _iterator(collector, s, x + 1, c + 1, n, data)
#             data.pop()
#
#     data_set = []
#     chars = []
#     _iterator(data_set, s, 0, 0, n, chars)
#     return data_set
# s = [1,2,3,4,5,6,7,8.9,0]
# n = 4
# print(combine(s,n))
import random

products = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']

count = 200


def get_transaction(n=8):
    pds = []
    p = list(products)
    for i in range(n):
        x = p[random.randint(0, len(p) -1)]
        p.remove(x)
        pds.append(x)
    return pds


with open("./transaction.txt", "w") as fp:
    for i in range(count):
        pds = get_transaction()
        fp.write("T: {}\n".format(",".join(pds)))

if __name__ == '__main__':
    get_transaction(8)