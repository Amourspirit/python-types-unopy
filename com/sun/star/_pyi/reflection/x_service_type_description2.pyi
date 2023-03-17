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
# Libre Office Version: 7.4
# Namespace: com.sun.star.reflection
from typing_extensions import Literal
import typing
from .x_service_type_description import XServiceTypeDescription as XServiceTypeDescription_b4481282
if typing.TYPE_CHECKING:
    from .x_service_constructor_description import XServiceConstructorDescription as XServiceConstructorDescription_430d1586
    from .x_type_description import XTypeDescription as XTypeDescription_3c210fb1

class XServiceTypeDescription2(XServiceTypeDescription_b4481282):
    """
    Reflects a service, supporting single-interface–based services.
    
    This type supersedes XServiceTypeDescription, which only supports obsolete, accumulation-based services.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XServiceTypeDescription2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XServiceTypeDescription2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.reflection.XServiceTypeDescription2']

    def getConstructors(self) -> 'typing.Tuple[XServiceConstructorDescription_430d1586, ...]':
        """
        Returns the constructors of the service.
        """
        ...
    def getInterface(self) -> 'XTypeDescription_3c210fb1':
        """
        Returns the interface type associated with the service.
        """
        ...
    def isSingleInterfaceBased(self) -> bool:
        """
        Returns whether this object reflects a single-interface–based service.
        """
        ...


