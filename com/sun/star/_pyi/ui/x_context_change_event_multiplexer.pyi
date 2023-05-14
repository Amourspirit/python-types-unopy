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
# Namespace: com.sun.star.ui
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .context_change_event_object import ContextChangeEventObject as ContextChangeEventObject_37b70f6a
    from .x_context_change_event_listener import XContextChangeEventListener as XContextChangeEventListener_678510b1

class XContextChangeEventMultiplexer(XInterface_8f010a43):
    """
    Provide a central access point for a group of events.
    
    Listeners can be added with a simple restriction on the event source. They are only called for events that originate at the specified source.
    
    Event providers can broadcast an event to all interested listeners.
    
    The XEventMultiplexer interface is typically implemented as a singleton

    See Also:
        `API XContextChangeEventMultiplexer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XContextChangeEventMultiplexer.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ui.XContextChangeEventMultiplexer']

    def addContextChangeEventListener(self, xListener: 'XContextChangeEventListener_678510b1', xEventFocus: 'XInterface_8f010a43') -> None:
        """
        Add an event listener that is called only when events are broadcast for the specified event focus.
        
        One listener may be added more than once for different event foci. Adding a listener a second time for the same event focus results in an InvalidArgumentException.
        
        The event focus may or may not be the source of the event.
        
        A typical example for an event focus is the XController of a view. Using an XController restricts events passed to a listener to events that belong to one view.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def broadcastContextChangeEvent(self, aEvent: 'ContextChangeEventObject_37b70f6a', xEventFocus: 'XInterface_8f010a43') -> None:
        """
        Call all event listeners that were added for the specified event focus.
        """
        ...
    def removeAllContextChangeEventListeners(self, xListener: 'XContextChangeEventListener_678510b1') -> None:
        """
        Remove an event listener for all event foci.
        
        It is not an error when the listener is not registered for any event focus.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def removeContextChangeEventListener(self, xListener: 'XContextChangeEventListener_678510b1', xEventFocus: 'XInterface_8f010a43') -> None:
        """
        Remove an event listener for the specified event focus.
        
        When the same listener was added for other event foci then these associations remain unmodified.
        
        When the listener is not registered for the given event focus then an InvalidArgumentException is thrown.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...


