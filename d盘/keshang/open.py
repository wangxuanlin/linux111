import os

class File:
    def __init__(self, path):
        self.path = os.open(path,os.O_RDONLY)

    def read(self, size):
        return os.read(self.path, size)

    def close(self):
        os.close(self.path)


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()




def open(path):
    return File(path)

try:
    with open('./open.py') as path:
        raise  Exception("with statement error")
        print(path.read(10))
except Exception as er:
    import traceback
    traceback.print_exc()
