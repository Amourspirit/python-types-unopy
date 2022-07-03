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
# Namespace: com.sun.star.document
from typing_extensions import Literal
import typing
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .undo_manager_event import UndoManagerEvent as UndoManagerEvent_1c2d0eba
    from ..lang.event_object import EventObject as EventObject_a3d70b03

class XUndoManagerListener(XEventListener_c7230c4a):
    """
    implemented by components which want to be notified of changes in the Undo/Redo stacks of an Undo manager.
    
    **since**
    
        OOo 3.4

    See Also:
        `API XUndoManagerListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XUndoManagerListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.document.XUndoManagerListener']

    def actionRedone(self, iEvent: 'UndoManagerEvent_1c2d0eba') -> None:
        """
        is called when the top-most action of the Redo stack has been re-applied.
        """
        ...
    def actionUndone(self, iEvent: 'UndoManagerEvent_1c2d0eba') -> None:
        """
        is called when the top-most action of the undo stack has been undone.
        """
        ...
    def allActionsCleared(self, iEvent: 'EventObject_a3d70b03') -> None:
        """
        is called when both the Undo and the Redo stack have been cleared from all Undo actions.
        """
        ...
    def cancelledContext(self, iEvent: 'UndoManagerEvent_1c2d0eba') -> None:
        """
        is called when an Undo context has been left, but no actions have been added within this context.
        
        In such a case, the context which has just been left will not contribute to the undo stack, but instead be silently removed. Consequently, the UndoManagerEvent.UndoActionTitle is empty.
        """
        ...
    def enteredContext(self, iEvent: 'UndoManagerEvent_1c2d0eba') -> None:
        """
        is called when a new Undo context has been entered.
        
        UndoManagerEvent.UndoActionTitle carries the title of the Undo context, and UndoManagerEvent.UndoContextDepth the number of open Undo contexts, including the one just entered.
        """
        ...
    def enteredHiddenContext(self, iEvent: 'UndoManagerEvent_1c2d0eba') -> None:
        """
        is called when a new hidden Undo context has been entered.
        
        UndoManagerEvent.UndoActionTitle carries the title of the Undo context, and UndoManagerEvent.UndoContextDepth the number of open Undo contexts, including the one just entered.
        """
        ...
    def leftContext(self, iEvent: 'UndoManagerEvent_1c2d0eba') -> None:
        """
        is called when an Undo context has been left.
        
        UndoManagerEvent.UndoActionTitle carries the title of the Undo context, and UndoManagerEvent.UndoContextDepth the number of open Undo contexts, excluding the one just left.
        """
        ...
    def leftHiddenContext(self, iEvent: 'UndoManagerEvent_1c2d0eba') -> None:
        """
        is called when a hidden Undo context has been left.
        
        UndoManagerEvent.UndoActionTitle is empty, as hidden Undo contexts don't have a title.
        """
        ...
    def redoActionsCleared(self, iEvent: 'EventObject_a3d70b03') -> None:
        """
        is called when the Redo stack has been cleared.
        """
        ...
    def resetAll(self, iEvent: 'EventObject_a3d70b03') -> None:
        """
        called when the complete undo manager has been reset
        """
        ...
    def undoActionAdded(self, iEvent: 'UndoManagerEvent_1c2d0eba') -> None:
        """
        is called when an undo action is added to the undo stack.
        
        Note that the action must not necessarily be the new top element of the stack: In case there's an open Undo context, UndoManagerEvent.UndoContextDepth will be greater 0, and the newly added action will be subordinate of the context action.
        """
        ...


