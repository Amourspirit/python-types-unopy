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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.connection
from .x_acceptor import XAcceptor as XAcceptor_d6eb0cc1

class Acceptor(XAcceptor_d6eb0cc1):
    """
    Service Class

    allows to accept connection attempts from another process.
    
    Acceptor is a delegating service. You can add further acceptors by giving them a service name com.sun.star.connection.Acceptor.xxx, where xxx is the connection type used in the connection string during accept()/connect() call.

    See Also:
        `API Acceptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1connection_1_1Acceptor.html>`_
    """
    ...

