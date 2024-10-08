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
# Namespace: com.sun.star.table
# Libre Office Version: 2024.2
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class CellOrientationProto(Protocol):
    """Protocol for CellOrientation"""

    @property
    def typeName(self) -> Literal["com.sun.star.table.CellOrientation"]:
        ...
    value: Any
    BOTTOMTOP: CellOrientationProto
    STACKED: CellOrientationProto
    STANDARD: CellOrientationProto
    TOPBOTTOM: CellOrientationProto

BOTTOMTOP: CellOrientationProto
"""
contents are printed from bottom to top.
"""
STACKED: CellOrientationProto
"""
contents are printed from top to bottom with individual characters in normal (horizontal) orientation.
"""
STANDARD: CellOrientationProto
"""
default alignment is used (left for numbers, right for text).

default alignment is used.

contents are printed from left to right.
"""
TOPBOTTOM: CellOrientationProto
"""
contents are printed from top to bottom.
"""

