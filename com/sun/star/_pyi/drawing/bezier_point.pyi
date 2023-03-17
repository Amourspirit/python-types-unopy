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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing
from ..awt.point import Point as Point_5fb2085e


class BezierPoint(object):
    """
    Struct Class

    This is a point on a Bezier curve.
    
    The two control points specify how the Bezier curve goes through the given position.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API BezierPoint <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1BezierPoint.html>`_
    """
    typeName: Literal['com.sun.star.drawing.BezierPoint']

    def __init__(self, Position: typing.Optional[Point_5fb2085e] = ..., ControlPoint1: typing.Optional[Point_5fb2085e] = ..., ControlPoint2: typing.Optional[Point_5fb2085e] = ...) -> None:
        """
        Constructor

        Arguments:
            Position (Point, optional): Position value.
            ControlPoint1 (Point, optional): ControlPoint1 value.
            ControlPoint2 (Point, optional): ControlPoint2 value.
        """
        ...


    @property
    def Position(self) -> Point_5fb2085e:
        """
        This is the position of this point.
        """
        ...


    @property
    def ControlPoint1(self) -> Point_5fb2085e:
        """
        This is the position of the first control point.
        """
        ...


    @property
    def ControlPoint2(self) -> Point_5fb2085e:
        """
        This is the position of the second control point.
        """
        ...


