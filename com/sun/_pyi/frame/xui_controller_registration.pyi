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
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XUIControllerRegistration(XInterface_8f010a43):
    """
    is used to query, register and unregister user interface controller.
    
    A user interface controller can be registered for a command URL. A certain user interface controller will be created when a user interface element contains a registered command URL.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XUIControllerRegistration <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XUIControllerRegistration.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.frame.XUIControllerRegistration']

    def deregisterController(self, aCommandURL: str, aModelName: str) -> None:
        """
        function to remove a previously defined association between a user interface controller implementation and a command URL and optional module.
        """
    def hasController(self, aCommandURL: str, aModelName: str) -> bool:
        """
        function to check if an user interface controller is registered for a command URL and optional module.
        """
    def registerController(self, aCommandURL: str, aModelName: str, aControllerImplementationName: str) -> None:
        """
        function to create an association between a user interface controller implementation and a command URL and optional module.
        """

__all__ = ['XUIControllerRegistration']

