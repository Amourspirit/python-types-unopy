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
# Namespace: com.sun.star.util
from __future__ import annotations
import typing

from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from ..lang.event_object import EventObject as EventObject_a3d70b03


class XCloseListener(XEventListener_c7230c4a):
    """
    makes it possible to receive events when an object is called for closing
    
    Such close events are broadcasted by a XCloseBroadcaster if somewhere tries to close it by calling XCloseable.close(). Listener can:
    
    If an event com.sun.star.lang.XEventListener.disposing() occurred, nobody called XCloseable.close() on listened object before. Then it's not allowed to break this request - it must be accepted!

    See Also:
        `API XCloseListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XCloseListener.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.util.XCloseListener'

    def notifyClosing(self, Source: EventObject_a3d70b03) -> None:
        """
        is called when the listened object is closed really
        
        Now the listened object is closed really. Listener has to accept that; should deregister himself and release all references to it. It's not allowed nor possible to disagree with that by throwing any exception.
        
        If the event com.sun.star.lang.XEventListener.disposing() occurred before it must be accepted too. There exist no chance for a disagreement any more.
        """
        ...
    def queryClosing(self, Source: EventObject_a3d70b03, GetsOwnership: bool) -> None:
        """
        is called when somewhere tries to close listened object
        
        Is called before XCloseListener.notifyClosing(). Listener has the chance to break that by throwing a CloseVetoException. This exception must be passed to the original caller of XCloseable.close() without any interaction.
        
        The parameter GetsOwnership regulate who has to try to close the listened object again, if this listener disagree with the request by throwing the exception. If it's set to FALSE the original caller of XCloseable.close() will be the owner in every case. It's not allowed to call close() from this listener then. If it's set to TRUE this listener will be the new owner if he throw the exception, otherwise not! If his still running processes will be finished he must call close() on listened object again then.
        
        If this listener doesn't disagree with th close request it depends from his internal implementation if he deregister himself at the listened object. But normally this must be done in XCloseListener.notifyClosing().

        Raises:
            CloseVetoException: ``CloseVetoException``
        """
        ...


