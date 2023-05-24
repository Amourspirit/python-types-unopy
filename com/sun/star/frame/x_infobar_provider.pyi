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
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.string_pair import StringPair as StringPair_a4bc0b14


class XInfobarProvider(XInterface_8f010a43):
    """
    Allows to add Infobars to a frame.
    
    This interface can be obtained via com.sun.star.frame.XController.
    
    **since**
    
        LibreOffice 6.4

    See Also:
        `API XInfobarProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XInfobarProvider.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.frame.XInfobarProvider'

    def appendInfobar(self, id: str, primaryMessage: str, secondaryMessage: str, infobarType: int, actionButtons: typing.Tuple[StringPair_a4bc0b14, ...], showCloseButton: bool) -> None:
        """
        Creates and displays a new Infobar.
        
        The example below adds a new infobar named MyInfoBar with type INFO and close (x) button.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def hasInfobar(self, id: str) -> bool:
        """
        Check if Infobar exists.
        
        **since**
        
            LibreOffice 7.0
        """
        ...
    def removeInfobar(self, id: str) -> None:
        """
        Removes an existing Infobar.
        
        Remove MyInfoBar infobar

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    def updateInfobar(self, id: str, primaryMessage: str, secondaryMessage: str, infobarType: int) -> None:
        """
        Updates an existing Infobar.
        
        Use if you want to update only small parts of the Infobar.
        
        Update the infobar and change the type to WARNING

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...


