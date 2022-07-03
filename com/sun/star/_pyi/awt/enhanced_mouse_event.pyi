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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.3
from typing_extensions import Literal
from .mouse_event import MouseEvent as MouseEvent_8f430a5f
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43


class EnhancedMouseEvent(MouseEvent_8f430a5f):
    """
    Struct Class

    specifies an event from the mouse.
    
    **since**
    
        OOo 2.0

    See Also:
        `API EnhancedMouseEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1EnhancedMouseEvent.html>`_
    """
    typeName: Literal['com.sun.star.awt.EnhancedMouseEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., Modifiers: typing.Optional[int] = ..., Buttons: typing.Optional[int] = ..., X: typing.Optional[int] = ..., Y: typing.Optional[int] = ..., ClickCount: typing.Optional[int] = ..., PopupTrigger: typing.Optional[bool] = ..., Target: typing.Optional[XInterface_8f010a43] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            Modifiers (int, optional): Modifiers value.
            Buttons (int, optional): Buttons value.
            X (int, optional): X value.
            Y (int, optional): Y value.
            ClickCount (int, optional): ClickCount value.
            PopupTrigger (bool, optional): PopupTrigger value.
            Target (XInterface, optional): Target value.
        """
        ...


    @property
    def Target(self) -> XInterface_8f010a43:
        """
        contains the object on the location of the mouse.
        """
        ...


