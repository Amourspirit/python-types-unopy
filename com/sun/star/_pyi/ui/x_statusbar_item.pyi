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
# Libre Office Version: 7.4
# Namespace: com.sun.star.ui
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ..awt.rectangle import Rectangle as Rectangle_84b109e9

class XStatusbarItem(ABC):
    """
    Represents an item in a status bar.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API XStatusbarItem <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1XStatusbarItem.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ui.XStatusbarItem']

    def repaint(self) -> None:
        """
        forces repainting the item onto the status bar device
        """
        ...

    @property
    def AccessibleName(self) -> str:
        """
        the accessible name of the status bar item
        """
        ...

    @property
    def Command(self) -> str:
        """
        the command of the status bar item
        """
        ...

    @property
    def HelpText(self) -> str:
        """
        the help text of the status bar item when extended help tips are on
        """
        ...

    @property
    def ItemId(self) -> int:
        """
        the unique ID of the control within the status bar
        """
        ...

    @property
    def ItemRect(self) -> 'Rectangle_84b109e9':
        """
        the rectangle on the status bar device onto which the item is drawn
        """
        ...

    @property
    def Offset(self) -> int:
        """
        the offset between this status bar item and the following
        """
        ...

    @property
    def QuickHelpText(self) -> str:
        """
        the help text of the status bar item when help tips are on
        """
        ...

    @property
    def Style(self) -> int:
        """
        the style of the status bar item
        
        The following values apply for a status bar item:
        
        **since**
        
            LibreOffice 6.1)
        """
        ...

    @property
    def Text(self) -> str:
        """
        the text of status bar item
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        whether the item is visible or not
        """
        ...

    @property
    def Width(self) -> int:
        """
        the width of the status bar item
        """
        ...


