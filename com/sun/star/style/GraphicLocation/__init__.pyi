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
from __future__ import annotations
import uno
from com.sun.star._pyi.style.graphic_location import GraphicLocation as PyiGraphicLocation
"""
Enum


See Also:
    `API GraphicLocation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1style.html#ae71ca73feb713866e85597329dfaec2e>`_
"""
typeName: str = 'com.sun.star.style.GraphicLocation'

AREA: PyiGraphicLocation = ...
"""
The graphic is scaled to fill the whole surrounding area.
"""
LEFT_BOTTOM: PyiGraphicLocation = ...
"""
The graphic is located in the bottom left corner.
"""
LEFT_MIDDLE: PyiGraphicLocation = ...
"""
The graphic is located in the middle of the left edge.
"""
LEFT_TOP: PyiGraphicLocation = ...
"""
The graphic is located in the top left corner.
"""
MIDDLE_BOTTOM: PyiGraphicLocation = ...
"""
The graphic is located in the middle of the bottom edge.
"""
MIDDLE_MIDDLE: PyiGraphicLocation = ...
"""
The graphic is located at the center of the surrounding object.
"""
MIDDLE_TOP: PyiGraphicLocation = ...
"""
The graphic is located in the middle of the top edge.
"""
NONE: PyiGraphicLocation = ...
"""
No column or page break is applied.

This value specifies that a location is not yet assigned.
"""
RIGHT_BOTTOM: PyiGraphicLocation = ...
"""
The graphic is located in the bottom right corner.
"""
RIGHT_MIDDLE: PyiGraphicLocation = ...
"""
The graphic is located in the middle of the right edge.
"""
RIGHT_TOP: PyiGraphicLocation = ...
"""
The graphic is located in the top right corner.
"""
TILED: PyiGraphicLocation = ...
"""
The graphic is repeatedly spread over the surrounding object like tiles.
"""

