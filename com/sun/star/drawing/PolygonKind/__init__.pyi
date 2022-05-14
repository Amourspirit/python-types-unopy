# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
"""
Enum



See Also:
    `API PolygonKind <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#adec70dcaa1fdfc08f03cf30ccee65ef6>`_
"""

FREEFILL: 'uno.Enum'
"""
This is the PolygonKind for a ClosedFreeHandShape.
"""
FREELINE: 'uno.Enum'
"""
This is the PolygonKind for an OpenFreeHandShape.
"""
LINE: 'uno.Enum'
"""
the ConnectorShape is drawn as a straight line

This is the PolygonKind for a LineShape.
"""
PATHFILL: 'uno.Enum'
"""
This is the PolygonKind for a ClosedBezierShape.
"""
PATHLINE: 'uno.Enum'
"""
This is the PolygonKind for an OpenBezierShape.
"""
PATHPLIN: 'uno.Enum'
"""
This is the PolygonKind for a PolyLinePathShape.
"""
PATHPOLY: 'uno.Enum'
"""
This is the PolygonKind for a PolyPolygonPathShape.
"""
PLIN: 'uno.Enum'
"""
This is the PolygonKind for a PolyLineShape.
"""
POLY: 'uno.Enum'
"""
This is the PolygonKind for a PolyPolygonShape.
"""
