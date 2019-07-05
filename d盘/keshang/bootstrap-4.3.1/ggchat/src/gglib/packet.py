class Packet:
  def __setitem__(self, key, value):
    self.__dict__[key] = value

  def __getitem__(self, item):
    return self.__dict__[item]

  def __bytes__(self):
    import json
    json_data = json.dumps(self.__dict__)
    return json_data.encode('utf-8')

class PacketRejected(BaseException):
  pass
