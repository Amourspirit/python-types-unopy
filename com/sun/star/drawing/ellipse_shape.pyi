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
from __future__ import annotations
import typing
from .fill_properties import FillProperties as FillProperties_f1200da8
from .line_properties import LineProperties as LineProperties_f13f0da9
from .rotation_descriptor import RotationDescriptor as RotationDescriptor_2cec0f63
from .shadow_properties import ShadowProperties as ShadowProperties_e350e87
from .shape import Shape as Shape_85cc09e5
from .text import Text as Text_7c140999
if typing.TYPE_CHECKING:
    from com.sun.star.drawing.CircleKind import CircleKindProto  # type: ignore

class EllipseShape(FillProperties_f1200da8, LineProperties_f13f0da9, RotationDescriptor_2cec0f63, ShadowProperties_e350e87, Shape_85cc09e5, Text_7c140999):
    """
    Service Class

    This service is for an ellipse or circle shape.

    See Also:
        `API EllipseShape <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1EllipseShape.html>`_
    """
    @property
    def CircleEndAngle(self) -> int:
        """
        If the kind specifies an open circle, this is the end angle.
        """
        ...
    @CircleEndAngle.setter
    def CircleEndAngle(self, value: int) -> None:
        ...
    @property
    def CircleKind(self) -> CircleKindProto:
        """
        This is the kind of circle.
        """
        ...
    @CircleKind.setter
    def CircleKind(self, value: CircleKindProto) -> None:
        ...
    @property
    def CircleStartAngle(self) -> int:
        """
        If the kind specifies an open circle, this is the start angle.
        """
        ...
    @CircleStartAngle.setter
    def CircleStartAngle(self, value: int) -> None:
        ...