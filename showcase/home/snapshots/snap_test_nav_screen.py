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
        "id": "nav-screen-1"
      },
      {
        "id": "nav-screen-2"
      }
    ],
    "startDestination": "screen1"
  }
}'''
