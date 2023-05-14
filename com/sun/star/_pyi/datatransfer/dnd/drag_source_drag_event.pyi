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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.datatransfer.dnd
# Libre Office Version: 7.4
from typing_extensions import Literal
from .drag_source_event import DragSourceEvent as DragSourceEvent_8ccf115c
from ...uno.x_interface import XInterface as XInterface_8f010a43
from .x_drag_source_context import XDragSourceContext as XDragSourceContext_c2661297
from .x_drag_source import XDragSource as XDragSource_49900fb2
import typing


class DragSourceDragEvent(DragSourceEvent_8ccf115c):
    """
    Struct Class

    The DragSourceDragEvent is delivered from an object that implements the XDragSourceContext to the currently registered drag source listener.
    
    It contains state regarding the current state of the operation to enable the operations initiator to provide the end user with the appropriate drag over feedback.

    See Also:
        `API DragSourceDragEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1DragSourceDragEvent.html>`_
    """
    typeName: Literal['com.sun.star.datatransfer.dnd.DragSourceDragEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., DragSourceContext: typing.Optional[XDragSourceContext_c2661297] = ..., DragSource: typing.Optional[XDragSource_49900fb2] = ..., DropAction: typing.Optional[int] = ..., UserAction: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            DragSourceContext (XDragSourceContext, optional): DragSourceContext value.
            DragSource (XDragSource, optional): DragSource value.
            DropAction (int, optional): DropAction value.
            UserAction (int, optional): UserAction value.
        """
        ...


    @property
    def DropAction(self) -> int:
        """
        The drag action selected by the current drop target.
        """
        ...

    @DropAction.setter
    def DropAction(self, value: int) -> None:
        ...

    @property
    def UserAction(self) -> int:
        """
        The user's currently selected drop action.
        """
        ...

    @UserAction.setter
    def UserAction(self, value: int) -> None:
        ...

