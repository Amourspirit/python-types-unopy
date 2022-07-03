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
# Namespace: com.sun.star.util
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_changes_listener import XChangesListener as XChangesListener_e1b70d1d

class XChangesNotifier(XInterface_8f010a43):
    """
    broadcasts events about multiple changes that occur in bulk.

    See Also:
        `API XChangesNotifier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XChangesNotifier.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.util.XChangesNotifier']

    def addChangesListener(self, aListener: 'XChangesListener_e1b70d1d') -> None:
        """
        adds the specified listener to receive events when changes occurred.
        """
        ...
    def removeChangesListener(self, aListener: 'XChangesListener_e1b70d1d') -> None:
        """
        removes the specified listener.
        """
        ...


