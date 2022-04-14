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
from ...lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .drag_gesture_event import DragGestureEvent as DragGestureEvent_9e7211ca

class XDragGestureListener(XEventListener_c7230c4a):
    """
    This interface will be used by a XDragGestureRecognizer when it detects a drag initiating gesture.
    
    The implementor of this interface is responsible for starting the drag as a result of receiving such notification.

    See Also:
        `API XDragGestureListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1XDragGestureListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.datatransfer.dnd.XDragGestureListener']

    def dragGestureRecognized(self, dge: 'DragGestureEvent_9e7211ca') -> None:
        """
        A XDragGestureRecognizer has detected a platform-dependent drag initiating gesture and is notifying this listener in order for it to initiate the action for the user.
        """

__all__ = ['XDragGestureListener']

