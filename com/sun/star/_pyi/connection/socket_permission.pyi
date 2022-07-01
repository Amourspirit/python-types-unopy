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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.connection
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class SocketPermission(object):
    """
    Struct Class

    This permission represents access to a network via sockets.
    
    A SocketPermission consists of a host specification and a set of actions specifying ways to connect to that host. The host is specified as
    
    The host is expressed as a DNS name, as a numerical IP address, or as \"localhost\" (for the local machine). The wildcard \"*\" may be included once in a DNS name host specification. If it is included, it must be in the leftmost position, as in \"*.sun.com\". The port or portrange is optional. A port specification of the form \"N-\", where N is a port number, signifies all ports numbered N and above, while a specification of the form \"-N\" indicates all ports numbered N and below.
    
    The possible ways to connect to the host are
    
    The \"listen\" action is only meaningful when used with \"localhost\". The \"resolve\" (resolve host/ip name service lookups) action is implied when any of the other actions are present. As an example of the creation and meaning of SocketPermissions, note that if the following permission
    
    is granted, it allows to connect to port 7777 on foo.bar.com, and to accept connections on that port. Similarly, if the following permission
    
    is granted, it allows that code to accept connections on, connect to, or listen on any port between 1024 and 65535 on the local host.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API SocketPermission <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1connection_1_1SocketPermission.html>`_
    """
    typeName: Literal['com.sun.star.connection.SocketPermission']

    def __init__(self, Host: typing.Optional[str] = ..., Actions: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Host (str, optional): Host value.
            Actions (str, optional): Actions value.
        """


    @property
    def Host(self) -> str:
        """
        target host with optional portrange
        """


    @property
    def Actions(self) -> str:
        """
        comma separated actions list
        """


