import socket
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('127.0.0.1', 9000))
ss.listen()
conn, addr = ss.accept()
msg = conn.recv(1024)
print(msg)