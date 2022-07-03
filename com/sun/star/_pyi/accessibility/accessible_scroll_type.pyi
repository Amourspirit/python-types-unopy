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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.accessibility
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class AccessibleScrollType(Enum):
    """
    Enum

    

    See Also:
        `API AccessibleScrollType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1accessibility.html#a8c72ce09bd8167944fb5c7a237420e74>`_
    """
    typeName: str = 'com.sun.star.accessibility.AccessibleScrollType'

    SCROLL_ANYWHERE: 'uno.Enum'
    """
    Scroll the object or string such that as much as possible of the object or string is within the top level window.
    """
    SCROLL_BOTTOM_EDGE: 'uno.Enum'
    """
    Scroll the bottom edge of the object or string such that the bottom edge is within the top level window.
    """
    SCROLL_BOTTOM_RIGHT: 'uno.Enum'
    """
    Scroll the bottom right corner of the object or string such that the bottom right corner is within the top level window.
    """
    SCROLL_LEFT_EDGE: 'uno.Enum'
    """
    Scroll the left edge of the object or string such that the left edge is within the top level window.
    """
    SCROLL_RIGHT_EDGE: 'uno.Enum'
    """
    Scroll the right edge of the object or string such that the right edge is within the top level window.
    """
    SCROLL_TOP_EDGE: 'uno.Enum'
    """
    Scroll the top edge of the object or string such that the top edge is within the top level window.
    """
    SCROLL_TOP_LEFT: 'uno.Enum'
    """
    Scroll the top left corner of the object or string such that the top left corner is within the top level window.
    """

