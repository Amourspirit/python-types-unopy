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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing

from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from ..lang.event_object import EventObject as EventObject_a3d70b03


class XLayoutManagerListener(XEventListener_c7230c4a):
    """
    makes it possible to receive events from a layout manager.
    
    Events are provided only for notification purposes only. All operations are handled internally by the layout manager component, so that GUI layout works properly regardless of whether a component registers such a listener or not.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XLayoutManagerListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XLayoutManagerListener.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.frame.XLayoutManagerListener'

    def layoutEvent(self, aSource: EventObject_a3d70b03, eLayoutEvent: int, aInfo: typing.Any) -> None:
        """
        is invoked when a layout manager has made a certain operation.
        """
        ...


