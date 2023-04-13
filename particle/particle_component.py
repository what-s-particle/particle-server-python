from google.protobuf.json_format import MessageToJson
from particle.protos.particle import Particle


class ParticleComponent:
    def __init__(self, data: Particle):
        self.data = data
        self.json = MessageToJson(data)
        self.pb = data.SerializeToString()
