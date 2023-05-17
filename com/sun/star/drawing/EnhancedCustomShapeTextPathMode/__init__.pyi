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
import uno
"""
Enum

ENUM EnhancedCustomShapeTextPathMode

See Also:
    `API EnhancedCustomShapeTextPathMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a0babaeb0d04df312f158184b26a302d6>`_
"""
typeName: str = 'com.sun.star.drawing.EnhancedCustomShapeTextPathMode'

NORMAL: EnhancedCustomShapeTextPathMode = ...
"""
the text is drawn along the path without scaling.

the point is normal, from the curve discussion view.
"""
PATH: EnhancedCustomShapeTextPathMode = ...
"""
the text is fit to the path.
"""
SHAPE: EnhancedCustomShapeTextPathMode = ...
"""
the text is fit to the bounding box of the shape.
"""

