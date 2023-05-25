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

from .x_type_description import XTypeDescription as XTypeDescription_3c210fb1
if typing.TYPE_CHECKING:
    from .x_interface_member_type_description import XInterfaceMemberTypeDescription as XInterfaceMemberTypeDescription_52ea159a
    from ..uno.uik import Uik as Uik_4fac0783


class XInterfaceTypeDescription(XTypeDescription_3c210fb1):
    """
    Reflects an interface type.
    
    This type is superseded by XInterfaceTypeDescription2, which supports multiple inheritance.

    See Also:
        `API XInterfaceTypeDescription <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XInterfaceTypeDescription.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.reflection.XInterfaceTypeDescription'

    def getBaseType(self) -> XTypeDescription_3c210fb1:
        """
        Returns the base interface or null, if the reflected interface is not inherited from another.
        
        This method is deprecated, as it only supports single inheritance. See XInterfaceTypeDescription2 for a replacement that supports multiple inheritance.
        """
        ...
    def getMembers(self) -> typing.Tuple[XInterfaceMemberTypeDescription_52ea159a, ...]:
        """
        Returns the members of the interfaces, i.e.
        
        attributes and methods.
        """
        ...
    def getUik(self) -> Uik_4fac0783:
        """
        Deprecated.
        
        UIK are not used anymore, a type is uniquely identified by its name.Returns the UIK, i.e. the unique identifier of the interface.
        """
        ...



