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
DEFAULT_ACCOUNT_BOX: IconComponent
DEFAULT_ACCOUNT_CIRCLE: IconComponent
DEFAULT_ADD: IconComponent
DEFAULT_ADD_CIRCLE: IconComponent
DEFAULT_ARROW_BACK: IconComponent
DEFAULT_ARROW_DROP_DOWN: IconComponent
DEFAULT_ARROW_FORWARD: IconComponent
DEFAULT_BUILD: IconComponent
DEFAULT_CALL: IconComponent
DEFAULT_CHECK: IconComponent
DEFAULT_CHECK_CIRCLE: IconComponent
DEFAULT_CLEAR: IconComponent
DEFAULT_CLOSE: IconComponent
DEFAULT_CREATE: IconComponent
DEFAULT_DATE_RANGE: IconComponent
DEFAULT_DELETE: IconComponent
DEFAULT_DONE: IconComponent
DEFAULT_EDIT: IconComponent
DEFAULT_EMAIL: IconComponent
DEFAULT_EXIT_TO_APP: IconComponent
DEFAULT_FACE: IconComponent
DEFAULT_FAVORITE: IconComponent
DEFAULT_FAVORITE_BORDER: IconComponent
DEFAULT_HOME: IconComponent
DEFAULT_INFO: IconComponent
DEFAULT_KEYBOARD_ARROW_DOWN: IconComponent
DEFAULT_KEYBOARD_ARROW_LEFT: IconComponent
DEFAULT_KEYBOARD_ARROW_RIGHT: IconComponent
DEFAULT_KEYBOARD_ARROW_UP: IconComponent
DEFAULT_LIST: IconComponent
DEFAULT_LOCATION_ON: IconComponent
DEFAULT_LOCK: IconComponent
DEFAULT_MAIL_OUTLINE: IconComponent
DEFAULT_MENU: IconComponent
DEFAULT_MOR_EVERT: IconComponent
DEFAULT_NOTIFICATIONS: IconComponent
DEFAULT_PERSON: IconComponent
DEFAULT_PHONE: IconComponent
DEFAULT_PLACE: IconComponent
DEFAULT_PLAY_ARROW: IconComponent
DEFAULT_REFRESH: IconComponent
DEFAULT_SEARCH: IconComponent
DEFAULT_SEND: IconComponent
DEFAULT_SETTINGS: IconComponent
DEFAULT_SHARE: IconComponent
DEFAULT_SHOPPINGCART: IconComponent
DEFAULT_STAR: IconComponent
DEFAULT_THUMBUP: IconComponent
DEFAULT_WARNING: IconComponent
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
XXXX: NavigationMode

class Action(_message.Message):
    __slots__ = ["condition", "custom", "navItemSelected", "navigateBack", "navigateTo", "openExternalApp", "retrieveData", "sendHttpRequest", "showDialog", "showMenu", "storeData", "updateModifier"]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    NAVIGATEBACK_FIELD_NUMBER: _ClassVar[int]
    NAVIGATETO_FIELD_NUMBER: _ClassVar[int]
    NAVITEMSELECTED_FIELD_NUMBER: _ClassVar[int]
    OPENEXTERNALAPP_FIELD_NUMBER: _ClassVar[int]
    RETRIEVEDATA_FIELD_NUMBER: _ClassVar[int]
    SENDHTTPREQUEST_FIELD_NUMBER: _ClassVar[int]
    SHOWDIALOG_FIELD_NUMBER: _ClassVar[int]
    SHOWMENU_FIELD_NUMBER: _ClassVar[int]
    STOREDATA_FIELD_NUMBER: _ClassVar[int]
    UPDATEMODIFIER_FIELD_NUMBER: _ClassVar[int]
    condition: ConditionAction
    custom: CustomAction
    navItemSelected: NavItemSelectedAction
    navigateBack: NavigateBackAction
    navigateTo: NavigateToAction
    openExternalApp: OpenExternalAppAction
    retrieveData: RetrieveDataAction
    sendHttpRequest: SendHttpRequestAction
    showDialog: ShowDialogAction
    showMenu: ShowMenuAction
    storeData: StoreDataAction
    updateModifier: UpdateModifierAction
    def __init__(self, custom: _Optional[_Union[CustomAction, _Mapping]] = ..., navigateTo: _Optional[_Union[NavigateToAction, _Mapping]] = ..., navigateBack: _Optional[_Union[NavigateBackAction, _Mapping]] = ..., showDialog: _Optional[_Union[ShowDialogAction, _Mapping]] = ..., showMenu: _Optional[_Union[ShowMenuAction, _Mapping]] = ..., updateModifier: _Optional[_Union[UpdateModifierAction, _Mapping]] = ..., storeData: _Optional[_Union[StoreDataAction, _Mapping]] = ..., sendHttpRequest: _Optional[_Union[SendHttpRequestAction, _Mapping]] = ..., openExternalApp: _Optional[_Union[OpenExternalAppAction, _Mapping]] = ..., condition: _Optional[_Union[ConditionAction, _Mapping]] = ..., retrieveData: _Optional[_Union[RetrieveDataAction, _Mapping]] = ..., navItemSelected: _Optional[_Union[NavItemSelectedAction, _Mapping]] = ...) -> None: ...

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

class BottomBarComponent(_message.Message):
    __slots__ = ["elements", "selectedElement"]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    SELECTEDELEMENT_FIELD_NUMBER: _ClassVar[int]
    elements: _containers.RepeatedCompositeFieldContainer[Particle]
    selectedElement: str
    def __init__(self, elements: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ..., selectedElement: _Optional[str] = ...) -> None: ...

class BottomBarItemComponent(_message.Message):
    __slots__ = ["icon", "selected", "text"]
    ICON_FIELD_NUMBER: _ClassVar[int]
    SELECTED_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    icon: Particle
    selected: bool
    text: Particle
    def __init__(self, text: _Optional[_Union[Particle, _Mapping]] = ..., icon: _Optional[_Union[Particle, _Mapping]] = ..., selected: bool = ...) -> None: ...

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
    __slots__ = ["elseActions", "ifActions", "type"]
    ELSEACTIONS_FIELD_NUMBER: _ClassVar[int]
    IFACTIONS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    elseActions: _containers.RepeatedCompositeFieldContainer[Action]
    ifActions: _containers.RepeatedCompositeFieldContainer[Action]
    type: ConditionType
    def __init__(self, type: _Optional[_Union[ConditionType, _Mapping]] = ..., ifActions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ..., elseActions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ...) -> None: ...

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

class LazyColumnComponent(_message.Message):
    __slots__ = ["alignment", "arrangement", "contentPadding", "elements", "reverseLayout", "spacing"]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ARRANGEMENT_FIELD_NUMBER: _ClassVar[int]
    CONTENTPADDING_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    REVERSELAYOUT_FIELD_NUMBER: _ClassVar[int]
    SPACING_FIELD_NUMBER: _ClassVar[int]
    alignment: Alignment
    arrangement: Arrangement
    contentPadding: InsetsModifier
    elements: _containers.RepeatedCompositeFieldContainer[Particle]
    reverseLayout: bool
    spacing: SizeModifier
    def __init__(self, elements: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ..., arrangement: _Optional[_Union[Arrangement, str]] = ..., alignment: _Optional[_Union[Alignment, str]] = ..., spacing: _Optional[_Union[SizeModifier, _Mapping]] = ..., reverseLayout: bool = ..., contentPadding: _Optional[_Union[InsetsModifier, _Mapping]] = ...) -> None: ...

class LazyRowComponent(_message.Message):
    __slots__ = ["alignment", "arrangement", "contentPadding", "elements", "reverseLayout", "spacing"]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ARRANGEMENT_FIELD_NUMBER: _ClassVar[int]
    CONTENTPADDING_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    REVERSELAYOUT_FIELD_NUMBER: _ClassVar[int]
    SPACING_FIELD_NUMBER: _ClassVar[int]
    alignment: Alignment
    arrangement: Arrangement
    contentPadding: InsetsModifier
    elements: _containers.RepeatedCompositeFieldContainer[Particle]
    reverseLayout: bool
    spacing: SizeModifier
    def __init__(self, elements: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ..., arrangement: _Optional[_Union[Arrangement, str]] = ..., alignment: _Optional[_Union[Alignment, str]] = ..., spacing: _Optional[_Union[SizeModifier, _Mapping]] = ..., reverseLayout: bool = ..., contentPadding: _Optional[_Union[InsetsModifier, _Mapping]] = ...) -> None: ...

class ModalDrawerComponent(_message.Message):
    __slots__ = ["content"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: Particle
    def __init__(self, content: _Optional[_Union[Particle, _Mapping]] = ...) -> None: ...

class Modifier(_message.Message):
    __slots__ = ["background", "blur", "border", "clickable", "custom", "focusable", "offset", "opacity", "padding", "requireSize", "shadow", "size", "visible", "weight"]
    BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    BLUR_FIELD_NUMBER: _ClassVar[int]
    BORDER_FIELD_NUMBER: _ClassVar[int]
    CLICKABLE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    FOCUSABLE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    OPACITY_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    REQUIRESIZE_FIELD_NUMBER: _ClassVar[int]
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
    requireSize: SizeModifier
    shadow: ShadowModifier
    size: SizeModifier
    visible: bool
    weight: float
    def __init__(self, custom: _Optional[_Iterable[_Union[CustomModifier, _Mapping]]] = ..., background: _Optional[_Union[ColorModifier, _Mapping]] = ..., blur: _Optional[_Union[OffsetModifier, _Mapping]] = ..., border: _Optional[_Union[BorderModifier, _Mapping]] = ..., clickable: bool = ..., focusable: bool = ..., offset: _Optional[_Union[OffsetModifier, _Mapping]] = ..., opacity: _Optional[float] = ..., padding: _Optional[_Union[InsetsModifier, _Mapping]] = ..., requireSize: _Optional[_Union[SizeModifier, _Mapping]] = ..., shadow: _Optional[_Union[ShadowModifier, str]] = ..., size: _Optional[_Union[SizeModifier, _Mapping]] = ..., visible: bool = ..., weight: _Optional[float] = ...) -> None: ...

class NavGraphComponent(_message.Message):
    __slots__ = ["name", "screens", "startDestination"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCREENS_FIELD_NUMBER: _ClassVar[int]
    STARTDESTINATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    screens: _containers.RepeatedCompositeFieldContainer[Particle]
    startDestination: str
    def __init__(self, name: _Optional[str] = ..., screens: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ..., startDestination: _Optional[str] = ...) -> None: ...

class NavItemSelectedAction(_message.Message):
    __slots__ = ["selectId", "target"]
    SELECTID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    selectId: str
    target: str
    def __init__(self, target: _Optional[str] = ..., selectId: _Optional[str] = ...) -> None: ...

class NavigateBackAction(_message.Message):
    __slots__ = ["mode"]
    MODE_FIELD_NUMBER: _ClassVar[int]
    mode: NavigationMode
    def __init__(self, mode: _Optional[_Union[NavigationMode, str]] = ...) -> None: ...

class NavigateToAction(_message.Message):
    __slots__ = ["mode", "route"]
    MODE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    mode: NavigationMode
    route: str
    def __init__(self, route: _Optional[str] = ..., mode: _Optional[_Union[NavigationMode, str]] = ...) -> None: ...

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
    __slots__ = ["actionSheet", "alert", "bottomBar", "bottomBarItem", "box", "button", "checkbox", "column", "icon", "id", "image", "interactions", "label", "lazyColumn", "lazyRow", "modalDrawer", "modifier", "navGraph", "picker", "radioButton", "row", "screen", "slider", "tabView", "textEditor", "textField", "toggle", "topBar"]
    ACTIONSHEET_FIELD_NUMBER: _ClassVar[int]
    ALERT_FIELD_NUMBER: _ClassVar[int]
    BOTTOMBARITEM_FIELD_NUMBER: _ClassVar[int]
    BOTTOMBAR_FIELD_NUMBER: _ClassVar[int]
    BOX_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    CHECKBOX_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    INTERACTIONS_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LAZYCOLUMN_FIELD_NUMBER: _ClassVar[int]
    LAZYROW_FIELD_NUMBER: _ClassVar[int]
    MODALDRAWER_FIELD_NUMBER: _ClassVar[int]
    MODIFIER_FIELD_NUMBER: _ClassVar[int]
    NAVGRAPH_FIELD_NUMBER: _ClassVar[int]
    PICKER_FIELD_NUMBER: _ClassVar[int]
    RADIOBUTTON_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    SCREEN_FIELD_NUMBER: _ClassVar[int]
    SLIDER_FIELD_NUMBER: _ClassVar[int]
    TABVIEW_FIELD_NUMBER: _ClassVar[int]
    TEXTEDITOR_FIELD_NUMBER: _ClassVar[int]
    TEXTFIELD_FIELD_NUMBER: _ClassVar[int]
    TOGGLE_FIELD_NUMBER: _ClassVar[int]
    TOPBAR_FIELD_NUMBER: _ClassVar[int]
    actionSheet: ActionSheetComponent
    alert: AlertComponent
    bottomBar: BottomBarComponent
    bottomBarItem: BottomBarItemComponent
    box: BoxComponent
    button: ButtonComponent
    checkbox: CheckBoxComponent
    column: ColumnComponent
    icon: IconComponent
    id: str
    image: ImageComponent
    interactions: _containers.RepeatedCompositeFieldContainer[Interaction]
    label: TextComponent
    lazyColumn: LazyColumnComponent
    lazyRow: LazyRowComponent
    modalDrawer: ModalDrawerComponent
    modifier: Modifier
    navGraph: NavGraphComponent
    picker: PickerComponent
    radioButton: RadioButtonComponent
    row: RowComponent
    screen: ScreenComponent
    slider: SliderComponent
    tabView: TabViewComponent
    textEditor: TextEditorComponent
    textField: TextFieldComponent
    toggle: ToggleComponent
    topBar: TopBarComponent
    def __init__(self, id: _Optional[str] = ..., modifier: _Optional[_Union[Modifier, _Mapping]] = ..., interactions: _Optional[_Iterable[_Union[Interaction, _Mapping]]] = ..., button: _Optional[_Union[ButtonComponent, _Mapping]] = ..., label: _Optional[_Union[TextComponent, _Mapping]] = ..., image: _Optional[_Union[ImageComponent, _Mapping]] = ..., textField: _Optional[_Union[TextFieldComponent, _Mapping]] = ..., textEditor: _Optional[_Union[TextEditorComponent, _Mapping]] = ..., slider: _Optional[_Union[SliderComponent, _Mapping]] = ..., toggle: _Optional[_Union[ToggleComponent, _Mapping]] = ..., checkbox: _Optional[_Union[CheckBoxComponent, _Mapping]] = ..., radioButton: _Optional[_Union[RadioButtonComponent, _Mapping]] = ..., picker: _Optional[_Union[PickerComponent, _Mapping]] = ..., icon: _Optional[_Union[IconComponent, str]] = ..., bottomBarItem: _Optional[_Union[BottomBarItemComponent, _Mapping]] = ..., alert: _Optional[_Union[AlertComponent, _Mapping]] = ..., actionSheet: _Optional[_Union[ActionSheetComponent, _Mapping]] = ..., navGraph: _Optional[_Union[NavGraphComponent, _Mapping]] = ..., screen: _Optional[_Union[ScreenComponent, _Mapping]] = ..., topBar: _Optional[_Union[TopBarComponent, _Mapping]] = ..., bottomBar: _Optional[_Union[BottomBarComponent, _Mapping]] = ..., modalDrawer: _Optional[_Union[ModalDrawerComponent, _Mapping]] = ..., row: _Optional[_Union[RowComponent, _Mapping]] = ..., column: _Optional[_Union[ColumnComponent, _Mapping]] = ..., box: _Optional[_Union[BoxComponent, _Mapping]] = ..., lazyColumn: _Optional[_Union[LazyColumnComponent, _Mapping]] = ..., lazyRow: _Optional[_Union[LazyRowComponent, _Mapping]] = ..., tabView: _Optional[_Union[TabViewComponent, _Mapping]] = ...) -> None: ...

class PickerComponent(_message.Message):
    __slots__ = ["iconContent", "options", "trigger"]
    ICONCONTENT_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    iconContent: Particle
    options: _containers.RepeatedCompositeFieldContainer[Particle]
    trigger: Event
    def __init__(self, iconContent: _Optional[_Union[Particle, _Mapping]] = ..., options: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ..., trigger: _Optional[_Union[Event, str]] = ...) -> None: ...

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
    __slots__ = ["key", "subsequentAction", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SUBSEQUENTACTION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    subsequentAction: _containers.RepeatedCompositeFieldContainer[Action]
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., subsequentAction: _Optional[_Iterable[_Union[Action, _Mapping]]] = ...) -> None: ...

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

class ScreenComponent(_message.Message):
    __slots__ = ["bottomBar", "content", "modalDrawer", "route", "topBar"]
    BOTTOMBAR_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    MODALDRAWER_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    TOPBAR_FIELD_NUMBER: _ClassVar[int]
    bottomBar: Particle
    content: Particle
    modalDrawer: Particle
    route: str
    topBar: Particle
    def __init__(self, route: _Optional[str] = ..., content: _Optional[_Union[Particle, _Mapping]] = ..., bottomBar: _Optional[_Union[Particle, _Mapping]] = ..., topBar: _Optional[_Union[Particle, _Mapping]] = ..., modalDrawer: _Optional[_Union[Particle, _Mapping]] = ..., **kwargs) -> None: ...

class SendHttpRequestAction(_message.Message):
    __slots__ = ["body", "endpoint", "failureActions", "successActions", "type"]
    class BodyEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    FAILUREACTIONS_FIELD_NUMBER: _ClassVar[int]
    SUCCESSACTIONS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    body: _containers.ScalarMap[str, str]
    endpoint: str
    failureActions: _containers.RepeatedCompositeFieldContainer[Action]
    successActions: _containers.RepeatedCompositeFieldContainer[Action]
    type: RequestType
    def __init__(self, endpoint: _Optional[str] = ..., type: _Optional[_Union[RequestType, str]] = ..., body: _Optional[_Mapping[str, str]] = ..., successActions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ..., failureActions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ...) -> None: ...

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
    __slots__ = ["enabled", "selected", "selectedColor", "tabs", "unselectedColor"]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SELECTEDCOLOR_FIELD_NUMBER: _ClassVar[int]
    SELECTED_FIELD_NUMBER: _ClassVar[int]
    TABS_FIELD_NUMBER: _ClassVar[int]
    UNSELECTEDCOLOR_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    selected: bool
    selectedColor: ColorModifier
    tabs: _containers.RepeatedCompositeFieldContainer[Particle]
    unselectedColor: ColorModifier
    def __init__(self, tabs: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ..., selected: bool = ..., enabled: bool = ..., selectedColor: _Optional[_Union[ColorModifier, _Mapping]] = ..., unselectedColor: _Optional[_Union[ColorModifier, _Mapping]] = ...) -> None: ...

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

class TopBarComponent(_message.Message):
    __slots__ = ["actions", "backgroundColor", "contentColor", "elevation", "navigationIcon", "title"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    BACKGROUNDCOLOR_FIELD_NUMBER: _ClassVar[int]
    CONTENTCOLOR_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_FIELD_NUMBER: _ClassVar[int]
    NAVIGATIONICON_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[Particle]
    backgroundColor: ColorModifier
    contentColor: ColorModifier
    elevation: int
    navigationIcon: Particle
    title: Particle
    def __init__(self, title: _Optional[_Union[Particle, _Mapping]] = ..., navigationIcon: _Optional[_Union[Particle, _Mapping]] = ..., actions: _Optional[_Iterable[_Union[Particle, _Mapping]]] = ..., elevation: _Optional[int] = ..., backgroundColor: _Optional[_Union[ColorModifier, _Mapping]] = ..., contentColor: _Optional[_Union[ColorModifier, _Mapping]] = ...) -> None: ...

class UpdateModifierAction(_message.Message):
    __slots__ = ["modifier", "override", "target"]
    MODIFIER_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    modifier: Modifier
    override: bool
    target: str
    def __init__(self, target: _Optional[str] = ..., override: bool = ..., modifier: _Optional[_Union[Modifier, _Mapping]] = ...) -> None: ...

class ColorToken(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SizeToken(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ShadowModifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ContentMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class FontFamily(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class IconComponent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
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
