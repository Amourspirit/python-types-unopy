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
# Namespace: com.sun.star.container
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_container_listener import XContainerListener as XContainerListener_4b89100c

class XContainer(XInterface_8f010a43):
    """
    supports quick access to the information if a container currently contains elements.
    
    The XContainer interface is provided for containers which need to broadcast changes within the container; that means the actions of adding or removing elements are broadcast to the listeners.
    
    This can be useful for UI to enable/disable some functions without actually accessing the data.

    See Also:
        `API XContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1container_1_1XContainer.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.container.XContainer']

    def addContainerListener(self, xListener: 'XContainerListener_4b89100c') -> None:
        """
        adds the specified listener to receive events when elements are inserted or removed.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.
        """
        ...
    def removeContainerListener(self, xListener: 'XContainerListener_4b89100c') -> None:
        """
        removes the specified listener so it does not receive any events from this container.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.
        """
        ...


