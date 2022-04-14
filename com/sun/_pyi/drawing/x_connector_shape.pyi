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
# Namespace: com.sun.star.drawing
from typing_extensions import Literal
import typing
from .x_shape import XShape as XShape_8fd00a3d
if typing.TYPE_CHECKING:
    from .connection_type import ConnectionType as ConnectionType_f1940da6
    from .x_connectable_shape import XConnectableShape as XConnectableShape_1abe0e9b

class XConnectorShape(XShape_8fd00a3d):
    """
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XConnectorShape <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1drawing_1_1XConnectorShape.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.drawing.XConnectorShape']

    def connectEnd(self, xShape: 'XConnectableShape_1abe0e9b', nPos: 'ConnectionType_f1940da6') -> None:
        """
        connects the end of this instance.
        """
    def connectStart(self, xShape: 'XConnectableShape_1abe0e9b', nPos: 'ConnectionType_f1940da6') -> None:
        """
        connects the start of this instance
        """
    def disconnectBegin(self, xShape: 'XConnectableShape_1abe0e9b') -> None:
        """
        disconnects the given Shape from the start of this instance.
        """
    def disconnectEnd(self, xShape: 'XConnectableShape_1abe0e9b') -> None:
        """
        disconnects the given Shape from the end of this instance.
        """

__all__ = ['XConnectorShape']

