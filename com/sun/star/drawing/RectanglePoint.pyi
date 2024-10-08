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


class RectanglePointProto(Protocol):
    """Protocol for RectanglePoint"""

    @property
    def typeName(self) -> Literal["com.sun.star.drawing.RectanglePoint"]:
        ...
    value: Any
    LEFT_BOTTOM: RectanglePointProto
    LEFT_MIDDLE: RectanglePointProto
    LEFT_TOP: RectanglePointProto
    MIDDLE_BOTTOM: RectanglePointProto
    MIDDLE_MIDDLE: RectanglePointProto
    MIDDLE_TOP: RectanglePointProto
    RIGHT_BOTTOM: RectanglePointProto
    RIGHT_MIDDLE: RectanglePointProto
    RIGHT_TOP: RectanglePointProto

LEFT_BOTTOM: RectanglePointProto
"""
specify to the point on the bottom of the left side from the rectangle.
"""
LEFT_MIDDLE: RectanglePointProto
"""
specify to the point on the middle of the left side from the rectangle.
"""
LEFT_TOP: RectanglePointProto
"""
specify to the point on the left side from the top of the rectangle.
"""
MIDDLE_BOTTOM: RectanglePointProto
"""
specify to the point on the middle of the bottom from the rectangle.
"""
MIDDLE_MIDDLE: RectanglePointProto
"""
specify to the point on the center from the rectangle.
"""
MIDDLE_TOP: RectanglePointProto
"""
specify to the point on the middle of the top from the rectangle.
"""
RIGHT_BOTTOM: RectanglePointProto
"""
specify to the point on the bottom of the right side from the rectangle.
"""
RIGHT_MIDDLE: RectanglePointProto
"""
specify to the point on the middle of the right side from the rectangle.
"""
RIGHT_TOP: RectanglePointProto
"""
specify to the point on the right side from the top of the rectangle.
"""

