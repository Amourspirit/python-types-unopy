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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.script
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .script_event_descriptor import ScriptEventDescriptor as ScriptEventDescriptor_4cef1033
    from .x_script_listener import XScriptListener as XScriptListener_f20b0db0

class XEventAttacherManager(XInterface_8f010a43):
    """
    registers listeners for specified events.

    See Also:
        `API XEventAttacherManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XEventAttacherManager.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.script.XEventAttacherManager']

    def addScriptListener(self, xListener: 'XScriptListener_f20b0db0') -> None:
        """
        adds an XScriptListener that will be notified when an event takes place.
        
        For that a ScriptEventDescriptor is registered at and attached to an object by an XEventAttacherManager.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def attach(self, nIndex: int, xObject: 'XInterface_8f010a43', aHelper: object) -> None:
        """
        attaches all the ScriptEvents which are registered for the given index to the given object.
        
        Exceptions of type com.sun.star.beans.IntrospectionException and com.sun.star.script.CannotCreateAdapterException that can be thrown by methods of XEventAttacher are caught and ignored.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.ServiceNotRegisteredException: ``ServiceNotRegisteredException``
        """
    def detach(self, nIndex: int, xObject: 'XInterface_8f010a43') -> None:
        """
        detaches all the ScriptEvents from the given object which are registered at this object for the given index.
        
        Exceptions of type com.sun.star.beans.IntrospectionException and com.sun.star.script.CannotCreateAdapterException that can be thrown by methods of XEventAttacher are caught and ignored.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def getScriptEvents(self, Index: int) -> 'typing.Tuple[ScriptEventDescriptor_4cef1033, ...]':
        """

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def insertEntry(self, nIndex: int) -> None:
        """
        creates an empty entry at the given position.
        
        The index n of all entries with n &gt;= nIndex will be increased by one.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def registerScriptEvent(self, nIndex: int, aScriptEvent: 'ScriptEventDescriptor_4cef1033') -> None:
        """
        registers one event for an object identified by its index.
        
        If any object is attached under this index, then this event is attached automatically.
        
        Exceptions of type com.sun.star.beans.IntrospectionException and com.sun.star.script.CannotCreateAdapterException that can be thrown by methods of XEventAttacher are caught and ignored.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def registerScriptEvents(self, nIndex: int, aScriptEvents: 'typing.Tuple[ScriptEventDescriptor_4cef1033, ...]') -> None:
        """
        registers several events for an object identified by its index.
        
        The result is the same as if the method registerScriptEvent() was called once for each ScriptEventDescriptor in the sequence.
        
        If any object is attached under this index, then this event is attached automatically (see attach())
        
        Exceptions of type com.sun.star.beans.IntrospectionException and com.sun.star.script.CannotCreateAdapterException that can be thrown by methods of XEventAttacher are caught and ignored.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def removeEntry(self, nIndex: int) -> None:
        """
        removes the entry at the given position.
        
        If any events are registered at this index, they will be revoked, too. So if the events at this index have been attached to any object they are detached automatically. (see attach()).

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def removeScriptListener(self, Listener: 'XScriptListener_f20b0db0') -> None:
        """
        removes a XScriptListener from the listener list.
        
        Nothing happens if the listener is not registered.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def revokeScriptEvent(self, nIndex: int, aListenerType: str, aEventMethod: str, aRemoveListenerParam: str) -> None:
        """
        revokes the registration of an event.
        
        The parameters ListenerType and EventMethod are equivalent to the first two members of the ScriptEventDescriptor used to register events. If this event at this index has been attached to any object, it is detached automatically (see attach()).
        
        Exceptions of type com.sun.star.beans.IntrospectionException and com.sun.star.script.CannotCreateAdapterException that can be thrown by methods of XEventAttacher are caught and ignored.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def revokeScriptEvents(self, nIndex: int) -> None:
        """
        revokes all events which are registered for the given index.
        
        If the events at this index have been attached to any object, they are detached automatically. (see attach()).

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

__all__ = ['XEventAttacherManager']

