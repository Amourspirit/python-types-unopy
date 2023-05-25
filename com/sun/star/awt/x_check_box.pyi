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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_item_listener import XItemListener as XItemListener_af710b81


class XCheckBox(XInterface_8f010a43):
    """
    gives access to the state of a check box and makes it possible to register for events.

    See Also:
        `API XCheckBox <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XCheckBox.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.awt.XCheckBox'

    def addItemListener(self, l: XItemListener_af710b81) -> None:
        """
        registers a listener for item events.
        """
        ...
    def enableTriState(self, b: bool) -> None:
        """
        enables or disables the tri state mode.
        """
        ...
    def getState(self) -> int:
        """
        returns the state of the check box.
        """
        ...
    def removeItemListener(self, l: XItemListener_af710b81) -> None:
        """
        unregisters a listener for item events.
        """
        ...
    def setLabel(self, Label: str) -> None:
        """
        sets the label of the check box.
        """
        ...
    def setState(self, n: int) -> None:
        """
        sets the state of the check box.
        """
        ...



