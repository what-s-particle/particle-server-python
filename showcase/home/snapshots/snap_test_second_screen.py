# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestNavScreen::test_second_screen 1'] = '''{
  "id": "screen2_destination",
  "screen": {
    "route": "screen2",
    "content": {
      "id": "screen2_text-id",
      "label": {
        "content": "screen2"
      }
    }
  }
}'''
