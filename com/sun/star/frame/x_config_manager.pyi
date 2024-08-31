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
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.x_property_change_listener import XPropertyChangeListener as XPropertyChangeListener_58e4105a


class XConfigManager(XInterface_8f010a43):
    """
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XConfigManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XConfigManager.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.frame.XConfigManager'

    def addPropertyChangeListener(self, KeyName: str, Listener: XPropertyChangeListener_58e4105a) -> None:
        """
        add a listener to notify changes on well known variables inside the real implementation
        
        Listener can update his text values by calling XConfigManager.substituteVariables() again. If KeyName specifies a group of keys, the listener gets one notify for each subkey.
        """
        ...
    def flush(self) -> None:
        """
        was designed for additional functionality for interface com.sun.star.registry.XSimpleRegistry and make no sense without that
        """
        ...
    def removePropertyChangeListener(self, KeyName: str, Listener: XPropertyChangeListener_58e4105a) -> None:
        """
        remove a registered listener
        """
        ...
    def substituteVariables(self, Text: str) -> str:
        """
        substitute variables (place holder) inside given parameter Text
        
        The value of Text is NOT changed.
        """
        ...


