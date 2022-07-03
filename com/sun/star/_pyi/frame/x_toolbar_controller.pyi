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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.frame
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.x_window import XWindow as XWindow_713b0924

class XToolbarController(XInterface_8f010a43):
    """
    is an abstract service for a component which offers a more complex user interface to users within a toolbar.
    
    A generic toolbar function is represented as a button which has a state (enabled,disabled and selected, not selected). A toolbar controller can be added to a toolbar and provide information or functions with a more sophisticated user interface.A typical example for toolbar controller is a font chooser on a toolbar. It provides all available fonts in a dropdown box and shows the current chosen font.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XToolbarController <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XToolbarController.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.frame.XToolbarController']

    def click(self) -> None:
        """
        notifies a component that a single click has been made on the toolbar item.
        """
        ...
    def createItemWindow(self, Parent: 'XWindow_713b0924') -> 'XWindow_713b0924':
        """
        requests to create an item window which can be added to the toolbar.
        """
        ...
    def createPopupWindow(self) -> 'XWindow_713b0924':
        """
        requests to create a pop-up window for additional functions.
        """
        ...
    def doubleClick(self) -> None:
        """
        notifies a component that a double click has been made on the toolbar item.
        """
        ...
    def execute(self, KeyModifier: int) -> None:
        """
        provides a function to execute the command which is bound to the toolbar controller.
        
        This function is usually called by a toolbar implementation when a user clicked on a toolbar button or pressed enter on the keyboard when the item has the input focus.
        """
        ...


