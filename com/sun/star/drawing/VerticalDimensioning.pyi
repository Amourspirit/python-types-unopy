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


class VerticalDimensioningProto(Protocol):
    """Protocol for VerticalDimensioning"""

    @property
    def typeName(self) -> Literal["com.sun.star.drawing.VerticalDimensioning"]:
        ...
    value: Any
    AUTO: VerticalDimensioningProto
    BOTTOM: VerticalDimensioningProto
    CENTERED: VerticalDimensioningProto
    TOP: VerticalDimensioningProto

AUTO: VerticalDimensioningProto
"""
the connection point is chosen automatically,

Set this to have the application select the best horizontal position for the text.
"""
BOTTOM: VerticalDimensioningProto
"""
the connection line leaves the connected object from the bottom,

The text is positioned below the main line.

The bottom edge of the text is adjusted to the bottom edge of the shape.
"""
CENTERED: VerticalDimensioningProto
"""
The text is positioned at the center.

The text is positioned over the main line.
"""
TOP: VerticalDimensioningProto
"""
the connection line leaves the connected object from the top,

The text is positioned above the main line.

The top edge of the text is adjusted to the top edge of the shape.
"""

