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
from typing import Protocol, Any
from typing_extensions import Literal


class PolygonKindProto(Protocol):
    """Protocol for PolygonKind"""

    @property
    def typeName(self) -> Literal["com.sun.star.drawing.PolygonKind"]:
        ...
    value: Any
    FREEFILL: PolygonKindProto
    FREELINE: PolygonKindProto
    LINE: PolygonKindProto
    PATHFILL: PolygonKindProto
    PATHLINE: PolygonKindProto
    PATHPLIN: PolygonKindProto
    PATHPOLY: PolygonKindProto
    PLIN: PolygonKindProto
    POLY: PolygonKindProto

FREEFILL: PolygonKindProto
"""
This is the PolygonKind for a ClosedFreeHandShape.
"""
FREELINE: PolygonKindProto
"""
This is the PolygonKind for an OpenFreeHandShape.
"""
LINE: PolygonKindProto
"""
the ConnectorShape is drawn as a straight line

This is the PolygonKind for a LineShape.
"""
PATHFILL: PolygonKindProto
"""
This is the PolygonKind for a ClosedBezierShape.
"""
PATHLINE: PolygonKindProto
"""
This is the PolygonKind for an OpenBezierShape.
"""
PATHPLIN: PolygonKindProto
"""
This is the PolygonKind for a PolyLinePathShape.
"""
PATHPOLY: PolygonKindProto
"""
This is the PolygonKind for a PolyPolygonPathShape.
"""
PLIN: PolygonKindProto
"""
This is the PolygonKind for a PolyLineShape.
"""
POLY: PolygonKindProto
"""
This is the PolygonKind for a PolyPolygonShape.
"""

