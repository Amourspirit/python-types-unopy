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
# Namespace: com.sun.star.mail
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_authenticator import XAuthenticator as XAuthenticator_c7b50c5e
    from .x_connection_listener import XConnectionListener as XConnectionListener_aaa0e59
    from ..uno.x_current_context import XCurrentContext as XCurrentContext_c9110c7a

class XMailService(XInterface_8f010a43):
    """
    Represents a mail server abstraction.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XMailService <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1mail_1_1XMailService.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.mail.XMailService']

    def addConnectionListener(self, xListener: 'XConnectionListener_aaa0e59') -> None:
        """
        Register a connection listener.
        """
        ...
    def connect(self, xConnectionContext: 'XCurrentContext_c9110c7a', xAuthenticator: 'XAuthenticator_c7b50c5e') -> None:
        """
        Connect to a mail service.
        
        Only one connection to a mail service can be established at a time.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.io.AlreadyConnectedException: ``AlreadyConnectedException``
            com.sun.star.io.UnknownHostException: ``UnknownHostException``
            com.sun.star.io.NoRouteToHostException: ``NoRouteToHostException``
            com.sun.star.io.ConnectException: ``ConnectException``
            com.sun.star.auth.AuthenticationFailedException: ``AuthenticationFailedException``
            com.sun.star.mail.MailException: ``MailException``
        """
        ...
    def disconnect(self) -> None:
        """
        Disconnect from a mail service.

        Raises:
            com.sun.star.mail.MailException: ``MailException``
        """
        ...
    def getCurrentConnectionContext(self) -> 'XCurrentContext_c9110c7a':
        """
        Return the context of the current connection.
        
        The context contains information like the server name, port, connection type etc.

        Raises:
            com.sun.star.io.NotConnectedException: ``NotConnectedException``
        """
        ...
    def getSupportedConnectionTypes(self) -> 'typing.Tuple[str, ...]':
        """
        Returns all connection types which are supported to connect to the mail service.
        
        At least support insecure connections must be supported. Currently defined connection types are (the values should be handled case insensitive): \"Insecure\" - insecure connections \"SSL\" - Secure Socket Layer 2.0/3.0 based connection
        """
        ...
    def isConnected(self) -> bool:
        """
        Returns whether a connection to a mail service currently exist or not.
        """
        ...
    def removeConnectionListener(self, xListener: 'XConnectionListener_aaa0e59') -> None:
        """
        Unregister a connection listener.
        """
        ...


