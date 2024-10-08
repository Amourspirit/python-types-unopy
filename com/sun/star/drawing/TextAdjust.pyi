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
# Namespace: com.sun.star.drawing
# Libre Office Version: 2024.2
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class TextAdjustProto(Protocol):
    """Protocol for TextAdjust"""

    @property
    def typeName(self) -> Literal["com.sun.star.drawing.TextAdjust"]:
        ...
    value: Any
    BLOCK: TextAdjustProto
    CENTER: TextAdjustProto
    LEFT: TextAdjustProto
    RIGHT: TextAdjustProto
    STRETCH: TextAdjustProto

BLOCK: TextAdjustProto
"""
The text extends from the left to the right edge of the shape.

The text extends from the top to the bottom edge of the shape.
"""
CENTER: TextAdjustProto
"""
The text is centered inside the shape.
"""
LEFT: TextAdjustProto
"""
the connection line leaves the connected object to the left,

The left edge of the text is adjusted to the left edge of the shape.

The text is positioned to the left.
"""
RIGHT: TextAdjustProto
"""
the connection line leaves the connected object to the right,

The right edge of the text is adjusted to the right edge of the shape.

The text is positioned to the right.
"""
STRETCH: TextAdjustProto
"""
the bitmap is stretched to fill the area.

The text is stretched so that the longest line goes from the left to the right edge of the shape.
"""

