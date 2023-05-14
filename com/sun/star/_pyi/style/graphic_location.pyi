# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.style
# Libre Office Version: 7.4
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class GraphicLocation(Enum):
    """
    Enum

    

    See Also:
        `API GraphicLocation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style.html#ae71ca73feb713866e85597329dfaec2e>`_
    """
    typeName: str = 'com.sun.star.style.GraphicLocation'

    AREA: 'uno.Enum'
    """
    The graphic is scaled to fill the whole surrounding area.
    """
    LEFT_BOTTOM: 'uno.Enum'
    """
    The graphic is located in the bottom left corner.
    """
    LEFT_MIDDLE: 'uno.Enum'
    """
    The graphic is located in the middle of the left edge.
    """
    LEFT_TOP: 'uno.Enum'
    """
    The graphic is located in the top left corner.
    """
    MIDDLE_BOTTOM: 'uno.Enum'
    """
    The graphic is located in the middle of the bottom edge.
    """
    MIDDLE_MIDDLE: 'uno.Enum'
    """
    The graphic is located at the center of the surrounding object.
    """
    MIDDLE_TOP: 'uno.Enum'
    """
    The graphic is located in the middle of the top edge.
    """
    NONE: 'uno.Enum'
    """
    No column or page break is applied.
    
    This value specifies that a location is not yet assigned.
    """
    RIGHT_BOTTOM: 'uno.Enum'
    """
    The graphic is located in the bottom right corner.
    """
    RIGHT_MIDDLE: 'uno.Enum'
    """
    The graphic is located in the middle of the right edge.
    """
    RIGHT_TOP: 'uno.Enum'
    """
    The graphic is located in the top right corner.
    """
    TILED: 'uno.Enum'
    """
    The graphic is repeatedly spread over the surrounding object like tiles.
    """

