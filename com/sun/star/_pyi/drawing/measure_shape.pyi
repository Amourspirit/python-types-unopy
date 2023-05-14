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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.drawing
import typing
from .line_properties import LineProperties as LineProperties_f13f0da9
from .measure_properties import MeasureProperties as MeasureProperties_1d340ef3
from .rotation_descriptor import RotationDescriptor as RotationDescriptor_2cec0f63
from .shadow_properties import ShadowProperties as ShadowProperties_e350e87
from .shape import Shape as Shape_85cc09e5
from .text import Text as Text_7c140999
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e

class MeasureShape(LineProperties_f13f0da9, MeasureProperties_1d340ef3, RotationDescriptor_2cec0f63, ShadowProperties_e350e87, Shape_85cc09e5, Text_7c140999):
    """
    Service Class

    This service is for a dimensioning shape.

    See Also:
        `API MeasureShape <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1MeasureShape.html>`_
    """
    @property
    def EndPosition(self) -> 'Point_5fb2085e':
        """
        this point is the end of the measured distance
        """
        ...
    @EndPosition.setter
    def EndPosition(self, value: 'Point_5fb2085e') -> None:
        ...
    @property
    def StartPosition(self) -> 'Point_5fb2085e':
        """
        this point is the start of the measured distance
        """
        ...
    @StartPosition.setter
    def StartPosition(self, value: 'Point_5fb2085e') -> None:
        ...

