import importlib
import random

def import_attr(path):
  module, attr = path.rsplit('.',1)
  module = importlib.import_module(module)
  return getattr(module,attr)

def get_random_str(char_set=None,k=5):
  if not char_set:
    char_set = 'abcdefghijklmnopqrstuvwxyz'
    char_set += char_set.upper()
    char_set += '1234567890'



  return ''.join(random.choice(char_set, k=k))
