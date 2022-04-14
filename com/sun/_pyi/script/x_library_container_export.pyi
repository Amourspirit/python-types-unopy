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
# Namespace: com.sun.star.script
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..task.x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51

class XLibraryContainerExport(XInterface_8f010a43):
    """
    Extension of XLibraryContainer to provide functionality to store a library to a location represented by a URL.

    See Also:
        `API XLibraryContainerExport <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XLibraryContainerExport.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.script.XLibraryContainerExport']

    def exportLibrary(self, Name: str, URL: str, Handler: 'XInteractionHandler_bf80e51') -> None:
        """
        Exports a library specified by Name to the location specified by the passed URL string.
        
        An interaction handler can be passed to be used for internal ucb operations. Exceptions not processed by this handler will be passed as com.sun.star.uno.Exception. If this parameter is null this applies to all exceptions thrown by ucb.
        
        If a library with the this name doesn't exist a com.sun.star.container.NoSuchElementException is thrown.

        Raises:
            com.sun.star.uno.Exception: ``Exception``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """

__all__ = ['XLibraryContainerExport']

