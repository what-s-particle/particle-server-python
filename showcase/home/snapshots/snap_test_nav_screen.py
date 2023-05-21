# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestNavScreen::test_nav_screen 1'] = '''{
  "id": "nav_graph",
  "modifier": {
    "clickable": true,
    "visible": true
  },
  "navGraph": {
    "screens": [
      {
        "id": "2b9c809d-f3fb-4a01-a9e1-6c3378d6c09a"
      },
      {
        "id": "322cd67e-34bb-4b21-ba3a-64f55b82c0af"
      }
    ],
    "startDestination": "screen1"
  }
}'''
