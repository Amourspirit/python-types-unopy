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
    from .line_dash import LineDash as LineDash_a54e0afc
    from .poly_polygon_bezier_coords import PolyPolygonBezierCoords as PolyPolygonBezierCoords_7ec5114b
    from ..util.color import Color as Color_68e908c5
    from com.sun.star.drawing.LineCap import LineCapProto  # type: ignore
    from com.sun.star.drawing.LineJoint import LineJointProto  # type: ignore
    from com.sun.star.drawing.LineStyle import LineStyleProto  # type: ignore

class LineProperties(ABC):
    """
    Service Class

    This is a set of properties to describe the style for rendering a Line.
    
    The properties for line ends and line starts are only supported by shapes with open line ends.

    See Also:
        `API LineProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1LineProperties.html>`_
    """
    @property
    def LineCap(self) -> LineCapProto:
        """
        This property defines the rendering of ends of thick lines.
        """
        ...
    @LineCap.setter
    def LineCap(self, value: LineCapProto) -> None:
        ...
    @property
    def LineColor(self) -> Color_68e908c5:
        """
        This property contains the line color.
        """
        ...
    @LineColor.setter
    def LineColor(self, value: Color_68e908c5) -> None:
        ...
    @property
    def LineDash(self) -> LineDash_a54e0afc:
        """
        This property contains the dash of the line.
        """
        ...
    @LineDash.setter
    def LineDash(self, value: LineDash_a54e0afc) -> None:
        ...
    @property
    def LineDashName(self) -> str:
        """
        This property contains the name of the dash of the line.
        """
        ...
    @LineDashName.setter
    def LineDashName(self, value: str) -> None:
        ...
    @property
    def LineEnd(self) -> PolyPolygonBezierCoords_7ec5114b:
        """
        This property contains the line end in the form of a poly polygon Bezier.
        """
        ...
    @LineEnd.setter
    def LineEnd(self, value: PolyPolygonBezierCoords_7ec5114b) -> None:
        ...
    @property
    def LineEndCenter(self) -> bool:
        """
        If this property is TRUE, the line will end in the center of the polygon.
        """
        ...
    @LineEndCenter.setter
    def LineEndCenter(self, value: bool) -> None:
        ...
    @property
    def LineEndName(self) -> str:
        """
        This property contains the name of the line end poly polygon Bezier.
        
        If this string is empty, no line end polygon is rendered.
        """
        ...
    @LineEndName.setter
    def LineEndName(self, value: str) -> None:
        ...
    @property
    def LineEndWidth(self) -> int:
        """
        This property contains the width of the line end polygon.
        """
        ...
    @LineEndWidth.setter
    def LineEndWidth(self, value: int) -> None:
        ...
    @property
    def LineJoint(self) -> LineJointProto:
        """
        This property defines the rendering of joints between thick lines.
        """
        ...
    @LineJoint.setter
    def LineJoint(self, value: LineJointProto) -> None:
        ...
    @property
    def LineStart(self) -> PolyPolygonBezierCoords_7ec5114b:
        """
        This property contains the line start in the form of a poly polygon Bezier.
        """
        ...
    @LineStart.setter
    def LineStart(self, value: PolyPolygonBezierCoords_7ec5114b) -> None:
        ...
    @property
    def LineStartCenter(self) -> bool:
        """
        If this property is TRUE, the line will start from the center of the polygon.
        """
        ...
    @LineStartCenter.setter
    def LineStartCenter(self, value: bool) -> None:
        ...
    @property
    def LineStartName(self) -> str:
        """
        This property contains the name of the line start poly polygon Bezier.
        
        If this string is empty, no line start polygon is rendered.
        """
        ...
    @LineStartName.setter
    def LineStartName(self, value: str) -> None:
        ...
    @property
    def LineStartWidth(self) -> int:
        """
        This property contains the width of the line start polygon.
        """
        ...
    @LineStartWidth.setter
    def LineStartWidth(self, value: int) -> None:
        ...
    @property
    def LineStyle(self) -> LineStyleProto:
        """
        This property contains the type of the line.
        """
        ...
    @LineStyle.setter
    def LineStyle(self, value: LineStyleProto) -> None:
        ...
    @property
    def LineTransparence(self) -> int:
        """
        This property contains the extent of transparency.
        """
        ...
    @LineTransparence.setter
    def LineTransparence(self, value: int) -> None:
        ...
    @property
    def LineWidth(self) -> int:
        """
        This property contains the width of the line in 1/100th mm.
        """
        ...
    @LineWidth.setter
    def LineWidth(self, value: int) -> None:
        ...