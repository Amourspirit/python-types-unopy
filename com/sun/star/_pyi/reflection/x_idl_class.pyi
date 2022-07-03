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
# Namespace: com.sun.star.reflection
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_idl_array import XIdlArray as XIdlArray_d65d0ca3
    from .x_idl_field import XIdlField as XIdlField_d62c0c88
    from .x_idl_method import XIdlMethod as XIdlMethod_e3740d05
    from ..uno.type_class import TypeClass as TypeClass_853109f2
    from ..uno.uik import Uik as Uik_4fac0783

class XIdlClass(XInterface_8f010a43):
    """
    Provides information reflecting a UNO type.

    See Also:
        `API XIdlClass <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XIdlClass.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.reflection.XIdlClass']

    def createObject(self, obj: object) -> None:
        """
        This method creates instances of the reflected type.

        * ``obj`` is an out direction argument.
        """
        ...
    def equals(self, Type: 'XIdlClass') -> bool:
        """
        Tests whether two reflecting objects reflect the same type.
        """
        ...
    def getArray(self) -> 'XIdlArray_d65d0ca3':
        """
        If the reflected type is an array, then you get a XIdlArray interface to modify instances of the array type.
        
        If the reflected type is not an array, then a null-reference is returned.
        """
        ...
    def getClass(self, aName: str) -> 'XIdlClass':
        """
        Deprecated.
        
        Do not call.
        """
        ...
    def getClasses(self) -> 'typing.Tuple[XIdlClass, ...]':
        """
        Deprecated.
        
        Do not call.
        """
        ...
    def getComponentType(self) -> 'XIdlClass':
        """
        If the reflected type is an array or sequence, then this method returns a XIdlClass interface reflecting the element.
        """
        ...
    def getField(self, aName: str) -> 'XIdlField_d62c0c88':
        """
        If the reflected type is an interface, struct or union, then you get a XIdlField interface reflecting the demanded field (/interface attribute) by name.
        
        If the reflected type is not an interface, struct or union or the interface, struct or union does not have a field (/interface attribute) with the demanded name, then a null-reference is returned.
        """
        ...
    def getFields(self) -> 'typing.Tuple[XIdlField_d62c0c88, ...]':
        """
        If the reflected type is an interface, struct or union, then you get a sequence of XIdlField interfaces reflecting all fields (/interface attributes).
        
        This also includes all inherited fields (/interface attributes) of the interface, struct of union. If the reflected type is not an interface, struct or union or the interface, struct or union does not have any field (/interface attribute), then an empty sequence is returned.
        """
        ...
    def getInterfaces(self) -> 'typing.Tuple[XIdlClass, ...]':
        """
        Deprecated.
        
        Do not call.
        """
        ...
    def getMethod(self, aName: str) -> 'XIdlMethod_e3740d05':
        """
        If the reflected type is an interface, then you get a XIdlMethod interface reflecting the demanded method by name.
        
        If the reflected type is not an interface or the interface does not have a method with the demanded name (including inherited methods), then a null-reference is returned.
        """
        ...
    def getMethods(self) -> 'typing.Tuple[XIdlMethod_e3740d05, ...]':
        """
        If the reflected type is an interface, then you get a sequence of XIdlMethod interfaces reflecting all methods of the interface.
        
        This also includes the inherited methods of the interface. If the reflected type is not an interface or the interface does not have any methods, then a null-reference is returned.
        """
        ...
    def getName(self) -> str:
        """
        Returns the fully-qualified name of the reflected type.
        """
        ...
    def getSuperclasses(self) -> 'typing.Tuple[XIdlClass, ...]':
        """
        If the reflected type is an interface, then the returned sequence of XIdlClass reflect the base interfaces.
        
        If the reflected type is not an interface or an interface that is not derived from another, then an empty sequence is returned.
        """
        ...
    def getTypeClass(self) -> 'TypeClass_853109f2':
        """
        Returns the com.sun.star.uno.TypeClass of the reflected type.
        """
        ...
    def getUik(self) -> 'Uik_4fac0783':
        """
        Deprecated.
        
        Do not call.
        """
        ...
    def isAssignableFrom(self, xType: 'XIdlClass') -> bool:
        """
        Tests whether values of this reflected type are assignable from values of a second one (xType).
        """
        ...


