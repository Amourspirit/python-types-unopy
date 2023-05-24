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
# Namespace: com.sun.star.reflection
from __future__ import annotations
import typing

from .x_interface_member_type_description import XInterfaceMemberTypeDescription as XInterfaceMemberTypeDescription_52ea159a
if typing.TYPE_CHECKING:
    from .x_method_parameter import XMethodParameter as XMethodParameter_3b120f8d
    from .x_type_description import XTypeDescription as XTypeDescription_3c210fb1


class XInterfaceMethodTypeDescription(XInterfaceMemberTypeDescription_52ea159a):
    """
    Reflects an interface method type.
    
    The type class of this type is TypeClass_INTERFACE_METHOD.

    See Also:
        `API XInterfaceMethodTypeDescription <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XInterfaceMethodTypeDescription.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.reflection.XInterfaceMethodTypeDescription'

    def getExceptions(self) -> typing.Tuple[XTypeDescription_3c210fb1, ...]:
        """
        Returns declared exceptions that may occur upon invocations of the method.
        """
        ...
    def getParameters(self) -> typing.Tuple[XMethodParameter_3b120f8d, ...]:
        """
        Returns all parameters of the method in order of IDL declaration.
        """
        ...
    def getReturnType(self) -> XTypeDescription_3c210fb1:
        """
        Returns the method's return type.
        """
        ...
    def isOneway(self) -> bool:
        """
        Returns true, if this method is declared oneway.
        """
        ...


