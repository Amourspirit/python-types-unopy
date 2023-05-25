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
# Namespace: com.sun.star.auth
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .xsso_manager import XSSOManager as XSSOManager_a2080ac2


class XSSOManagerFactory(XInterface_8f010a43):
    """
    Factory for creating an SSO Manager supporting the user's configured security mechanism.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XSSOManagerFactory <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1auth_1_1XSSOManagerFactory.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.auth.XSSOManagerFactory'

    def getSSOManager(self) -> XSSOManager_a2080ac2:
        """
        provides a XSSOManager to be used in subsequent security context creation.
        """
        ...



