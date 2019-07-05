# class _HttpClient:
#     _sharedInstanc = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._sharedInstanc is None:
#             cls._sharedInstanc = super().__new__(cls, *args, **kwargs)
#         return cls._sharedInstanc
#
#     def get(self, url):
#         pass
#
#     def post(self, url):
#         pass
#
#
# x1 = _HttpClient()
# x2 = _HttpClient()
# x3 = _HttpClient()
#
#
# print(x1 is x2, id(x1), id(x2))
# print(x2 is x3, id(x2), id(x3))


def wen(a):
    def up(*args):
        mas = a(*args)
        mas = mas.capitalize()
        return mas

    return up


@wen
def f(a):
    return a


if __name__ == '__main__':
    print(f("a"))
