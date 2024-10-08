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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.awt
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_menu_bar import XMenuBar as XMenuBar_7a040956
    from .x_top_window_listener import XTopWindowListener as XTopWindowListener_efc20d9d


class XTopWindow(XInterface_8f010a43):
    """
    manages the functionality specific for a top window.

    See Also:
        `API XTopWindow <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XTopWindow.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.awt.XTopWindow'

    def addTopWindowListener(self, xListener: XTopWindowListener_efc20d9d) -> None:
        """
        adds the specified top window listener to receive window events from this window.
        """
        ...
    def removeTopWindowListener(self, xListener: XTopWindowListener_efc20d9d) -> None:
        """
        removes the specified top window listener so that it no longer receives window events from this window.
        """
        ...
    def setMenuBar(self, xMenu: XMenuBar_7a040956) -> None:
        """
        sets a menu bar.
        """
        ...
    def toBack(self) -> None:
        """
        places this window at the bottom of the stacking order and makes the corresponding adjustment to other visible windows.
        """
        ...
    def toFront(self) -> None:
        """
        places this window at the top of the stacking order and shows it in front of any other windows.
        """
        ...


