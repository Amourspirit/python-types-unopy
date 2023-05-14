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
# Namespace: com.sun.star.lang
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_connection_point import XConnectionPoint as XConnectionPoint_e0da0d1c

class XConnectionPointContainer(XInterface_8f010a43):
    """
    makes it possible to locate a specific connection point for a specified UIK and manages a sequence of connections points.
    
    An implementation of this interface must support the com.sun.star.uno.XWeak interface. Look at the language binding for a superclass or something else.

    See Also:
        `API XConnectionPointContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1lang_1_1XConnectionPointContainer.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.lang.XConnectionPointContainer']

    def advise(self, aType: object, xListener: 'XInterface_8f010a43') -> None:
        """
        creates a connection between this object and a client's sink, where the sink implements the outgoing interface specified with ID.
        
        The interface is advised under the connection point you get with queryConnectionPoint( id ).
        
        Use this method instead of the advise method at the connection point, only if you know that the broadcaster supports the outgoing interface, or if it does not matter that the outgoing interface is not supported.
        """
        ...
    def getConnectionPointTypes(self) -> 'typing.Tuple[object, ...]':
        """
        """
        ...
    def queryConnectionPoint(self, aType: object) -> 'XConnectionPoint_e0da0d1c':
        """
        """
        ...
    def unadvise(self, aType: object, xListener: 'XInterface_8f010a43') -> None:
        """
        terminates a notification previously set up with advise at the container or at the suitable connection point.
        """
        ...


