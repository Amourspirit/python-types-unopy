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
# Namespace: com.sun.star.datatransfer.dnd
# Libre Office Version: 7.4
from typing_extensions import Literal
from ...lang.event_object import EventObject as EventObject_a3d70b03
from ...uno.x_interface import XInterface as XInterface_8f010a43
import typing
from .x_drag_source import XDragSource as XDragSource_49900fb2


class DragGestureEvent(EventObject_a3d70b03):
    """
    Struct Class

    A DragGestureEvent is passed to the method XDragGestureListener.dragGestureRecognized() when a particular XDragGestureRecognizer detects that a platform dependent drag initiating gesture has occurred on the component that it is tracking.

    See Also:
        `API DragGestureEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1DragGestureEvent.html>`_
    """
    typeName: Literal['com.sun.star.datatransfer.dnd.DragGestureEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., DragAction: typing.Optional[int] = ..., DragOriginX: typing.Optional[int] = ..., DragOriginY: typing.Optional[int] = ..., DragSource: typing.Optional[XDragSource_49900fb2] = ..., Event: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            DragAction (int, optional): DragAction value.
            DragOriginX (int, optional): DragOriginX value.
            DragOriginY (int, optional): DragOriginY value.
            DragSource (XDragSource, optional): DragSource value.
            Event (object, optional): Event value.
        """
        ...


    @property
    def DragAction(self) -> int:
        """
        The action selected by the user.
        
        Different constants may be combined using a logical OR.
        
        It's further possible to combine the ACTION_DEFAULT with one of the other actions defined in com.sun.star.datatransfer.dnd.DNDConstants. This means the user did not press any key during the Drag and Drop operation and the action that was combined with ACTION_DEFAULT is the system default action.
        """
        ...


    @property
    def DragOriginX(self) -> int:
        """
        The x coordinate where the drag originated in component coordinates.
        """
        ...


    @property
    def DragOriginY(self) -> int:
        """
        The y coordinate where the drag originated in component coordinates.
        """
        ...


    @property
    def DragSource(self) -> XDragSource_49900fb2:
        """
        The DragSource associated with this drag action.
        """
        ...


    @property
    def Event(self) -> object:
        """
        The last event comprising the gesture.
        
        The initial trigger event will presumably be a com.sun.star.awt.MouseEvent event. If it is not, the implementation should either react accordingly or presume that the left mouse button was clicked.
        """
        ...


