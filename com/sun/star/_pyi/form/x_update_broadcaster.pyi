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
# Namespace: com.sun.star.form
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_update_listener import XUpdateListener as XUpdateListener_d4eb0cbd

class XUpdateBroadcaster(XInterface_8f010a43):
    """
    is the broadcaster interface for sending \"approveUpdate\" and \"updated\" events.
    
    The component supporting this interface must do approval calls (XUpdateListener.approveUpdate()) immediately before the data is updated, and notification calls (XUpdateListener.updated()) immediately afterwards.

    See Also:
        `API XUpdateBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XUpdateBroadcaster.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.form.XUpdateBroadcaster']

    def addUpdateListener(self, aListener: 'XUpdateListener_d4eb0cbd') -> None:
        """
        adds the specified listener to receive the events \"approveUpdate\" and \"updated\".
        """
        ...
    def removeUpdateListener(self, aListener: 'XUpdateListener_d4eb0cbd') -> None:
        """
        removes the specified listener.
        """
        ...


