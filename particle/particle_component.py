import uuid
from google.protobuf.json_format import MessageToJson
from particle.protos.particle import Particle


class ParticleWrapper:
    def __init__(self, data: Particle):
        if not data.id:
            data.id = str(uuid.uuid4())

        self.data = data
        self.json = MessageToJson(data)
        self.pb = data.SerializeToString()
