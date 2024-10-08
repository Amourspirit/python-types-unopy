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
# Namespace: com.sun.star.beans
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_introspection_access import XIntrospectionAccess as XIntrospectionAccess_2a050f2c


class XIntrospection(XInterface_8f010a43):
    """
    allows the inspection of an object's properties and methods.
    
    Important note:An object can only be inspected completely if it supports the com.sun.star.lang.XTypeProvider interface.
    
    For details see method XIntrospection.inspect().

    See Also:
        `API XIntrospection <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XIntrospection.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.beans.XIntrospection'

    def inspect(self, aObject: typing.Any) -> XIntrospectionAccess_2a050f2c:
        """
        inspects the given object.
        
        It identifies all properties supported by the object if they are represented in one of the following ways:
        
        In addition, the inspect method identifies all listener access methods in the form add...Listener/ remove...Listener (except methods of interface XPropertySet) where \"...\" stands for the listener type.
        
        Methods which do not belong to a property nor which represent a listener access nor which are methods of XPropertySet, com.sun.star.container.XNameAccess, com.sun.star.container.XIndexAccess, or com.sun.star.container.XEnumerationAccess, are considered to be normal methods.
        """
        ...


