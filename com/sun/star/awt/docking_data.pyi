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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt
# Libre Office Version: 2024.2
import typing
from .rectangle import Rectangle as Rectangle_84b109e9


class DockingData(object):
    """
    Struct Class

    data returned by docking handler

    See Also:
        `API DockingData <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1DockingData.html>`_
    """
    typeName: str = 'com.sun.star.awt.DockingData'

    def __init__(self, TrackingRectangle: typing.Optional[Rectangle_84b109e9] = ..., bFloating: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            TrackingRectangle (Rectangle, optional): TrackingRectangle value.
            bFloating (bool, optional): bFloating value.
        """
        ...

    @property
    def TrackingRectangle(self) -> Rectangle_84b109e9:
        """
        specifies the position and size where the window would be placed if the user releases the mouse
        """
        ...
    @TrackingRectangle.setter
    def TrackingRectangle(self, value: Rectangle_84b109e9) -> None:
        ...
    @property
    def bFloating(self) -> bool:
        """
        specifies that the window should be floating (TRUE) or docked (FALSE)
        """
        ...
    @bFloating.setter
    def bFloating(self, value: bool) -> None:
        ...

