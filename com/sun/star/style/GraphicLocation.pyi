# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class GraphicLocationProto(Protocol):
    """Protocol for GraphicLocation"""

    @property
    def typeName(self) -> Literal["com.sun.star.style.GraphicLocation"]:
        ...
    value: Any
    AREA: GraphicLocationProto
    LEFT_BOTTOM: GraphicLocationProto
    LEFT_MIDDLE: GraphicLocationProto
    LEFT_TOP: GraphicLocationProto
    MIDDLE_BOTTOM: GraphicLocationProto
    MIDDLE_MIDDLE: GraphicLocationProto
    MIDDLE_TOP: GraphicLocationProto
    NONE: GraphicLocationProto
    RIGHT_BOTTOM: GraphicLocationProto
    RIGHT_MIDDLE: GraphicLocationProto
    RIGHT_TOP: GraphicLocationProto
    TILED: GraphicLocationProto

AREA: GraphicLocationProto
"""
The graphic is scaled to fill the whole surrounding area.
"""
LEFT_BOTTOM: GraphicLocationProto
"""
The graphic is located in the bottom left corner.
"""
LEFT_MIDDLE: GraphicLocationProto
"""
The graphic is located in the middle of the left edge.
"""
LEFT_TOP: GraphicLocationProto
"""
The graphic is located in the top left corner.
"""
MIDDLE_BOTTOM: GraphicLocationProto
"""
The graphic is located in the middle of the bottom edge.
"""
MIDDLE_MIDDLE: GraphicLocationProto
"""
The graphic is located at the center of the surrounding object.
"""
MIDDLE_TOP: GraphicLocationProto
"""
The graphic is located in the middle of the top edge.
"""
NONE: GraphicLocationProto
"""
No column or page break is applied.

This value specifies that a location is not yet assigned.
"""
RIGHT_BOTTOM: GraphicLocationProto
"""
The graphic is located in the bottom right corner.
"""
RIGHT_MIDDLE: GraphicLocationProto
"""
The graphic is located in the middle of the right edge.
"""
RIGHT_TOP: GraphicLocationProto
"""
The graphic is located in the top right corner.
"""
TILED: GraphicLocationProto
"""
The graphic is repeatedly spread over the surrounding object like tiles.
"""

