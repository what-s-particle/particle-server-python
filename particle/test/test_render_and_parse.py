from unittest import TestCase

from particle.protos.particle import Particle
from particle.scripts.parsers import ProtobufParser
from particle.scripts.renderers import ProtobufRenderer


class ProtobufRenderAndParserTestCase(TestCase):

    def test_render_and_parse(self):
        obj = {
            "name": "Test Name",
            "id": 42,
            "email": "testname@test.c1om",
        }

        context = {"protobuf_cls": particle.Person}

        renderer = ProtobufRenderer()
        content = renderer.render(obj, renderer_context=context, )

        parser = ProtobufParser()
        new_obj = parser.parse(content, parser_context=context)

        assert new_obj == obj
