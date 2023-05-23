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
from typing import cast
from com.sun.star import UnoEnumProto

class PageStyleLayoutProto(UnoEnumProto):
    ALL: UnoEnumProto
    LEFT: UnoEnumProto
    MIRRORED: UnoEnumProto
    RIGHT: UnoEnumProto

ALL: PageStyleLayoutProto
"""
The page style is identically used for left and right pages.
"""
LEFT: PageStyleLayoutProto
"""
set the horizontal alignment to the left margin from the container object

The text range is left-aligned between the previous tabulator (or the left border, if none) and this tabulator.

adjusted to the left border

The page style is only used for left pages.
"""
MIRRORED: PageStyleLayoutProto
"""
The page style is used unchanged for left pages and mirrored for right pages.
"""
RIGHT: PageStyleLayoutProto
"""
set the horizontal alignment to the right margin from the container object

The text range is right-aligned between the previous tabulator (or the left border, if none) and this tabulator.

adjusted to the right border

The page style is only used for right pages.
"""

