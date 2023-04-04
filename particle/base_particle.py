from google.protobuf.json_format import MessageToJson
from particle.protos.particle import Particle


class BaseParticle:
    def __init__(self, data: Particle):
        self.json = MessageToJson(data)
        self.pb = data.SerializeToString()
