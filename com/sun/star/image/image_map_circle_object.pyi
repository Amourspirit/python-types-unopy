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
# Namespace: com.sun.star.image
from __future__ import annotations
import typing
from .image_map_object import ImageMapObject as ImageMapObject_d1e20c63
if typing.TYPE_CHECKING:
    from ..awt.point import Point as Point_5fb2085e

class ImageMapCircleObject(ImageMapObject_d1e20c63):
    """
    Service Class

    this service describes a circular-shaped region inside a HTML image map.

    See Also:
        `API ImageMapCircleObject <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1image_1_1ImageMapCircleObject.html>`_
    """
    @property
    def Center(self) -> Point_5fb2085e:
        """
        This is the center point of the circle in pixels.
        """
        ...
    @Center.setter
    def Center(self, value: Point_5fb2085e) -> None:
        ...
    @property
    def Radius(self) -> int:
        """
        This is the radius of the circle in pixels.
        """
        ...
    @Radius.setter
    def Radius(self, value: int) -> None:
        ...

