# import socket
# import threading
#
# conn_lists =[]
# def handle_conn(conn, addr):
#     while 1:
#         msg = conn.recv(1024)
#         return_msg = '地址在{}的用户说{}'.format(addr, msg.decode())
#         for conn in conn_lists:
#             conn.send(return_msg.encode())
#
# def conn_server(addr):
#     ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     ss.bind(addr)
#     ss.listen()
#     print('服务器已经启动')
#     while 1:
#         conn, addr = ss.accept()
#         conn_lists.append(conn)
#         print('链接已经进来了,地址{}'.format(addr))
#         handle = threading.Thread(target=handle_conn, args=(conn, addr))
#         handle.start()
#
# if __name__ == '__main__':
#
#     addr = ('127.0.0.1', 9519)
#     conn_server(addr)
#
# import socket
# import subprocess
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# add = ('127.0.0.1', 16183)
# server.bind(add)
# server.listen(5)
#
# while 1:
#     print('waiting....')
#     conn, addr = server.accept()
#     print('-->conn:', conn)
#     print('--addr:',addr)
#     print('got it....')
#
#
#     while 1:
#         try:
#             cmd = conn.recv(1024)
#             res = subprocess.Popen(cmd.decode('utf-8'), shell= True,
#                                    stdout= subprocess.PIPE,
#                                    stderr= subprocess.PIPE)
#
#             conn.send(res.stdout.read())
#             conn.send(res.stderr.read())
#         except Exception:
#             break
#     conn.close()
#
# # set
# import socket
# from threading import RLock
# from concurrent.futures import ThreadPoolExecutor
# from functools import partial
# conn_lists = list()
# lock = RLock()
# pools = ThreadPoolExecutor(max_workers=20)
#
# def handle_conn(conn, addr):
#     while 1:
#         msg = conn.recv(65535)
#         return_msg = '地址在{}的用户说:{}'.format(addr, msg.decode())
#         lock.acquire()
#         for conn in conn_lists:
#             conn.send(return_msg.encode())
#         lock.release()
#
# def conn_server(addr):
#     ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     ss.bind(addr)
#     ss.listen()
#     print('服务器已经启动')
#     # 会阻塞 等待链接进来
#
#     while 1:
#         conn, addr = ss.accept()
#         conn_lists.append(conn)
#         print('新来链接,地址{}'.format(addr))
#         pools.submit(partial(handle_conn,conn,addr))
#
# if __name__ == "__main__":
#     addr = ("127.0.0.1", 9520)
#     conn_server(addr)






import pymysql
# import pymysql.cursors
#
# connection = pymysql.connect(host = '127.0.0.1',
#                              user = 'root',
#                              password = 'wxl4174858',
#                              db = 'wang',
#                              charset ='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)
#
# with connection.cursor() as cursor:
#     sql = 'SELECT * FROM `company`'
#     cursor.execute(sql)
#     result = cursor.fetchall()
#
# print(result)
# import pymysql
# import pymysql.cursors
#
#
# def my(sql):
#     # Connect to the database
#     connection = pymysql.connect(host='10.2.1.78',
#                                  user='p1901',
#                                  password='123456',
#                                  db='p1901_leetcode',
#                                  charset='utf8mb4',
#                                  cursorclass=pymysql.cursors.DictCursor)
#
#     with connection.cursor() as cursor:
#         # Read a single record
#         # sql = "SELECT * FROM `employee`"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#     return result
#
#
# if __name__ == "__main__":
#     sql = "select name from `employee`"
#     res = my(sql)
#     print(res)
#
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:wxl4174858@127.0.0.1/wang', echo=True)
Base = declarative_base()

from  sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'al_users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    fullname = Column(String(255))
    nickname = Column(String(200))

# Base.metadata.create_all(engine)
from  sqlalchemy.orm import  sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

ed_user = User(name = '小泽玛利亚', fullname ='小泽玛利亚', nickname = 'endjkl')

session.add(ed_user)
session.commit()
