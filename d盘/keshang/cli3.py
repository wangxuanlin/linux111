# import time
# from threading  import Thread
#
# def test1():
#     time.sleep(6)
#     print('结束')
#
# def test2():
#     time.sleep(4)
#     print('结束1')
#
#
#
# t1= Thread(target= test1)
# t1.start()
# test2()
#
# from math import hypot

# class Vector:
#     def __init__(self, ):

# import time
# import threading
# def lo1():
#     time.sleep(4)
#     print('<-----lo1------>')
#
#
# def lo2():
#     time.sleep(2)
#     print('<------lo2------>')
#
# def main():
#     t1 = time.time()
#     fi = threading.Thread(target= lo1)
#     f2 = threading.Thread(target=lo2)
#     fi.start()
#     f2.start()
#     fi.join()
#     f2.join()
#     t2 = time.time()
#     print('total time: {}'.format(t2 - t1))
#
# if __name__ == '__main__':
#     main()


import threading
a = 0
def add():
    global a
    for i in range(100000):
        a += 1

def minus():
    global  a
    for i in range(1000000):
        a -= 1
def main():
    threading.Thread(target=add).start()
    threading.Thread(target=minus).start()


if __name__ == '__main__':
    main()
    print(a)

