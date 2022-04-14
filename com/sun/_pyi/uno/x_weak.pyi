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
# Namespace: com.sun.star.uno
from typing_extensions import Literal
import typing
from .x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_adapter import XAdapter as XAdapter_7a4e0973

class XWeak(XInterface_8f010a43):
    """
    the server-side interface to a weak object.
    
    This interface is proxy to the adapted object. In order to make it possible to have weak references to objects, the XAdapter interface must be implemented to provide a weak adapter for the clients.
    
    This module specifies the interfaces for implementing and using weak references.
    
    The sense of weak references is to hold a reference to an object without affecting the lifetime of the object. That means that a weak reference may become invalid, at any time, if the referenced object dies.
    
    The following interfaces describe one way to handle weak references by providing a weak adapter. The weak object has to provide this adapter if anyone wants to hold a weak reference. To separate their lifetimes, the adapter and the original object must not share the same reference counter. The weak reference is in fact only a hard reference to the adapter, which knows - but does not hold - the original object. That means that the implementation and synchronization of weak referencing is the responsibility of the object. The following interfaces are involved in the concept of weak referencing:

    See Also:
        `API XWeak <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1uno_1_1XWeak.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.uno.XWeak']

    def queryAdapter(self) -> 'XAdapter_7a4e0973':
        """
        queries the weak adapter.
        
        It is important that the adapter must know, but not hold the adapted object. If the adapted object dies, all references to the adapter have to be notified to release the adapter.
        """

__all__ = ['XWeak']

