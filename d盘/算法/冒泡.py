class SQList:
    def __init__(self, lis=None):
        self.r = lis

    def swap(self, i, j):
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp

    def bubble_sort_simple(self):
        lis = self.r
        length = len(self.r)
        for i in range(length):
            for j in range(i + 1, length):
                if lis[i] > lis[j]:
                    self.swap(j, j + 1)
                    j -= 1

    def bubble_sort(self):
        lis = self.r
        length = len(self.r)
        for i in range(length):
            j = length - 2
            while j >= i:
                if lis[j] > lis[j + 1]:
                    self.swap(j, j + 1)
                j -= 1

    def bubble_sort_advance(self):
        lis = self.r
        length = len(self.r)
        flag = True
        i = 0
        while i < length and flag:
            flag = False
            j = length - 2
            while j >= i:
                if lis[j] > lis(j + 1):
                    self .swap(j, j + 1)
                    flag = True

                j -= 1
            i += 1



    def __str__(self):
        ret = ''
        for i in self.r:
            ret += "%s" %i
        return  ret

if __name__ == '__main__':
    sqlist = SQList([2,3,1,4,6,3,2,4,5])
    sqlist.bubble_sort()
    print(sqlist)
