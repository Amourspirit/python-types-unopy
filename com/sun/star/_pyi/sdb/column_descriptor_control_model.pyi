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
# Libre Office Version: 7.2
# Namespace: com.sun.star.sdb
import typing
from ..awt.uno_control_model import UnoControlModel as UnoControlModel_c8ce0c58
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
    from ..sdbc.x_connection import XConnection as XConnection_a36a0b0c

class ColumnDescriptorControlModel(UnoControlModel_c8ce0c58):
    """
    Service Class

    specifies the standard model of a ColumnDescriptorControl.

    See Also:
        `API ColumnDescriptorControlModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1ColumnDescriptorControlModel.html>`_
    """
    @property
    def ActiveConnection(self) -> 'XConnection_a36a0b0c':
        """
        specifies the connection to a database.
        """
        ...
    @property
    def Border(self) -> int:
        """
        specifies the border style of the control.
        """
        ...
    @property
    def Column(self) -> 'XPropertySet_bc180bfa':
        """
        specifies the column descriptor where the values will be stored in.
        """
        ...
    @property
    def Enabled(self) -> bool:
        """
        determines whether the control is enabled or disabled.
        """
        ...
    @property
    def Tabstop(self) -> bool:
        """
        specifies that the control can be reached with the TAB key.
        """
        ...


