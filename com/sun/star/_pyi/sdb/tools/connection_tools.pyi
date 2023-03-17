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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdb.tools
import typing
from .x_connection_tools import XConnectionTools as XConnectionTools_28110f19
if typing.TYPE_CHECKING:
    from ...sdbc.x_connection import XConnection as XConnection_a36a0b0c

class ConnectionTools(XConnectionTools_28110f19):
    """
    Service Class

    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API ConnectionTools <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1tools_1_1ConnectionTools.html>`_
    """
    def createWithConnection(self, Connection: 'XConnection_a36a0b0c') -> None:
        """
        """
        ...

