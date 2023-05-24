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
    from ..lang.event_object import EventObject as EventObject_a3d70b03


class XTopWindowListener(XEventListener_c7230c4a):
    """
    makes it possible to receive window events.

    See Also:
        `API XTopWindowListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XTopWindowListener.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.awt.XTopWindowListener'

    def windowActivated(self, e: EventObject_a3d70b03) -> None:
        """
        is invoked when a window is activated.
        """
        ...
    def windowClosed(self, e: EventObject_a3d70b03) -> None:
        """
        is invoked when a window has been closed.
        """
        ...
    def windowClosing(self, e: EventObject_a3d70b03) -> None:
        """
        is invoked when a window is in the process of being closed.
        
        The close operation can be overridden at this point.
        """
        ...
    def windowDeactivated(self, e: EventObject_a3d70b03) -> None:
        """
        is invoked when a window is deactivated.
        """
        ...
    def windowMinimized(self, e: EventObject_a3d70b03) -> None:
        """
        is invoked when a window is iconified.
        """
        ...
    def windowNormalized(self, e: EventObject_a3d70b03) -> None:
        """
        is invoked when a window is deiconified.
        """
        ...
    def windowOpened(self, e: EventObject_a3d70b03) -> None:
        """
        is invoked when a window has been opened.
        """
        ...


