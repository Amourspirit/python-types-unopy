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
from .hatch_style import HatchStyle as HatchStyle_bcfe0bed
from ..util.color import Color as Color_68e908c5


class Hatch(object):
    """
    Struct Class

    This struct defines the appearance of a hatch.
    
    A hatch is a texture made of straight lines.

    See Also:
        `API Hatch <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1Hatch.html>`_
    """
    typeName: Literal['com.sun.star.drawing.Hatch']

    def __init__(self, Style: typing.Optional[HatchStyle_bcfe0bed] = ..., Color: typing.Optional[Color_68e908c5] = ..., Distance: typing.Optional[int] = ..., Angle: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Style (HatchStyle, optional): Style value.
            Color (Color, optional): Color value.
            Distance (int, optional): Distance value.
            Angle (int, optional): Angle value.
        """
        ...


    @property
    def Style(self) -> HatchStyle_bcfe0bed:
        """
        The HatchStyle defines the kind of lines used to draw this hatch.
        """
        ...


    @property
    def Color(self) -> Color_68e908c5:
        """
        This is the color of the hatch lines.
        """
        ...


    @property
    def Distance(self) -> int:
        """
        This is the distance between the lines in the hatch.
        """
        ...


    @property
    def Angle(self) -> int:
        """
        You can rotate the lines of the hatch with this angle.
        
        Specified in tenths of a degree.
        """
        ...


