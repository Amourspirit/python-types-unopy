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
# Namespace: com.sun.star.registry
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_simple_registry import XSimpleRegistry as XSimpleRegistry_10150e9c

class XImplementationRegistration(XInterface_8f010a43):
    """
    offers a registry for implementation objects and provides information about the registered implementations.

    See Also:
        `API XImplementationRegistration <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1registry_1_1XImplementationRegistration.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.registry.XImplementationRegistration']

    def checkInstantiation(self, implementationName: str) -> 'typing.Tuple[str, ...]':
        """
        """
    def getImplementations(self, aImplementationLoader: str, aLocation: str) -> 'typing.Tuple[str, ...]':
        """
        """
    def registerImplementation(self, aImplementationLoader: str, aLocation: str, xReg: 'XSimpleRegistry_10150e9c') -> None:
        """
        registers a component which provides one or more implementations.

        Raises:
            com.sun.star.registry.CannotRegisterImplementationException: ``CannotRegisterImplementationException``
        """
    def revokeImplementation(self, aLocation: str, xReg: 'XSimpleRegistry_10150e9c') -> bool:
        """
        revokes a component and all their provided implementations from the registry.
        """

__all__ = ['XImplementationRegistration']

