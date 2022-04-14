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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.xml.dom.events
# Libre Office Version: 7.2
from typing_extensions import Literal
from enum import Enum


class EventType(Enum):
    """
    Enum Class

    ENUM EventType

    See Also:
        `API EventType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1xml_1_1dom_1_1events.html#a2628ea8d12e8b2563c32f05dc7fff6fa>`_
    """
    DOMActivate: Literal['DOMActivate']
    """
    """
    DOMAttrModified: Literal['DOMAttrModified']
    """
    """
    DOMCharacterDataModified: Literal['DOMCharacterDataModified']
    """
    """
    DOMFocusIn: Literal['DOMFocusIn']
    """
    """
    DOMFocusOut: Literal['DOMFocusOut']
    """
    """
    DOMNodeInserted: Literal['DOMNodeInserted']
    """
    """
    DOMNodeInsertedIntoDocument: Literal['DOMNodeInsertedIntoDocument']
    """
    """
    DOMNodeRemoved: Literal['DOMNodeRemoved']
    """
    """
    DOMNodeRemovedFromDocument: Literal['DOMNodeRemovedFromDocument']
    """
    """
    DOMSubtreeModified: Literal['DOMSubtreeModified']
    """
    """
    click: Literal['click']
    """
    """
    mousedown: Literal['mousedown']
    """
    """
    mousemove: Literal['mousemove']
    """
    """
    mouseout: Literal['mouseout']
    """
    """
    mouseover: Literal['mouseover']
    """
    """
    mouseup: Literal['mouseup']
    """
    """

__all__ = ['EventType']

