import pytest
from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase

from particle.protos import addressbook_pb2
from particle.protos.parsers import ProtobufParser


class ProtobufParserTestCase(TestCase):

    def test_parse_simple(self):
        # person = b"\n\tTest Name\x10*\x1a\x11testname@test.com"

        person = addressbook_pb2.Person()
        person.id = 42
        person.name = "Test Name"
        person.email = "testname@test.com"

        parser = ProtobufParser()
        obj = parser.parse(person.SerializeToString(), parser_context={"protobuf_cls": addressbook_pb2.Person}, )
        assert obj == {
            "name": "Test Name",
            "id": 42,
            "email": "testname@test.com",
        }

    def test_missing_protobuf_cls(self):
        parser = ProtobufParser()
        with pytest.raises(ImproperlyConfigured):
            parser.parse(
                "", parser_context=None,
            )
