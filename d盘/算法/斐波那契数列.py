def fib_recur(n):
    assert n >= 0, 'n>0'
    if n <= 1:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)


for i in range(1, 20):
    print(fib_recur(i), end='')


def fib_loop(n):
    a, b = 0, 1
    for i in range(n + 1):
        a, b = b, a + b
        return a


for i in range(20):
    print(fib_recur(i), end='')


def fib_loop_while(max):
    a, b = 0, 1
    while max > 0:
        a, b = b, a + b
        max -= 1
        yield a


for i in fib_loop_while(10):
    print(i)


class Fibonacci(object):
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.a = 0
        self.b = 1

    def __next__(self):
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    fib = Fibonacci(15)
    for num in fib:
        print(num)



