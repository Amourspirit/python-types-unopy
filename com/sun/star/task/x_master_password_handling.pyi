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
# Namespace: com.sun.star.task
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51


class XMasterPasswordHandling(XInterface_8f010a43):
    """
    allows to change the master password, or let it be requested and checked.

    See Also:
        `API XMasterPasswordHandling <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XMasterPasswordHandling.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.task.XMasterPasswordHandling'

    def allowPersistentStoring(self, bAllow: bool) -> bool:
        """
        allows to specify whether persistent storing of passwords is allowed
        
        After the storing is forbidden the master password and all the stored passwords are removed.
        """
        ...
    def authorizateWithMasterPassword(self, xHandler: XInteractionHandler_bf80e51) -> bool:
        """
        allows to check the user authorization.
        
        This call let the master password be requested from user using the provided interaction handler.
        
        The call will use the standard interaction handler service InteractionHandler if no handler is provided.
        """
        ...
    def changeMasterPassword(self, xHandler: XInteractionHandler_bf80e51) -> bool:
        """
        allows to change the master password.
        
        If there is still no master password, the user will be asked to provide the new one.
        
        The call will use the standard interaction handler service InteractionHandler if no handler is provided.
        """
        ...
    def hasMasterPassword(self) -> bool:
        """
        allows to detect whether there is already a master password
        """
        ...
    def isPersistentStoringAllowed(self) -> bool:
        """
        allows to detect whether persistent storing of passwords is allowed
        """
        ...
    def removeMasterPassword(self) -> None:
        """
        let the master password and all the related stored passwords be removed.
        """
        ...


