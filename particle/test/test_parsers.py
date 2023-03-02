import pytest
from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase

from particle.protos.particle import Particle
from particle.scripts.parsers import ProtobufParser


class ProtobufParserTestCase(TestCase):

    def test_parse_simple(self):
        # component = b"\n\tTest Name\x10*\x1a\x11testname@test.com"

        particle = Particle()
        particle.id = "id-123"

        parser = ProtobufParser()
        obj = parser.parse(particle.SerializeToString(), parser_context={"protobuf_cls": particle.Particle}, )
        assert obj == {
            "id": "id-123"
        }

    def test_missing_protobuf_cls(self):
        parser = ProtobufParser()
        with pytest.raises(ImproperlyConfigured):
            parser.parse(
                "", parser_context=None,
            )
