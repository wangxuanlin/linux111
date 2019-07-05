IO = {
  "BIND_ADDRESS": ('127.0.0.1', 1213),
  'SZ_SEND_BUFFER': 0xFFFF,
  'SZ_RECV_BUFFER': 0xFFFF,
  'SOCKET_KEEPALIVE': (5, 5)
}

NUM_WORKERS = 10

DATABSE = {
  'NAME': 'mysql',
  'OPTIONS': {
    "HOST": "",
    "PORT": "",
    "USER": "",
    "PASSWORD": "",
    "OB": "",
  }
}
LOGGER = {
  'BACKEND': 'gglib.loggers.file.FileHandler',
  'OPTIONS': {'file':'ggchat.log'},
  'LEVEL': 'warn',
  "FORMAT": "",

}
CACHE = {
  'BACKEND': "",
  'OPTIONS': {

  }
}

MIDDLEWARES = [

]
