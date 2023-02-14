from unittest import TestCase

import pytest
from django.core.exceptions import ImproperlyConfigured

from particle.protos import particle
from particle.scripts.renderers import ProtobufRenderer


class ProtobufRendersTest(TestCase):

    def test_render_simple(self):
        obj = {
            "name": "Test Name",
            "id": 42,
            "email": "testname@test.com",
        }
        renderer = ProtobufRenderer()
        content = renderer.render(
            obj, renderer_context={"protobuf_cls": particle.Person},
        )
        assert content == b"\n\tTest Name\x10*\x1a\x11testname@test.com"


    def test_render_unknown_field(self):
        obj = {
            "unknown_field": "raises an error",
        }

        renderer = ProtobufRenderer()
        with pytest.raises(AttributeError):
            renderer.render(
                obj, renderer_context={"protobuf_cls": particle.Person},
            )

    def test_missing_protobuf_cls(self):
        renderer = ProtobufRenderer()
        with pytest.raises(ImproperlyConfigured):
            renderer.render(
                {}, renderer_context=None,
            )
