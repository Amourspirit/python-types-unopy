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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
from __future__ import annotations
import typing

from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .docking_data import DockingData as DockingData_98da0a8d
    from .docking_event import DockingEvent as DockingEvent_a4210b15
    from .end_docking_event import EndDockingEvent as EndDockingEvent_c6400c2c
    from .end_popup_mode_event import EndPopupModeEvent as EndPopupModeEvent_e0bd0d06
    from ..lang.event_object import EventObject as EventObject_a3d70b03


class XDockableWindowListener(XEventListener_c7230c4a):
    """
    makes it possible to receive docking events.

    See Also:
        `API XDockableWindowListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XDockableWindowListener.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.awt.XDockableWindowListener'

    def closed(self, e: EventObject_a3d70b03) -> None:
        """
        is invoked when the window was actively closed
        """
        ...
    def docking(self, e: DockingEvent_a4210b15) -> DockingData_98da0a8d:
        """
        is invoked during the docking procedure when the window has been moved.
        
        on return the DockingData must contain either the old tracking rectangle or a changed rectangle if required, additionally it must indicate if the window should be docked or floating
        
        Note: the tracking rectangle indicates to the user where the window would be placed if he releases the mouse.
        """
        ...
    def endDocking(self, e: EndDockingEvent_c6400c2c) -> None:
        """
        is invoked when the docking procedure ends.
        
        aWindowRect contains the new position and size of the window
        """
        ...
    def endPopupMode(self, e: EndPopupModeEvent_e0bd0d06) -> None:
        """
        is invoked when the window currently is in pop-up mode and wants to be undocked or closed
        """
        ...
    def prepareToggleFloatingMode(self, e: EventObject_a3d70b03) -> bool:
        """
        is invoked when the floating mode is about to be changed between floating and docked or vice versa
        
        if returned FALSE the floating mode will not be changed
        """
        ...
    def startDocking(self, e: DockingEvent_a4210b15) -> None:
        """
        is invoked when the docking procedure starts.
        """
        ...
    def toggleFloatingMode(self, e: EventObject_a3d70b03) -> None:
        """
        is invoked when the floating mode is changed between floating and docked or vice versa
        """
        ...


