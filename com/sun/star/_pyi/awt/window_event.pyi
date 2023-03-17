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
# Libre Office Version: 7.4
from typing_extensions import Literal
from ..lang.event_object import EventObject as EventObject_a3d70b03
from ..uno.x_interface import XInterface as XInterface_8f010a43
import typing


class WindowEvent(EventObject_a3d70b03):
    """
    Struct Class

    specifies a window event.

    See Also:
        `API WindowEvent <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1WindowEvent.html>`_
    """
    typeName: Literal['com.sun.star.awt.WindowEvent']

    def __init__(self, Source: typing.Optional[XInterface_8f010a43] = ..., X: typing.Optional[int] = ..., Y: typing.Optional[int] = ..., Width: typing.Optional[int] = ..., Height: typing.Optional[int] = ..., LeftInset: typing.Optional[int] = ..., TopInset: typing.Optional[int] = ..., RightInset: typing.Optional[int] = ..., BottomInset: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Source (XInterface, optional): Source value.
            X (int, optional): X value.
            Y (int, optional): Y value.
            Width (int, optional): Width value.
            Height (int, optional): Height value.
            LeftInset (int, optional): LeftInset value.
            TopInset (int, optional): TopInset value.
            RightInset (int, optional): RightInset value.
            BottomInset (int, optional): BottomInset value.
        """
        ...


    @property
    def X(self) -> int:
        """
        specifies the outer x position of the window.
        """
        ...


    @property
    def Y(self) -> int:
        """
        specifies the outer y position of the window.
        """
        ...


    @property
    def Width(self) -> int:
        """
        specifies the outer (total) width of the window.
        """
        ...


    @property
    def Height(self) -> int:
        """
        specifies the outer (total) height of the window.
        """
        ...


    @property
    def LeftInset(self) -> int:
        """
        specifies the inset from the left.
        
        The inset is the distance between the outer and the inner window, that means the left inset is the width of the left border.
        """
        ...


    @property
    def TopInset(self) -> int:
        """
        specifies the inset from the top.
        
        The inset is the distance between the outer and the inner window, that means the top inset is the height of the top border.
        """
        ...


    @property
    def RightInset(self) -> int:
        """
        specifies the inset from the right.
        
        The inset is the distance between the outer and the inner window, that means the right inset is the width of the right border.
        """
        ...


    @property
    def BottomInset(self) -> int:
        """
        specifies the inset from the bottom.
        
        The inset is the distance between the outer and the inner window, that means the bottom inset is the height of the bottom border.
        """
        ...


