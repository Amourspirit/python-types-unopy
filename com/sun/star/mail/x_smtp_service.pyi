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
# Namespace: com.sun.star.mail
from __future__ import annotations
import typing

from .x_mail_service import XMailService as XMailService_ae610b57
if typing.TYPE_CHECKING:
    from .x_mail_message import XMailMessage as XMailMessage_ae200b4b


class XSmtpService(XMailService_ae610b57):
    """
    Represents a SMTP service abstraction.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XSmtpService <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1mail_1_1XSmtpService.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.mail.XSmtpService'

    def sendMailMessage(self, xMailMessage: XMailMessage_ae200b4b) -> None:
        """
        Send a mail message to its recipients.

        Raises:
            com.sun.star.io.NotConnectedException: ``NotConnectedException``
            com.sun.star.mail.SendMailMessageFailedException: ``SendMailMessageFailedException``
            com.sun.star.mail.MailException: ``MailException``
            com.sun.star.datatransfer.UnsupportedFlavorException: ``UnsupportedFlavorException``
        """
        ...


