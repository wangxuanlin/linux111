import traceback
from gglib import logger
from gglib.settings import MIDDLEWARES
from gglib.utils import import_attr

_middleware_set = []

for m in MIDDLEWARES:
  mw_cls = import_attr(m)
  mw_instanc = mw_cls
  if not hasattr(mw_instanc, 'process_incoming'):
    raise Exception('Invalid middleware')
  if not hasattr(mw_instanc, 'process_outgoing'):
    raise Exception('Invalid middleware')

  _middleware_set.append(mw_instanc)


def process_packet(session, packet, incoming=True):
  for mw in _middleware_set:
    try:
      mw.process_packet(session, packet, incoming)
    except Exception as e:
      traceback.print_exc()
      logger.error(e)
