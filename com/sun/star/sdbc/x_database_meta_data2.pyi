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
# Namespace: com.sun.star.sdbc
from __future__ import annotations
import typing

from .x_database_meta_data import XDatabaseMetaData as XDatabaseMetaData_eafd0d12
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73


class XDatabaseMetaData2(XDatabaseMetaData_eafd0d12):
    """
    extends the XDatabaseMetaData interface to allow retrieval of additional information.

    See Also:
        `API XDatabaseMetaData2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XDatabaseMetaData2.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sdbc.XDatabaseMetaData2'

    def getConnectionInfo(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        """
        complements XDatabaseMetaData.getURL by returning the settings which, upon construction of the connection, have been used besides the connection URL.
        """
        ...


