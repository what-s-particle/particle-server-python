# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestNavScreen::test_first_screen 1'] = '''{
  "id": "screen1_destination",
  "screen": {
    "route": "screen1",
    "content": {
      "id": "screen1_text-id",
      "label": {
        "content": "screen1"
      }
    },
    "bottomBar": {
      "id": "bottom",
      "bottomBar": {
        "elements": [
          {
            "id": "bottom-bar-item-1",
            "interactions": [
              {
                "event": [
                  "TAP_EVENT"
                ],
                "action": [
                  {
                    "navItemSelected": {
                      "target": "bottom",
                      "selectId": "bottom-bar-item-1"
                    }
                  }
                ]
              }
            ],
            "bottomBarItem": {
              "text": {
                "id": "bottom-bar-item-1-text",
                "label": {
                  "content": "Component"
                }
              },
              "selected": true
            }
          },
          {
            "id": "bottom-bar-item-2",
            "interactions": [
              {
                "event": [
                  "TAP_EVENT"
                ],
                "action": [
                  {
                    "navItemSelected": {
                      "target": "bottom",
                      "selectId": "bottom-bar-item-2"
                    }
                  }
                ]
              }
            ],
            "bottomBarItem": {
              "text": {
                "id": "bottom-bar-item-2-text",
                "label": {
                  "content": "Custom"
                }
              }
            }
          }
        ],
        "selectedElement": "bottom-bar-item-1"
      }
    },
    "topBar": {
      "id": "top",
      "topBar": {
        "title": {
          "id": "top_text-id",
          "label": {
            "content": "Top bar"
          }
        }
      }
    },
    "modalDrawer": {
      "id": "drawer",
      "modalDrawer": {
        "content": {
          "id": "12345",
          "label": {
            "content": "screen1"
          }
        }
      }
    }
  }
}'''
