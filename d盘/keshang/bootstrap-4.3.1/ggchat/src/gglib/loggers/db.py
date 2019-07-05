from  abc import ABC


from gglib.logger import Baselogger
import pymysql


class MySQLLOgger(Baselogger):
  def __init__(self, level, fmt, host, port, password, db, user):
    super().__init__(level, fmt)
    self.mysql_connection = pymysql.connect(host =host,
                                            port = port,
                                            password = password,
                                            user = user,
                                            database =db

    )

  def debug(self, sender, *args):
    assert isinstance(self.mysql_connection, pymysql.Connection)
    pass
