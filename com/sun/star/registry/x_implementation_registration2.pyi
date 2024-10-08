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
# Namespace: com.sun.star.registry
from __future__ import annotations
import typing

from .x_implementation_registration import XImplementationRegistration as XImplementationRegistration_df8c139a
if typing.TYPE_CHECKING:
    from .x_simple_registry import XSimpleRegistry as XSimpleRegistry_10150e9c


class XImplementationRegistration2(XImplementationRegistration_df8c139a):
    """
    extends the functionality of com.sun.star.registry.XImplementationRegistration.
    
    It can be useful to specify a complete Url to a component but register the components name only (library or jar name).
    
    **since**
    
        OOo 2.4

    See Also:
        `API XImplementationRegistration2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1registry_1_1XImplementationRegistration2.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.registry.XImplementationRegistration2'

    def registerImplementationWithLocation(self, aImplementationLoader: str, aLocation: str, aRegisteredLocation: str, xReg: XSimpleRegistry_10150e9c) -> None:
        """
        registers a component which provides one or more implementations.

        Raises:
            com.sun.star.registry.CannotRegisterImplementationException: ``CannotRegisterImplementationException``
        """
        ...


