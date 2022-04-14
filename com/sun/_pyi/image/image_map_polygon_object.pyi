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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.image
import typing
from .image_map_object import ImageMapObject as ImageMapObject_d1e20c63
if typing.TYPE_CHECKING:
    from ..drawing.point_sequence import PointSequence as PointSequence_e43f0d37

class ImageMapPolygonObject(ImageMapObject_d1e20c63):
    """
    Service Class

    this service describes a polygon-shaped region inside a HTML image map.

    See Also:
        `API ImageMapPolygonObject <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1image_1_1ImageMapPolygonObject.html>`_
    """
    @property
    def Polygon(self) -> 'PointSequence_e43f0d37':
        """
        This sequence of points outlines the click area of this image map object.
        """


