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
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XModule(XInterface_8f010a43):
    """
    can be used to overrule identification of office modules.
    
    Normally an office module will be identified by its service name in combination with a set of configuration data. But sometimes whole existing office modules will be used as black box components to implement a different office module on top of it. Patching a service name is not possible. So this optional interface can be used to overwrite identification of a module.
    
    **since**
    
        OOo 2.3

    See Also:
        `API XModule <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XModule.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.frame.XModule'

    def getIdentifier(self) -> str:
        """
        """
        ...
    def setIdentifier(self, Identifier: str) -> None:
        """
        """
        ...



