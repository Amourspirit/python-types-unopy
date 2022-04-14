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
# Namespace: com.sun.star.datatransfer.dnd
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_drag_gesture_listener import XDragGestureListener as XDragGestureListener_e8b41366

class XDragGestureRecognizer(XInterface_8f010a43):
    """
    This interface is implemented by a view or window that supports drag operations.
    
    Different to Java, the association between view and interface is fixed and cannot be changed. Otherwise, the AWT messaging would have to be implemented for any window supporting Drag and Drop operations, which would be a performance issue.

    See Also:
        `API XDragGestureRecognizer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1XDragGestureRecognizer.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.datatransfer.dnd.XDragGestureRecognizer']

    def addDragGestureListener(self, dgl: 'XDragGestureListener_e8b41366') -> None:
        """
        Registers a new XDragGestureListener.
        """
    def removeDragGestureListener(self, dgl: 'XDragGestureListener_e8b41366') -> None:
        """
        Unregisters the specified XDragGestureListener.
        """
    def resetRecognizer(self) -> None:
        """
        Reset the recognizer.
        
        If it is currently recognizing a gesture, ignore it.
        """

__all__ = ['XDragGestureRecognizer']

