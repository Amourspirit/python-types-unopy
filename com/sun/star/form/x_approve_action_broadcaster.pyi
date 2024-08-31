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
# Namespace: com.sun.star.form
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_approve_action_listener import XApproveActionListener as XApproveActionListener_390f0f95


class XApproveActionBroadcaster(XInterface_8f010a43):
    """
    allows to probably veto actions to be performed on components.
    
    Usually, a component which supports the XApproveActionBroadcaster interface implements com.sun.star.awt.XActionListener as well.

    See Also:
        `API XApproveActionBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XApproveActionBroadcaster.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.form.XApproveActionBroadcaster'

    def addApproveActionListener(self, aListener: XApproveActionListener_390f0f95) -> None:
        """
        adds the specified listener to receive the XApproveActionListener.approveAction() event.
        """
        ...
    def removeApproveActionListener(self, aListener: XApproveActionListener_390f0f95) -> None:
        """
        removes the specified listener
        """
        ...


