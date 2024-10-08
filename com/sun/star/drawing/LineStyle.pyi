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


class LineStyleProto(Protocol):
    """Protocol for LineStyle"""

    @property
    def typeName(self) -> Literal["com.sun.star.drawing.LineStyle"]:
        ...
    value: Any
    DASH: LineStyleProto
    NONE: LineStyleProto
    SOLID: LineStyleProto

DASH: LineStyleProto
"""
the line use dashes.
"""
NONE: LineStyleProto
"""
the area is not filled.

The text size is only defined by the font properties.

Don't animate this text.

the line is hidden.

the joint between lines will not be connected

the line has no special end.
"""
SOLID: LineStyleProto
"""
use a solid color to fill the area.

the line is solid.
"""

