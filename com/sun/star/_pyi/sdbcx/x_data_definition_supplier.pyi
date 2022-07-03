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
# Libre Office Version: 7.2
# Namespace: com.sun.star.sdbcx
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..sdbc.x_connection import XConnection as XConnection_a36a0b0c
    from .x_tables_supplier import XTablesSupplier as XTablesSupplier_e1ad0d23

class XDataDefinitionSupplier(XInterface_8f010a43):
    """
    provides the access to data definition beans from a connected database.

    See Also:
        `API XDataDefinitionSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbcx_1_1XDataDefinitionSupplier.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sdbcx.XDataDefinitionSupplier']

    def getDataDefinitionByConnection(self, connection: 'XConnection_a36a0b0c') -> 'XTablesSupplier_e1ad0d23':
        """
        returns at least the container of tables related to the given connection.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def getDataDefinitionByURL(self, url: str, info: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> 'XTablesSupplier_e1ad0d23':
        """
        returns at least the container of tables related to the given Database URL.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...


