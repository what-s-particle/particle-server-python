# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestHome::test_first_screen 1'] = '''{
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
            "id": "bottom_bar_item_1",
            "bottomBarItem": {
              "text": {
                "id": "bottom_bar_item_1_text-id",
                "label": {
                  "content": "tab2"
                }
              },
              "selected": true
            }
          },
          {
            "id": "bottom_bar_item_1",
            "bottomBarItem": {
              "text": {
                "id": "bottom_bar_item_1_text-id",
                "label": {
                  "content": "tab2"
                }
              }
            }
          }
        ],
        "selectedElement": "bottom_bar_item_1"
      }
    },
    "topBar": {
      "id": "top",
      "topBar": {
        "title": {
          "id": "top_text-id",
          "label": {
            "content": "tab1"
          }
        },
        "navigationIcon": {
          "id": "icon",
          "icon": "DEFAULT_ARROW_BACK"
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

snapshots['TestHome::test_home 1'] = '''{
  "id": "nav_graph",
  "modifier": {
    "clickable": true,
    "visible": true
  },
  "navGraph": {
    "screens": [
      {
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
                  "id": "bottom_bar_item_1",
                  "bottomBarItem": {
                    "text": {
                      "id": "bottom_bar_item_1_text-id",
                      "label": {
                        "content": "tab2"
                      }
                    },
                    "selected": true
                  }
                },
                {
                  "id": "bottom_bar_item_1",
                  "bottomBarItem": {
                    "text": {
                      "id": "bottom_bar_item_1_text-id",
                      "label": {
                        "content": "tab2"
                      }
                    }
                  }
                }
              ],
              "selectedElement": "bottom_bar_item_1"
            }
          },
          "topBar": {
            "id": "top",
            "topBar": {
              "title": {
                "id": "top_text-id",
                "label": {
                  "content": "tab1"
                }
              },
              "navigationIcon": {
                "id": "icon",
                "icon": "DEFAULT_ARROW_BACK"
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
      },
      {
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
      }
    ],
    "startDestination": "screen1"
  }
}'''
