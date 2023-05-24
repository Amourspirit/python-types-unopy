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
# Namespace: com.sun.star.script
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..container.x_name_container import XNameContainer as XNameContainer_cb90e47


class XStarBasicLibraryInfo(XInterface_8f010a43):
    """
    Interface representing a library and provides access to its modules.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XStarBasicLibraryInfo <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XStarBasicLibraryInfo.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.script.XStarBasicLibraryInfo'

    def getDialogContainer(self) -> XNameContainer_cb90e47:
        """
        returns the dialog container giving access to the dialogs stored in the library.
        
        The container has to be returned in any case, no matter if the library is stored embedded, external, or linked.
        """
        ...
    def getExternalSourceURL(self) -> str:
        """
        returns an URL describing the location where the library is stored if the library is stored separately (for example not in the main XML file but in a special library format file), an empty string otherwise.
        
        This information can be useful to optimize the access to the library, e.g., for loading on demand.
        """
        ...
    def getLinkTargetURL(self) -> str:
        """
        returns an URL describing the location of the library linked to.
        
        HINT: This method can be removed when there is a generic interface for linking. Then the implementation will simply support this \"XLinked\" interface and it can be checked by queryInterface().
        """
        ...
    def getModuleContainer(self) -> XNameContainer_cb90e47:
        """
        returns the module container giving access to the modules stored in the library.
        
        The container has to be returned in any case, no matter if the library is stored embedded, external, or linked.
        """
        ...
    def getName(self) -> str:
        """
        returns the library's name
        """
        ...
    def getPassword(self) -> str:
        """
        returns the password, if the library is protected with one, an empty string otherwise.
        """
        ...


