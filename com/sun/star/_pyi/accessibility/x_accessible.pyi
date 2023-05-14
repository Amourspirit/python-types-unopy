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
# Namespace: com.sun.star.accessibility
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_accessible_context import XAccessibleContext as XAccessibleContext_8eae119b

class XAccessible(XInterface_8f010a43):
    """
    This interface has to be implemented by any class that wants to be accessible.
    
    It is used to provide access to the XAccessibleContext interface but allows at the same time that the interface is implemented by another class.
    
    The distinction between the interfaces XAccessible and XAccessibleContext makes it possible to split up the implementation of the class that is made accessible and the actual accessibility code into two (mostly) independent parts. The only necessary dependence is the XAccessible.getAccessibleContext() function that returns the accessible context. This one-way link has to be persistent in some sense: As long as there is at least one reference to a specific XAccessibleContext object the XAccessible object has to return the same context for every call to XAccessible.getAccessibleContext(). This is necessary to allow the use of object identity for comparing accessibility contexts for being equal.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessible <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessible.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.accessibility.XAccessible']

    def getAccessibleContext(self) -> 'XAccessibleContext_8eae119b':
        """
        Returns the AccessibleContext associated with this object.
        
        The idea to let this interface only return an XAccessibleContext instead of directly supporting its functions is to allow the separation of the implementation of the functions that make a class accessible from the implementation of that class. You may, of course, implement XAccessible and XAccessibleContext in one class.
        """
        ...


