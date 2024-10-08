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

from .x_menu import XMenu as XMenu_5f470841
if typing.TYPE_CHECKING:
    from .key_event import KeyEvent as KeyEvent_7a78097f
    from .rectangle import Rectangle as Rectangle_84b109e9
    from .x_window_peer import XWindowPeer as XWindowPeer_99760ab0
    from ..graphic.x_graphic import XGraphic as XGraphic_a4da0afc


class XPopupMenu(XMenu_5f470841):
    """
    controls a pop-up menu.

    See Also:
        `API XPopupMenu <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XPopupMenu.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.awt.XPopupMenu'

    def checkItem(self, nItemId: int, bCheck: bool) -> None:
        """
        sets the state of the item to be checked or unchecked.
        """
        ...
    def endExecute(self) -> None:
        """
        ends the execution of the PopupMenu.
        
        com.sun.star.awt.XPopupMenu.execute() will then return 0.
        """
        ...
    def execute(self, Parent: XWindowPeer_99760ab0, Position: Rectangle_84b109e9, Direction: int) -> int:
        """
        executes the popup menu and returns the selected item or 0, if cancelled.
        """
        ...
    def getAcceleratorKeyEvent(self, nItemId: int) -> KeyEvent_7a78097f:
        """
        retrieves the KeyEvent for the menu item.
        
        The KeyEvent is only used as a container to transport the shortcut information, so that in this case com.sun.star.lang.EventObject.Source is NULL.
        """
        ...
    def getDefaultItem(self) -> int:
        """
        returns the menu default item.
        """
        ...
    def getItemImage(self, nItemId: int) -> XGraphic_a4da0afc:
        """
        retrieves the image for the menu item.
        """
        ...
    def insertSeparator(self, nItemPos: int) -> None:
        """
        inserts a separator at the specified position.
        """
        ...
    def isInExecute(self) -> bool:
        """
        queries if the PopupMenu is being.
        
        Returns TRUE only if the PopupMenu is being executed as a result of invoking XPopupMenu.execute(); that is, for a PopupMenu activated by a MenuBar item, this methods returns FALSE.
        """
        ...
    def isItemChecked(self, nItemId: int) -> bool:
        """
        returns whether the item is checked or unchecked.
        """
        ...
    def setAcceleratorKeyEvent(self, nItemId: int, aKeyEvent: KeyEvent_7a78097f) -> None:
        """
        sets the KeyEvent for the menu item.
        
        The KeyEvent is only used as a container to transport the shortcut information, this methods only draws the text corresponding to this keyboard shortcut. The client code is responsible for listening to keyboard events (typically done via XUserInputInterception), and dispatch the respective command.
        """
        ...
    def setDefaultItem(self, nItemId: int) -> None:
        """
        sets the menu default item.
        """
        ...
    def setItemImage(self, nItemId: int, xGraphic: XGraphic_a4da0afc, bScale: bool) -> None:
        """
        sets the image for the menu item.
        """
        ...


