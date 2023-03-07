from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

APP_BACKGROUND_EVENT: Event
APP_EXIT_EVENT: Event
APP_FOREGROUND_EVENT: Event
APP_START_EVENT: Event
BATTERY_CHANGE: Event
BATTERY_LOW: Event
BLUR_EVENT: Event
BOTTOM: Arrangement
BOTTOM_ALIGNMENT: Alignment
BOTTOM_CENTER: Alignment
BOTTOM_END: Alignment
BOTTOM_START: Alignment
CENTER: Arrangement
CENTER_ALIGNMENT: Alignment
CENTER_END: Alignment
CENTER_START: Alignment
CHANGE_EVENT: Event
CONNECT: RequestType
CUSTOM_FONT: FontFamily
DEFAULT: ShadowModifier
DELETE: RequestType
DESCRIPTOR: _descriptor.FileDescriptor
DOUBLE_TAP_EVENT: Event
END: Arrangement
END_ALIGNMENT: Alignment
FOCUS_EVENT: Event
GET: RequestType
HEAD: RequestType
INPUT_EVENT: Event
LOCATION_UPDATE_EVENT: Event
LONG_PRESS_EVENT: Event
MONOSPACE: FontFamily
NETWORK_CONNECTED_EVENT: Event
NETWORK_DISCONNECTED_EVENT: Event
ON_ACTION_SHEET_ITEM_CLICK: Event
ON_CHECKBOX_CHANGE: Event
ON_NAVIGATION_BAR_ITEM_CLICK: Event
ON_PICKER_ITEM_CLICK: Event
ON_RADIO_BUTTON_CLICK: Event
ON_SLIDER_VALUE_CHANGED: Event
ON_TEXT_EDITOR_VALUE_CHANGED: Event
ON_TEXT_FIELD_VALUE_CHANGED: Event
ON_TOGGLE_CHECKED_CHANGE: Event
OPTIONS: RequestType
PAGE_LOADED_EVENT: Event
PATCH: RequestType
PINCH_EVENT: Event
POST: RequestType
PUSH_NOTIFICATION_OPENED: Event
PUSH_NOTIFICATION_RECEIVED: Event
PUT: RequestType
RESET_EVENT: Event
ROTATE_EVENT: Event
SANS_SERIF: FontFamily
SCALE_ASPECT_FILL: ContentMode
SCALE_ASPECT_FIT: ContentMode
SCALE_TO_FIT: ContentMode
SCREEN_OFF: Event
SCREEN_ON: Event
SCROLL_EVENT: Event
SERIF: FontFamily
SHADOW_1: ShadowModifier
SHADOW_2: ShadowModifier
SIZE_TOKEN_0: SizeToken
SPACE_AROUND: Arrangement
SPACE_BETWEEN: Arrangement
SPACE_EVENLY: Arrangement
START: Arrangement
START_ALIGNMENT: Alignment
SYSTEM_DEFAULT: FontFamily
TAP_EVENT: Event
TOKEN_1: ColorToken
TOKEN_2: ColorToken
TOP: Arrangement
TOP_ALIGNMENT: Alignment
TOP_CENTER: Alignment
TOP_END: Alignment
TOP_START: Alignment
TOUCH_EVENT: Event
TRACE: RequestType
UNDEFINED: FontFamily
XXX: SymbolToken
XXXX: NavigationMode

class Action(_message.Message):
    __slots__ = ["condition", "custom", "navigate_back", "navigate_to", "open_external_app", "retrieve_data", "send_http_request", "show_dialog", "show_menu", "store_data", "update_modifier"]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    NAVIGATE_BACK_FIELD_NUMBER: _ClassVar[int]
    NAVIGATE_TO_FIELD_NUMBER: _ClassVar[int]
    OPEN_EXTERNAL_APP_FIELD_NUMBER: _ClassVar[int]
    RETRIEVE_DATA_FIELD_NUMBER: _ClassVar[int]
    SEND_HTTP_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SHOW_DIALOG_FIELD_NUMBER: _ClassVar[int]
    SHOW_MENU_FIELD_NUMBER: _ClassVar[int]
    STORE_DATA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    condition: ConditionAction
    custom: CustomAction
    navigate_back: NavigateBackAction
    navigate_to: NavigateToAction
    open_external_app: OpenExternalAppAction
    retrieve_data: RetrieveDataAction
    send_http_request: SendHttpRequestAction
    show_dialog: ShowDialogAction
    show_menu: ShowMenuAction
    store_data: StoreDataAction
    update_modifier: UpdateModifierAction
    def __init__(self, custom: _Optional[_Union[CustomAction, _Mapping]] = ..., navigate_to: _Optional[_Union[NavigateToAction, _Mapping]] = ..., navigate_back: _Optional[_Union[NavigateBackAction, _Mapping]] = ..., show_dialog: _Optional[_Union[ShowDialogAction, _Mapping]] = ..., show_menu: _Optional[_Union[ShowMenuAction, _Mapping]] = ..., update_modifier: _Optional[_Union[UpdateModifierAction, _Mapping]] = ..., store_data: _Optional[_Union[StoreDataAction, _Mapping]] = ..., send_http_request: _Optional[_Union[SendHttpRequestAction, _Mapping]] = ..., open_external_app: _Optional[_Union[OpenExternalAppAction, _Mapping]] = ..., condition: _Optional[_Union[ConditionAction, _Mapping]] = ..., retrieve_data: _Optional[_Union[RetrieveDataAction, _Mapping]] = ...) -> None: ...

class ActionSheetComponent(_message.Message):
    __slots__ = ["buttons", "message", "title"]
    BUTTONS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    buttons: _containers.RepeatedCompositeFieldContainer[Particle]
    message: Particle
    title: Particle
    def __init__(self, title: _Optional[_Union[Particle, _Mapping]] = ..., message: _Optional[_Union[Particle, _Mapping]] = ..., buttons: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ...) -> None: ...

class AlertComponent(_message.Message):
    __slots__ = ["confirmButton", "dismissButton", "icon", "message", "title"]
    CONFIRMBUTTON_FIELD_NUMBER: _ClassVar[int]
    DISMISSBUTTON_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    confirmButton: Particle
    dismissButton: Particle
    icon: Particle
    message: str
    title: str
    def __init__(self, title: _Optional[str] = ..., message: _Optional[str] = ..., confirmButton: _Optional[_Union[Particle, _Mapping]] = ..., dismissButton: _Optional[_Union[Particle, _Mapping]] = ..., icon: _Optional[_Union[Particle, _Mapping]] = ...) -> None: ...

class BorderModifier(_message.Message):
    __slots__ = ["color", "width"]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    color: ColorModifier
    width: int
    def __init__(self, width: _Optional[int] = ..., color: _Optional[_Union[ColorModifier, _Mapping]] = ...) -> None: ...

class BoxComponent(_message.Message):
    __slots__ = ["elements"]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    elements: _containers.RepeatedCompositeFieldContainer[Particle]
    def __init__(self, elements: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ...) -> None: ...

class ButtonComponent(_message.Message):
    __slots__ = ["elements"]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    elements: Particle
    def __init__(self, elements: _Optional[_Union[Particle, _Mapping]] = ...) -> None: ...

class CheckBoxComponent(_message.Message):
    __slots__ = ["checkedColor", "isChecked", "label", "uncheckedColor"]
    CHECKEDCOLOR_FIELD_NUMBER: _ClassVar[int]
    ISCHECKED_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    UNCHECKEDCOLOR_FIELD_NUMBER: _ClassVar[int]
    checkedColor: ColorModifier
    isChecked: bool
    label: str
    uncheckedColor: ColorModifier
    def __init__(self, label: _Optional[str] = ..., isChecked: bool = ..., uncheckedColor: _Optional[_Union[ColorModifier, _Mapping]] = ..., checkedColor: _Optional[_Union[ColorModifier, _Mapping]] = ...) -> None: ...

class ColorModifier(_message.Message):
    __slots__ = ["token", "value"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    token: ColorToken
    value: int
    def __init__(self, token: _Optional[_Union[ColorToken, str]] = ..., value: _Optional[int] = ...) -> None: ...

class ColorValue(_message.Message):
    __slots__ = ["alpha", "blue", "green", "red"]
    ALPHA_FIELD_NUMBER: _ClassVar[int]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    GREEN_FIELD_NUMBER: _ClassVar[int]
    RED_FIELD_NUMBER: _ClassVar[int]
    alpha: float
    blue: int
    green: int
    red: int
    def __init__(self, red: _Optional[int] = ..., green: _Optional[int] = ..., blue: _Optional[int] = ..., alpha: _Optional[float] = ...) -> None: ...

class ColumnComponent(_message.Message):
    __slots__ = ["alignment", "arrangement", "elements", "spacing"]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ARRANGEMENT_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    SPACING_FIELD_NUMBER: _ClassVar[int]
    alignment: Alignment
    arrangement: Arrangement
    elements: _containers.RepeatedCompositeFieldContainer[Particle]
    spacing: SizeModifier
    def __init__(self, elements: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ..., arrangement: _Optional[_Union[Arrangement, str]] = ..., alignment: _Optional[_Union[Alignment, str]] = ..., spacing: _Optional[_Union[SizeModifier, _Mapping]] = ...) -> None: ...

class ConditionAction(_message.Message):
    __slots__ = ["else_actions", "if_actions", "type"]
    ELSE_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    IF_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    else_actions: _containers.RepeatedCompositeFieldContainer[Action]
    if_actions: _containers.RepeatedCompositeFieldContainer[Action]
    type: ConditionType
    def __init__(self, type: _Optional[_Union[ConditionType, _Mapping]] = ..., if_actions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ..., else_actions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ...) -> None: ...

class ConditionType(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CustomAction(_message.Message):
    __slots__ = ["id", "payload"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    id: str
    payload: str
    def __init__(self, id: _Optional[str] = ..., payload: _Optional[str] = ...) -> None: ...

class CustomModifier(_message.Message):
    __slots__ = ["id", "payload"]
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    id: str
    payload: str
    def __init__(self, id: _Optional[str] = ..., payload: _Optional[str] = ...) -> None: ...

class ElementComponent(_message.Message):
    __slots__ = ["action_sheet", "alert", "button", "checkbox", "image", "label", "navigation_view_item", "picker", "radio_button", "slider", "text_editor", "text_field", "toggle", "top_app_bar"]
    ACTION_SHEET_FIELD_NUMBER: _ClassVar[int]
    ALERT_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    CHECKBOX_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    NAVIGATION_VIEW_ITEM_FIELD_NUMBER: _ClassVar[int]
    PICKER_FIELD_NUMBER: _ClassVar[int]
    RADIO_BUTTON_FIELD_NUMBER: _ClassVar[int]
    SLIDER_FIELD_NUMBER: _ClassVar[int]
    TEXT_EDITOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_FIELD_NUMBER: _ClassVar[int]
    TOGGLE_FIELD_NUMBER: _ClassVar[int]
    TOP_APP_BAR_FIELD_NUMBER: _ClassVar[int]
    action_sheet: ActionSheetComponent
    alert: AlertComponent
    button: ButtonComponent
    checkbox: CheckBoxComponent
    image: ImageComponent
    label: TextComponent
    navigation_view_item: NavigationBarItemComponent
    picker: PickerComponent
    radio_button: RadioButtonComponent
    slider: SliderComponent
    text_editor: TextEditorComponent
    text_field: TextFieldComponent
    toggle: ToggleComponent
    top_app_bar: TopAppBarComponent
    def __init__(self, button: _Optional[_Union[ButtonComponent, _Mapping]] = ..., label: _Optional[_Union[TextComponent, _Mapping]] = ..., image: _Optional[_Union[ImageComponent, _Mapping]] = ..., text_field: _Optional[_Union[TextFieldComponent, _Mapping]] = ..., text_editor: _Optional[_Union[TextEditorComponent, _Mapping]] = ..., slider: _Optional[_Union[SliderComponent, _Mapping]] = ..., toggle: _Optional[_Union[ToggleComponent, _Mapping]] = ..., checkbox: _Optional[_Union[CheckBoxComponent, _Mapping]] = ..., radio_button: _Optional[_Union[RadioButtonComponent, _Mapping]] = ..., picker: _Optional[_Union[PickerComponent, _Mapping]] = ..., top_app_bar: _Optional[_Union[TopAppBarComponent, _Mapping]] = ..., navigation_view_item: _Optional[_Union[NavigationBarItemComponent, _Mapping]] = ..., alert: _Optional[_Union[AlertComponent, _Mapping]] = ..., action_sheet: _Optional[_Union[ActionSheetComponent, _Mapping]] = ...) -> None: ...

class IconComponent(_message.Message):
    __slots__ = ["description", "symbol"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    description: str
    symbol: SymbolToken
    def __init__(self, symbol: _Optional[_Union[SymbolToken, str]] = ..., description: _Optional[str] = ...) -> None: ...

class ImageComponent(_message.Message):
    __slots__ = ["circular", "content_mode", "description", "local", "url"]
    CIRCULAR_FIELD_NUMBER: _ClassVar[int]
    CONTENT_MODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    circular: bool
    content_mode: ContentMode
    description: str
    local: bool
    url: str
    def __init__(self, url: _Optional[str] = ..., description: _Optional[str] = ..., circular: bool = ..., local: bool = ..., content_mode: _Optional[_Union[ContentMode, str]] = ...) -> None: ...

class InsetsModifier(_message.Message):
    __slots__ = ["bottom", "left", "right", "top"]
    BOTTOM_FIELD_NUMBER: _ClassVar[int]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    TOP_FIELD_NUMBER: _ClassVar[int]
    bottom: SizeModifier
    left: SizeModifier
    right: SizeModifier
    top: SizeModifier
    def __init__(self, left: _Optional[_Union[SizeModifier, _Mapping]] = ..., top: _Optional[_Union[SizeModifier, _Mapping]] = ..., right: _Optional[_Union[SizeModifier, _Mapping]] = ..., bottom: _Optional[_Union[SizeModifier, _Mapping]] = ...) -> None: ...

class Interaction(_message.Message):
    __slots__ = ["action", "event"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    action: _containers.RepeatedCompositeFieldContainer[Action]
    event: _containers.RepeatedScalarFieldContainer[Event]
    def __init__(self, event: _Optional[_Iterable[_Union[Event, str]]] = ..., action: _Optional[_Iterable[_Union[Action, _Mapping]]] = ...) -> None: ...

class LayoutComponent(_message.Message):
    __slots__ = ["box", "column", "lazy_column", "lazy_row", "navigation_view", "row", "tab_view"]
    BOX_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    LAZY_COLUMN_FIELD_NUMBER: _ClassVar[int]
    LAZY_ROW_FIELD_NUMBER: _ClassVar[int]
    NAVIGATION_VIEW_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    TAB_VIEW_FIELD_NUMBER: _ClassVar[int]
    box: BoxComponent
    column: ColumnComponent
    lazy_column: LazyColumnComponent
    lazy_row: LazyRowComponent
    navigation_view: NavigationViewComponent
    row: RowComponent
    tab_view: TabViewComponent
    def __init__(self, row: _Optional[_Union[RowComponent, _Mapping]] = ..., column: _Optional[_Union[ColumnComponent, _Mapping]] = ..., box: _Optional[_Union[BoxComponent, _Mapping]] = ..., lazy_column: _Optional[_Union[LazyColumnComponent, _Mapping]] = ..., lazy_row: _Optional[_Union[LazyRowComponent, _Mapping]] = ..., tab_view: _Optional[_Union[TabViewComponent, _Mapping]] = ..., navigation_view: _Optional[_Union[NavigationViewComponent, _Mapping]] = ...) -> None: ...

class LazyColumnComponent(_message.Message):
    __slots__ = ["alignment", "arrangement", "content_padding", "elements", "reverse_layout", "spacing"]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ARRANGEMENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_PADDING_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    REVERSE_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    SPACING_FIELD_NUMBER: _ClassVar[int]
    alignment: Alignment
    arrangement: Arrangement
    content_padding: InsetsModifier
    elements: _containers.RepeatedCompositeFieldContainer[Particle]
    reverse_layout: bool
    spacing: SizeModifier
    def __init__(self, elements: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ..., arrangement: _Optional[_Union[Arrangement, str]] = ..., alignment: _Optional[_Union[Alignment, str]] = ..., spacing: _Optional[_Union[SizeModifier, _Mapping]] = ..., reverse_layout: bool = ..., content_padding: _Optional[_Union[InsetsModifier, _Mapping]] = ...) -> None: ...

class LazyRowComponent(_message.Message):
    __slots__ = ["alignment", "arrangement", "content_padding", "elements", "reverse_layout", "spacing"]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ARRANGEMENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_PADDING_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    REVERSE_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    SPACING_FIELD_NUMBER: _ClassVar[int]
    alignment: Alignment
    arrangement: Arrangement
    content_padding: InsetsModifier
    elements: _containers.RepeatedCompositeFieldContainer[Particle]
    reverse_layout: bool
    spacing: SizeModifier
    def __init__(self, elements: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ..., arrangement: _Optional[_Union[Arrangement, str]] = ..., alignment: _Optional[_Union[Alignment, str]] = ..., spacing: _Optional[_Union[SizeModifier, _Mapping]] = ..., reverse_layout: bool = ..., content_padding: _Optional[_Union[InsetsModifier, _Mapping]] = ...) -> None: ...

class Modifier(_message.Message):
    __slots__ = ["background", "blur", "border", "clickable", "custom", "focusable", "offset", "opacity", "padding", "require_size", "shadow", "size", "visible", "weight"]
    BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    BLUR_FIELD_NUMBER: _ClassVar[int]
    BORDER_FIELD_NUMBER: _ClassVar[int]
    CLICKABLE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    FOCUSABLE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    OPACITY_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SHADOW_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    background: ColorModifier
    blur: OffsetModifier
    border: BorderModifier
    clickable: bool
    custom: _containers.RepeatedCompositeFieldContainer[CustomModifier]
    focusable: bool
    offset: OffsetModifier
    opacity: float
    padding: InsetsModifier
    require_size: SizeModifier
    shadow: ShadowModifier
    size: SizeModifier
    visible: bool
    weight: float
    def __init__(self, custom: _Optional[_Iterable[_Union[CustomModifier, _Mapping]]] = ..., background: _Optional[_Union[ColorModifier, _Mapping]] = ..., blur: _Optional[_Union[OffsetModifier, _Mapping]] = ..., border: _Optional[_Union[BorderModifier, _Mapping]] = ..., clickable: bool = ..., focusable: bool = ..., offset: _Optional[_Union[OffsetModifier, _Mapping]] = ..., opacity: _Optional[float] = ..., padding: _Optional[_Union[InsetsModifier, _Mapping]] = ..., require_size: _Optional[_Union[SizeModifier, _Mapping]] = ..., shadow: _Optional[_Union[ShadowModifier, str]] = ..., size: _Optional[_Union[SizeModifier, _Mapping]] = ..., visible: bool = ..., weight: _Optional[float] = ...) -> None: ...

class NavigateBackAction(_message.Message):
    __slots__ = ["mode"]
    MODE_FIELD_NUMBER: _ClassVar[int]
    mode: NavigationMode
    def __init__(self, mode: _Optional[_Union[NavigationMode, str]] = ...) -> None: ...

class NavigateToAction(_message.Message):
    __slots__ = ["mode", "target"]
    MODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    mode: NavigationMode
    target: str
    def __init__(self, target: _Optional[str] = ..., mode: _Optional[_Union[NavigationMode, str]] = ...) -> None: ...

class NavigationBarItemComponent(_message.Message):
    __slots__ = ["icon", "selected", "text"]
    ICON_FIELD_NUMBER: _ClassVar[int]
    SELECTED_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    icon: Particle
    selected: bool
    text: Particle
    def __init__(self, text: _Optional[_Union[Particle, _Mapping]] = ..., icon: _Optional[_Union[Particle, _Mapping]] = ..., selected: bool = ...) -> None: ...

class NavigationViewComponent(_message.Message):
    __slots__ = ["bars", "elements", "selected_element"]
    BARS_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    bars: _containers.RepeatedCompositeFieldContainer[Particle]
    elements: _containers.RepeatedCompositeFieldContainer[Particle]
    selected_element: str
    def __init__(self, elements: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ..., bars: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ..., selected_element: _Optional[str] = ...) -> None: ...

class OffsetModifier(_message.Message):
    __slots__ = ["xOffset", "yOffset"]
    XOFFSET_FIELD_NUMBER: _ClassVar[int]
    YOFFSET_FIELD_NUMBER: _ClassVar[int]
    xOffset: SizeModifier
    yOffset: SizeModifier
    def __init__(self, xOffset: _Optional[_Union[SizeModifier, _Mapping]] = ..., yOffset: _Optional[_Union[SizeModifier, _Mapping]] = ...) -> None: ...

class OpenExternalAppAction(_message.Message):
    __slots__ = ["url"]
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class Particle(_message.Message):
    __slots__ = ["element", "id", "interactions", "layout", "modifier"]
    ELEMENT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INTERACTIONS_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_FIELD_NUMBER: _ClassVar[int]
    element: ElementComponent
    id: str
    interactions: _containers.RepeatedCompositeFieldContainer[Interaction]
    layout: LayoutComponent
    modifier: Modifier
    def __init__(self, id: _Optional[str] = ..., element: _Optional[_Union[ElementComponent, _Mapping]] = ..., layout: _Optional[_Union[LayoutComponent, _Mapping]] = ..., modifier: _Optional[_Union[Modifier, _Mapping]] = ..., interactions: _Optional[_Iterable[_Union[Interaction, _Mapping]]] = ...) -> None: ...

class PickerComponent(_message.Message):
    __slots__ = ["options", "selected_option"]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_OPTION_FIELD_NUMBER: _ClassVar[int]
    options: _containers.RepeatedCompositeFieldContainer[Particle]
    selected_option: str
    def __init__(self, options: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ..., selected_option: _Optional[str] = ...) -> None: ...

class RadioButtonComponent(_message.Message):
    __slots__ = ["disabledColor", "enabled", "selected", "selectedColor", "unselectedColor"]
    DISABLEDCOLOR_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SELECTEDCOLOR_FIELD_NUMBER: _ClassVar[int]
    SELECTED_FIELD_NUMBER: _ClassVar[int]
    UNSELECTEDCOLOR_FIELD_NUMBER: _ClassVar[int]
    disabledColor: ColorModifier
    enabled: bool
    selected: bool
    selectedColor: ColorModifier
    unselectedColor: ColorModifier
    def __init__(self, selected: bool = ..., enabled: bool = ..., selectedColor: _Optional[_Union[ColorModifier, _Mapping]] = ..., unselectedColor: _Optional[_Union[ColorModifier, _Mapping]] = ..., disabledColor: _Optional[_Union[ColorModifier, _Mapping]] = ...) -> None: ...

class RetrieveDataAction(_message.Message):
    __slots__ = ["key", "subsequent_action", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SUBSEQUENT_ACTION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    subsequent_action: _containers.RepeatedCompositeFieldContainer[Action]
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., subsequent_action: _Optional[_Iterable[_Union[Action, _Mapping]]] = ...) -> None: ...

class RowComponent(_message.Message):
    __slots__ = ["alignment", "arrangement", "elements", "spacing"]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ARRANGEMENT_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    SPACING_FIELD_NUMBER: _ClassVar[int]
    alignment: Alignment
    arrangement: Arrangement
    elements: _containers.RepeatedCompositeFieldContainer[Particle]
    spacing: SizeModifier
    def __init__(self, elements: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ..., arrangement: _Optional[_Union[Arrangement, str]] = ..., alignment: _Optional[_Union[Alignment, str]] = ..., spacing: _Optional[_Union[SizeModifier, _Mapping]] = ...) -> None: ...

class SendHttpRequestAction(_message.Message):
    __slots__ = ["body", "endpoint", "failure_actions", "success_actions", "type"]
    class BodyEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    body: _containers.ScalarMap[str, str]
    endpoint: str
    failure_actions: _containers.RepeatedCompositeFieldContainer[Action]
    success_actions: _containers.RepeatedCompositeFieldContainer[Action]
    type: RequestType
    def __init__(self, endpoint: _Optional[str] = ..., type: _Optional[_Union[RequestType, str]] = ..., body: _Optional[_Mapping[str, str]] = ..., success_actions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ..., failure_actions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ...) -> None: ...

class ShowDialogAction(_message.Message):
    __slots__ = ["dialog"]
    DIALOG_FIELD_NUMBER: _ClassVar[int]
    dialog: Particle
    def __init__(self, dialog: _Optional[_Union[Particle, _Mapping]] = ...) -> None: ...

class ShowMenuAction(_message.Message):
    __slots__ = ["menu"]
    MENU_FIELD_NUMBER: _ClassVar[int]
    menu: Particle
    def __init__(self, menu: _Optional[_Union[Particle, _Mapping]] = ...) -> None: ...

class SizeModifier(_message.Message):
    __slots__ = ["token", "value"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    token: SizeToken
    value: int
    def __init__(self, token: _Optional[_Union[SizeToken, str]] = ..., value: _Optional[int] = ...) -> None: ...

class SliderComponent(_message.Message):
    __slots__ = ["currentValue", "defaultValue", "label", "max", "min"]
    CURRENTVALUE_FIELD_NUMBER: _ClassVar[int]
    DEFAULTVALUE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    currentValue: float
    defaultValue: float
    label: str
    max: float
    min: float
    def __init__(self, min: _Optional[float] = ..., max: _Optional[float] = ..., defaultValue: _Optional[float] = ..., currentValue: _Optional[float] = ..., label: _Optional[str] = ...) -> None: ...

class StoreDataAction(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class TabViewComponent(_message.Message):
    __slots__ = ["enabled", "selected", "selected_color", "tabs", "unselected_color"]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SELECTED_COLOR_FIELD_NUMBER: _ClassVar[int]
    SELECTED_FIELD_NUMBER: _ClassVar[int]
    TABS_FIELD_NUMBER: _ClassVar[int]
    UNSELECTED_COLOR_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    selected: bool
    selected_color: ColorModifier
    tabs: _containers.RepeatedCompositeFieldContainer[Particle]
    unselected_color: ColorModifier
    def __init__(self, tabs: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ..., selected: bool = ..., enabled: bool = ..., selected_color: _Optional[_Union[ColorModifier, _Mapping]] = ..., unselected_color: _Optional[_Union[ColorModifier, _Mapping]] = ...) -> None: ...

class TextComponent(_message.Message):
    __slots__ = ["bold", "color", "content", "fontFamily", "fontSize", "italic", "strikethrough", "underline"]
    BOLD_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FONTFAMILY_FIELD_NUMBER: _ClassVar[int]
    FONTSIZE_FIELD_NUMBER: _ClassVar[int]
    ITALIC_FIELD_NUMBER: _ClassVar[int]
    STRIKETHROUGH_FIELD_NUMBER: _ClassVar[int]
    UNDERLINE_FIELD_NUMBER: _ClassVar[int]
    bold: bool
    color: ColorModifier
    content: str
    fontFamily: FontFamily
    fontSize: SizeModifier
    italic: bool
    strikethrough: bool
    underline: bool
    def __init__(self, content: _Optional[str] = ..., fontFamily: _Optional[_Union[FontFamily, str]] = ..., fontSize: _Optional[_Union[SizeModifier, _Mapping]] = ..., bold: bool = ..., italic: bool = ..., underline: bool = ..., strikethrough: bool = ..., color: _Optional[_Union[ColorModifier, _Mapping]] = ...) -> None: ...

class TextEditorComponent(_message.Message):
    __slots__ = ["placeholder", "value"]
    PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    placeholder: str
    value: str
    def __init__(self, placeholder: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class TextFieldComponent(_message.Message):
    __slots__ = ["placeholder", "value"]
    PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    placeholder: str
    value: str
    def __init__(self, placeholder: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ToggleComponent(_message.Message):
    __slots__ = ["isChecked", "label"]
    ISCHECKED_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    isChecked: bool
    label: str
    def __init__(self, label: _Optional[str] = ..., isChecked: bool = ...) -> None: ...

class TopAppBarComponent(_message.Message):
    __slots__ = ["action_icon", "navigation_icon", "title"]
    ACTION_ICON_FIELD_NUMBER: _ClassVar[int]
    NAVIGATION_ICON_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    action_icon: Particle
    navigation_icon: Particle
    title: Particle
    def __init__(self, title: _Optional[_Union[Particle, _Mapping]] = ..., navigation_icon: _Optional[_Union[Particle, _Mapping]] = ..., action_icon: _Optional[_Union[Particle, _Mapping]] = ...) -> None: ...

class UpdateModifierAction(_message.Message):
    __slots__ = ["modifier", "override"]
    MODIFIER_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    modifier: Modifier
    override: bool
    def __init__(self, override: bool = ..., modifier: _Optional[_Union[Modifier, _Mapping]] = ...) -> None: ...

class ColorToken(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SizeToken(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ShadowModifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ContentMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SymbolToken(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class FontFamily(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Arrangement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Event(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class NavigationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class RequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
