from unittest import TestCase

from particle.protos import addressbook_pb2
from particle.protos.parsers import ProtobufParser
from particle.protos.renderers import ProtobufRenderer


class ProtobufRenderAndParserTestCase(TestCase):

    def test_render_and_parse(self):
        obj = {
            "name": "Test Name",
            "id": 42,
            "email": "testname@test.c1om",
        }

        context = {"protobuf_cls": addressbook_pb2.Person}

        renderer = ProtobufRenderer()
        content = renderer.render(obj, renderer_context=context, )

        parser = ProtobufParser()
        new_obj = parser.parse(content, parser_context=context)

        assert new_obj == obj
