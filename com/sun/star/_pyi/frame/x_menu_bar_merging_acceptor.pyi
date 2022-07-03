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
# Libre Office Version: 7.3
# Namespace: com.sun.star.frame
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d

class XMenuBarMergingAcceptor(XInterface_8f010a43):
    """
    provides functions to set and remove a merged menu bar for inplace editing.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XMenuBarMergingAcceptor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XMenuBarMergingAcceptor.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.frame.XMenuBarMergingAcceptor']

    def removeMergedMenuBar(self) -> None:
        """
        removes a previously set merged menu bar and sets a previously created menu bar back.
        """
        ...
    def setMergedMenuBar(self, xMergedMenuBar: 'XIndexAccess_f0910d6d') -> bool:
        """
        allows to set a merged menu bar.
        
        This function is normally used to provide inplace editing where functions from two application parts, container application and embedded object, are available to the user simultaneously. A menu bar which is set by this method has a higher priority than others created by com.sun.star.frame.XLayoutManager interface. Settings of a merged menu bar cannot be retrieved.
        """
        ...


