import traceback
from gglib import logger
from gglib.middieware import process_packet
from gglib.utils import import_attr
from gglib.packet import PacketRejected


def handle(session, packet):
  try:
    process_packet(session, packet, incoming=True)
  except PacketRejected:
    return

  command = packet['command']
  handler = import_attr('gglib.handlers.'+command+ '.handle')
  handle(session,packet)
