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
# Namespace: com.sun.star.text
# Libre Office Version: 7.4
from __future__ import annotations
from typing import cast
from com.sun.star import UnoEnumProto

class RubyAdjustProto(UnoEnumProto):
    BLOCK: UnoEnumProto
    CENTER: UnoEnumProto
    INDENT_BLOCK: UnoEnumProto
    LEFT: UnoEnumProto
    RIGHT: UnoEnumProto

BLOCK: RubyAdjustProto
"""
adjusted to both borders / stretched
"""
CENTER: RubyAdjustProto
"""
the object is adjusted to the center.

centric adjusted.
"""
INDENT_BLOCK: RubyAdjustProto
"""
adjusted to both borders except for a small indent on both sides
"""
LEFT: RubyAdjustProto
"""
the object is left adjusted.

text flows to the left side of the object.

adjusted to the left.
"""
RIGHT: RubyAdjustProto
"""
the object is right adjusted.

text flows to the right side of the object.

adjusted to the right.
"""

