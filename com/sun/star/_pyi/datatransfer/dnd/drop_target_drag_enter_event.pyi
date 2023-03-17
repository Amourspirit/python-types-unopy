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
from .drop_target_drag_event import DropTargetDragEvent as DropTargetDragEvent_d60612e7
from ...uno.x_interface import XInterface as XInterface_8f010a43
from .x_drop_target_drag_context import XDropTargetDragContext as XDropTargetDragContext_10221422
import typing
from ..data_flavor import DataFlavor as DataFlavor_ffd30deb


class DropTargetDragEnterEvent(DropTargetDragEvent_d60612e7):
    """
    Struct Class

    The DropTargetDragEnterEvent is delivered from the drop target to the currently registered drop target listeners whenever the logical cursor associated with a Drag and Drop operation enters the visible geometry of a window associated with a drop target.
    
    It contains the com.sun.star.datatransfer.DataFlavor types supported by the transferable object of the current Drag and Drop operation.

    See Also:
        `API DropTargetDragEnterEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1datatransfer_1_1dnd_1_1DropTargetDragEnterEvent.html>`_
    """
    typeName: Literal['com.sun.star.datatransfer.dnd.DropTargetDragEnterEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., Dummy: typing.Optional[int] = ..., Context: typing.Optional[XDropTargetDragContext_10221422] = ..., DropAction: typing.Optional[int] = ..., LocationX: typing.Optional[int] = ..., LocationY: typing.Optional[int] = ..., SourceActions: typing.Optional[int] = ..., SupportedDataFlavors: typing.Optional[typing.Tuple[DataFlavor_ffd30deb, ...]] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Dummy (int, optional): Dummy value.
            Context (XDropTargetDragContext, optional): Context value.
            DropAction (int, optional): DropAction value.
            LocationX (int, optional): LocationX value.
            LocationY (int, optional): LocationY value.
            SourceActions (int, optional): SourceActions value.
            SupportedDataFlavors (typing.Tuple[DataFlavor, ...], optional): SupportedDataFlavors value.
        """
        ...


    @property
    def SupportedDataFlavors(self) -> typing.Tuple[DataFlavor_ffd30deb, ...]:
        """
        A sequence of supported com.sun.star.datatransfer.DataFlavor types.
        """
        ...


