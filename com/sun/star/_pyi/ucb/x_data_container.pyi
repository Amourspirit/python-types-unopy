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
# Namespace: com.sun.star.ucb
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

import uno
from ..container.x_index_container import XIndexContainer as XIndexContainer_1c040ebe


class XDataContainer(XIndexContainer_1c040ebe):
    """
    specifies a container for (binary) data.
    
    A data container may contain data and/or other data containers. A typical container with children is a MIME message with attachments.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XDataContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XDataContainer.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ucb.XDataContainer']

    def getContentType(self) -> str:
        """
        returns the content type (MIME Type) of the data container.
        """
        ...
    def getData(self) -> uno.ByteSequence:
        """
        returns the data of the data container.
        """
        ...
    def getDataURL(self) -> str:
        """
        Deprecated.
        
        Do not use!
        """
        ...
    def setContentType(self, aType: str) -> None:
        """
        sets the content type (MIME Type) of the data container.
        """
        ...
    def setData(self, aData: uno.ByteSequence) -> None:
        """
        sets the data of the data container.
        """
        ...
    def setDataURL(self, aURL: str) -> None:
        """
        Deprecated.
        
        Do not use!
        """
        ...


