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
from abc import ABC
if typing.TYPE_CHECKING:
    from ..util.color import Color as Color_68e908c5

class ShadowProperties(ABC):
    """
    Service Class

    This is a set of properties to describe the style for rendering a shadow.

    See Also:
        `API ShadowProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1ShadowProperties.html>`_
    """
    @property
    def Shadow(self) -> bool:
        """
        enables/disables the shadow of a Shape.
        
        The other shadow properties are only applied if this is set to TRUE.
        """
        ...
    @Shadow.setter
    def Shadow(self, value: bool) -> None:
        ...
    @property
    def ShadowBlur(self) -> int:
        """
        This defines the degree of blur of the shadow in points.
        """
        ...
    @ShadowBlur.setter
    def ShadowBlur(self, value: int) -> None:
        ...
    @property
    def ShadowColor(self) -> 'Color_68e908c5':
        """
        This is the color of the shadow of this Shape.
        """
        ...
    @ShadowColor.setter
    def ShadowColor(self, value: 'Color_68e908c5') -> None:
        ...
    @property
    def ShadowTransparence(self) -> int:
        """
        This defines the degree of transparence of the shadow in percent.
        """
        ...
    @ShadowTransparence.setter
    def ShadowTransparence(self, value: int) -> None:
        ...
    @property
    def ShadowXDistance(self) -> int:
        """
        This is the horizontal distance of the left edge of the Shape to the shadow.
        """
        ...
    @ShadowXDistance.setter
    def ShadowXDistance(self, value: int) -> None:
        ...
    @property
    def ShadowYDistance(self) -> int:
        """
        This is the vertical distance of the top edge of the Shape to the shadow.
        """
        ...
    @ShadowYDistance.setter
    def ShadowYDistance(self, value: int) -> None:
        ...

