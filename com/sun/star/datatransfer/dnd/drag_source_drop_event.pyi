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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.datatransfer.dnd
# Libre Office Version: 2024.2
from .drag_source_event import DragSourceEvent as DragSourceEvent_8ccf115c
from ...uno.x_interface import XInterface as XInterface_8f010a43
from .x_drag_source_context import XDragSourceContext as XDragSourceContext_c2661297
from .x_drag_source import XDragSource as XDragSource_49900fb2
import typing


class DragSourceDropEvent(DragSourceEvent_8ccf115c):
    """
    Struct Class

    The DragSourceDropEvent is delivered from an object that implements XDragSourceContext to its currently registered drag source listener's.
    
    It contains sufficient information for the originator of the operation to provide appropriate feedback to the end user when the operation completes.

    See Also:
        `API DragSourceDropEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1DragSourceDropEvent.html>`_
    """
    typeName: str = 'com.sun.star.datatransfer.dnd.DragSourceDropEvent'

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., DragSourceContext: typing.Optional[XDragSourceContext_c2661297] = ..., DragSource: typing.Optional[XDragSource_49900fb2] = ..., DropAction: typing.Optional[int] = ..., DropSuccess: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            DragSourceContext (XDragSourceContext, optional): DragSourceContext value.
            DragSource (XDragSource, optional): DragSource value.
            DropAction (int, optional): DropAction value.
            DropSuccess (bool, optional): DropSuccess value.
        """
        ...

    @property
    def DropAction(self) -> int:
        """
        The action performed by the target on the subject of the drop.
        """
        ...
    @DropAction.setter
    def DropAction(self, value: int) -> None:
        ...
    @property
    def DropSuccess(self) -> bool:
        """
        Indicates if the drop was successful.
        """
        ...
    @DropSuccess.setter
    def DropSuccess(self, value: bool) -> None:
        ...

