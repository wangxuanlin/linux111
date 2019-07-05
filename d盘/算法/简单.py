class SQlist:
    def __init__(self, lis=None):
        self.r = lis

    def swap(self, i, j):
        temp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = temp

    def select_sort(self):
        lis = self.r
        length = len(self.r)
        for i in range(length):
            minimum = i
            for j in range(i + 1, length):
                if lis[minimum] > lis[j]:
                    minimum = j
            if i != minimum:
                self.swap(i, minimum)

    def __str__(self):
        ret = ""

        for i in self.r:
            ret += " %s" % i
        return ret


if __name__ == '__main__':
    sqlist = SQlist([4, 1, 2, 3, 5, 8, 4, 6, 1, 0])
    sqlist.select_sort()
    print(sqlist)
