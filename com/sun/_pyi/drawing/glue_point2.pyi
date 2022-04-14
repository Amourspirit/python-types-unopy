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
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing
from ..awt.point import Point as Point_5fb2085e
from .alignment import Alignment as Alignment_b1400b93
from .escape_direction import EscapeDirection as EscapeDirection_fdc50de6


class GluePoint2(object):
    """
    Struct Class

    This struct defines the attributes of a glue point.
    
    A glue point is a position inside a drawing shape where an edge of a connector shape can be connected.

    See Also:
        `API GluePoint2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1GluePoint2.html>`_
    """
    typeName: Literal['com.sun.star.drawing.GluePoint2']

    def __init__(self, Position: typing.Optional[Point_5fb2085e] = ..., IsRelative: typing.Optional[bool] = ..., PositionAlignment: typing.Optional[Alignment_b1400b93] = ..., Escape: typing.Optional[EscapeDirection_fdc50de6] = ..., IsUserDefined: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Position (Point, optional): Position value.
            IsRelative (bool, optional): IsRelative value.
            PositionAlignment (Alignment, optional): PositionAlignment value.
            Escape (EscapeDirection, optional): Escape value.
            IsUserDefined (bool, optional): IsUserDefined value.
        """


    @property
    def Position(self) -> Point_5fb2085e:
        """
        This is the position of this glue point.
        
        Depending on the flag IsRelative, this is either in 1/100cm or in 1/100%.
        """


    @property
    def IsRelative(self) -> bool:
        """
        if this flag is set to true, the position of this glue point is given in 1/100% values instead of 1/100cm.
        """


    @property
    def PositionAlignment(self) -> Alignment_b1400b93:
        """
        if this glue points position is not relative, this enum specifies the vertical and horizontal alignment of this point.
        
        The alignment specifies how the glue point is moved if the shape is resized.
        """


    @property
    def Escape(self) -> EscapeDirection_fdc50de6:
        """
        this member specifies the escape direction for a glue point.
        
        The escape direction is the direction the connecting line escapes the shape.
        """


    @property
    def IsUserDefined(self) -> bool:
        """
        if this flag is set to false, this is a default glue point.
        
        Some shapes may have default glue points attached to them which cannot be altered or removed.
        """



__all__ = ['GluePoint2']
