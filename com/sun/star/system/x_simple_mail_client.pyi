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
# Namespace: com.sun.star.system
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_simple_mail_message import XSimpleMailMessage as XSimpleMailMessage_1d420eb7


class XSimpleMailClient(XInterface_8f010a43):
    """
    Specifies an interface for creating and sending email messages.

    See Also:
        `API XSimpleMailClient <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1system_1_1XSimpleMailClient.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.system.XSimpleMailClient'

    def createSimpleMailMessage(self) -> XSimpleMailMessage_1d420eb7:
        """
        Create a simple mail message object that implements the interface XSimpleMailMessage.
        """
        ...
    def sendSimpleMailMessage(self, xSimpleMailMessage: XSimpleMailMessage_1d420eb7, aFlag: int) -> None:
        """
        Sends a given simple mail message object that implements the interface XSimpleMailMessage.
        
        The Message member of the exception may contain an error description.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...


