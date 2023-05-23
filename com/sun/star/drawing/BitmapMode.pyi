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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.4
from __future__ import annotations
from typing import cast
from com.sun.star import UnoEnumProto

class BitmapModeProto(UnoEnumProto):
    NO_REPEAT: UnoEnumProto
    REPEAT: UnoEnumProto
    STRETCH: UnoEnumProto

NO_REPEAT: BitmapModeProto
"""
the bitmap is painted in its original or selected size.
"""
REPEAT: BitmapModeProto
"""
the bitmap is repeated over the fill area.
"""
STRETCH: BitmapModeProto
"""
the bitmap is stretched to fill the area.

The text is stretched so that the longest line goes from the left to the right edge of the shape.
"""

