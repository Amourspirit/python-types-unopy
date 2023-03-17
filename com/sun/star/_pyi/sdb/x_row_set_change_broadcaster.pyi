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
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdb
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from .x_row_set_change_listener import XRowSetChangeListener as XRowSetChangeListener_167a0e89

class XRowSetChangeBroadcaster(ABC):
    """
    broadcasts changes in the RowSet supplied by a component
    
    **since**
    
        OOo 3.2

    See Also:
        `API XRowSetChangeBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1XRowSetChangeBroadcaster.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sdb.XRowSetChangeBroadcaster']

    def addRowSetChangeListener(self, iListener: 'XRowSetChangeListener_167a0e89') -> None:
        """
        adds a listener to be notified when the RowSet supplied by the component changes.
        """
        ...
    def removeRowSetChangeListener(self, iListener: 'XRowSetChangeListener_167a0e89') -> None:
        """
        removes a previously added listener.
        """
        ...


