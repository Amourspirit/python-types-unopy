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
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_event_handler import XEventHandler as XEventHandler_af250b6c


class XDisplayConnection(XInterface_8f010a43):
    """
    This interface should be implemented by toolkits that want to give access to their internal message handling loop.

    See Also:
        `API XDisplayConnection <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XDisplayConnection.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XDisplayConnection']

    def addErrorHandler(self, errorHandler: 'XEventHandler_af250b6c') -> None:
        """
        register an error handler for toolkit specific errors.
        """
        ...
    def addEventHandler(self, window: typing.Any, eventHandler: 'XEventHandler_af250b6c', eventMask: int) -> None:
        """
        registers an event handler.
        """
        ...
    def getIdentifier(self) -> typing.Any:
        """
        returns an identifier.
        """
        ...
    def removeErrorHandler(self, errorHandler: 'XEventHandler_af250b6c') -> None:
        """
        remover an error handler from the handler list.
        """
        ...
    def removeEventHandler(self, window: typing.Any, eventHandler: 'XEventHandler_af250b6c') -> None:
        """
        removes an eventHandler from the handler list.
        """
        ...


