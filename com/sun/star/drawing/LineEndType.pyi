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


class LineEndTypeProto(Protocol):
    """Protocol for LineEndType"""

    @property
    def typeName(self) -> Literal["com.sun.star.drawing.LineEndType"]:
        ...
    value: Any
    ARROW: LineEndTypeProto
    CIRCLE: LineEndTypeProto
    NONE: LineEndTypeProto
    SPECIAL: LineEndTypeProto
    SQUARE: LineEndTypeProto

ARROW: LineEndTypeProto
"""
the line uses an arrow for the line end.
"""
CIRCLE: LineEndTypeProto
"""
the line uses a circle for the line end.
"""
NONE: LineEndTypeProto
"""
the area is not filled.

The text size is only defined by the font properties.

Don't animate this text.

the line is hidden.

the joint between lines will not be connected

the line has no special end.
"""
SPECIAL: LineEndTypeProto
"""
not implemented, yet.

deprecated
"""
SQUARE: LineEndTypeProto
"""
the line will get a half square as additional cap

the line uses a square for the line end.
"""

