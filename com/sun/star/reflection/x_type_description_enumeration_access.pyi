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

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_type_description_enumeration import XTypeDescriptionEnumeration as XTypeDescriptionEnumeration_33e1438
    from ..uno.type_class import TypeClass as TypeClass_853109f2
    from com.sun.star.reflection.TypeDescriptionSearchDepth import TypeDescriptionSearchDepthProto


class XTypeDescriptionEnumerationAccess(XInterface_8f010a43):
    """
    Defines an interface for creating enumerations for type descriptions.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XTypeDescriptionEnumerationAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XTypeDescriptionEnumerationAccess.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.reflection.XTypeDescriptionEnumerationAccess'

    def createTypeDescriptionEnumeration(self, moduleName: str, types: typing.Tuple[TypeClass_853109f2, ...], depth: TypeDescriptionSearchDepthProto) -> XTypeDescriptionEnumeration_33e1438:
        """
        Creates an enumeration for type descriptions.
        
        An enumeration is always created for a UNOIDL module. The enumeration contents can be restricted by specifying type classes. Only types that match one of the supplied type classes will be part of the collection. Additionally, it is possible to specify the depth for the search within the underlying type description tree.
        
        Valid types classes are:
        
        The enumeration returns implementations of XTypeDescription. Following concrete UNOIDL parts represented by specialized interfaces derived from XTypeDescription can be returned by the enumerator:

        Raises:
            NoSuchTypeNameException: ``NoSuchTypeNameException``
            InvalidTypeNameException: ``InvalidTypeNameException``
        """
        ...


