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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2
from typing_extensions import Literal
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .point import Point as Point_5fb2085e
from .rectangle import Rectangle as Rectangle_84b109e9


class DockingEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies a docking event.

    See Also:
        `API DockingEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1DockingEvent.html>`_
    """
    typeName: Literal['com.sun.star.awt.DockingEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., TrackingRectangle: typing.Optional[Rectangle_84b109e9] = ..., MousePos: typing.Optional[Point_5fb2085e] = ..., bLiveMode: typing.Optional[bool] = ..., bInteractive: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            TrackingRectangle (Rectangle, optional): TrackingRectangle value.
            MousePos (Point, optional): MousePos value.
            bLiveMode (bool, optional): bLiveMode value.
            bInteractive (bool, optional): bInteractive value.
        """
        ...


    @property
    def TrackingRectangle(self) -> Rectangle_84b109e9:
        """
        specifies the current tracking rectangle
        """
        ...


    @property
    def MousePos(self) -> Point_5fb2085e:
        """
        specifies the current mouse position in frame coordinates
        """
        ...


    @property
    def bLiveMode(self) -> bool:
        """
        specifies if the layout should be adjusted immediately
        """
        ...


    @property
    def bInteractive(self) -> bool:
        """
        specifies if the docking procedure is interactive which means that the user is currently dragging the window to a new position if this member is FALSE the window will be docked or undocked immediately using the returned tracking rectangle
        """
        ...


