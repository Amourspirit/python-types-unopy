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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.drawing
from __future__ import annotations
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from .point_sequence_sequence import PointSequenceSequence as PointSequenceSequence_5c591070
    from com.sun.star.drawing.PolygonKind import PolygonKindProto  # type: ignore

class PolyPolygonDescriptor(ABC):
    """
    Service Class

    This service describes a poly-polygon.
    
    A poly-polygon consists of multiple polygons combined in one.

    See Also:
        `API PolyPolygonDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1PolyPolygonDescriptor.html>`_
    """
    @property
    def Geometry(self) -> PointSequenceSequence_5c591070:
        """
        These are the untransformed points of this polygon.
        """
        ...
    @Geometry.setter
    def Geometry(self, value: PointSequenceSequence_5c591070) -> None:
        ...
    @property
    def PolyPolygon(self) -> PointSequenceSequence_5c591070:
        """
        These are the reference points for this polygon.
        """
        ...
    @PolyPolygon.setter
    def PolyPolygon(self, value: PointSequenceSequence_5c591070) -> None:
        ...
    @property
    def PolygonKind(self) -> PolygonKindProto:
        """
        This is the type of polygon.
        """
        ...
    @PolygonKind.setter
    def PolygonKind(self, value: PolygonKindProto) -> None:
        ...