import datetime
import sys
from gglib.logger import Baselogger, LOG_LEVEL


class FileHandler(Baselogger):
  def __init__(self, level, fmt, file = None):
    super().__init__(level, fmt)
    if not file:
      self._file = sys.stdout
    else:
      self._file = open(file, 'w')

  def _output_log(self, level, sender, message):
    if LOG_LEVEL[level] >= LOG_LEVEL[self.level]:
      self._file.write('()<()>[()]:{}\n'.format(datetime.datetime.now().strftime("%Y/%m/%d %H:%m:%S"),
                                                sender,
                                                level,
                                                message))



  def debug(self, sender, *args):
    self._output_log('debug', sender,*args)


  def info(self, sender, *args):
    self._output_log('info', sender, *args)


  def warn(self, sender, *args):
    self._output_log("warm", sender, *args)



  def error(self, sender, *args):
    self._output_log('error', sender, *args)

