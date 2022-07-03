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
# Libre Office Version: 7.3
# Namespace: com.sun.star.text
from typing_extensions import Literal
import typing
from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
if typing.TYPE_CHECKING:
    from .x_auto_text_entry import XAutoTextEntry as XAutoTextEntry_c96f0c75
    from .x_text_range import XTextRange as XTextRange_9a910ab7

class XAutoTextGroup(XNameAccess_e2ab0cf6):
    """
    The interface provide methods to insert, rename and delete autotext entries from the current autotext group.

    See Also:
        `API XAutoTextGroup <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XAutoTextGroup.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.text.XAutoTextGroup']

    def getTitles(self) -> 'typing.Tuple[str, ...]':
        """
        returns the titles of all autotext entries.
        
        The order of the entries corresponds to the output of the function getElementNames().
        """
        ...
    def insertNewByName(self, aName: str, aTitle: str, xTextRange: 'XTextRange_9a910ab7') -> 'XAutoTextEntry_c96f0c75':
        """
        creates a new AutoTextEntry entry.

        Raises:
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """
        ...
    def removeByName(self, aEntryName: str) -> None:
        """
        removes the specified autotext entry.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    def renameByName(self, aElementName: str, aNewElementName: str, aNewElementTitle: str) -> None:
        """
        renames an entry in the autotext group.
        
        The position of the autotext entry is not changed.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...


