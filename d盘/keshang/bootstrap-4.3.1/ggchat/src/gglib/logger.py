from gglib.settings import LOGGER

__all__ = ['LOG_LEVEL', 'debug', 'info', "warn", 'error']
LOG_LEVEL = {
  'debug': 1,
  "info": 2,
  "warn": 3,
  "error": 4
}


class Baselogger:
  def __init__(self, level, fmt='', **kwargs):
    self.level = level
    self.fmt = fmt

  def info(self, sender, *args):
    raise NotImplementedError

  def debug(self, sender, *args):
    raise NotImplementedError

  def warn(self, sender, *args):
    raise NotImplementedError

  def error(self, sender, *args):
    raise NotImplementedError


import importlib
import pdb

# pdb.set_trace()

_backend = LOGGER['BACKEND']
_medule, _cls = _backend.rsplit('.', 1)
_logger_module = importlib.import_module(_medule)
_logger_cls = getattr(_logger_module, _cls)
if not issubclass(_logger_cls, Baselogger):
  raise ImportError("The {} class must be subclass of baselogger".format(_logger_cls.__name__))

_logger_handler = _logger_cls(LOGGER['LEVEL'], LOGGER['FORMAT'], **LOGGER['OPTIONS'])
debug = _logger_handler.debug
info = _logger_handler.info
warn = _logger_handler.warn
error = _logger_handler.error

if __name__ == '__main__':
  info(__package__, 'an error occurred.')
  debug(__package__, 'a = 3')


import io
