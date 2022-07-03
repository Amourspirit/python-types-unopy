# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.xml.dom.events
from typing_extensions import Literal
import typing
from .xui_event import XUIEvent as XUIEvent_fa900d82
if typing.TYPE_CHECKING:
    from .x_event_target import XEventTarget as XEventTarget_36420f4b
    from ..views.x_abstract_view import XAbstractView as XAbstractView_35f90f4a

class XMouseEvent(XUIEvent_fa900d82):
    """

    See Also:
        `API XMouseEvent <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1dom_1_1events_1_1XMouseEvent.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.dom.events.XMouseEvent']

    def getAltKey(self) -> bool:
        """
        """
        ...
    def getButton(self) -> int:
        """
        """
        ...
    def getClientX(self) -> int:
        """
        """
        ...
    def getClientY(self) -> int:
        """
        """
        ...
    def getCtrlKey(self) -> bool:
        """
        """
        ...
    def getMetaKey(self) -> bool:
        """
        """
        ...
    def getRelatedTarget(self) -> 'XEventTarget_36420f4b':
        """
        """
        ...
    def getScreenX(self) -> int:
        """
        """
        ...
    def getScreenY(self) -> int:
        """
        """
        ...
    def getShiftKey(self) -> bool:
        """
        """
        ...
    def initMouseEvent(self, typeArg: str, canBubbleArg: bool, cancelableArg: bool, viewArg: 'XAbstractView_35f90f4a', detailArg: int, screenXArg: int, screenYArg: int, clientXArg: int, clientYArg: int, ctrlKeyArg: bool, altKeyArg: bool, shiftKeyArg: bool, metaKeyArg: bool, buttonArg: int, relatedTargetArg: 'XEventTarget_36420f4b') -> None:
        """
        """
        ...


