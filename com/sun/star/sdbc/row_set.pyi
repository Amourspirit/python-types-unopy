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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sdbc
from __future__ import annotations
import typing
from .result_set import ResultSet as ResultSet_8ecf0a4f
from .x_parameters import XParameters as XParameters_a36c0b10
from .x_row_set import XRowSet as XRowSet_7a090960
if typing.TYPE_CHECKING:
    from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6

class RowSet(ResultSet_8ecf0a4f, XParameters_a36c0b10, XRowSet_7a090960):
    """
    Service Class

    is a client side ResultSet, which combines the characteristics of a com.sun.star.sdbc.Statement and a com.sun.star.sdbc.ResultSet.
    
    It acts like a typical bean. Before you use the RowSet, you have to specify a set of properties like a DataSource and a Command and other properties known of Statement. Afterwards, you can populate the RowSet by its execute method to fill the set with data.
    
    On the one hand, a RowSet can be used as a short cut to retrieve the data of a DataSource. You don't have to establish a connection, create a Statement, and then create a ResultSet. On the other hand, a row set can be used to implement capabilities for a result set, which are not supported by a driver result set, like caching strategies or update capabilities.

    See Also:
        `API RowSet <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbc_1_1RowSet.html>`_
    """
    @property
    def Command(self) -> str:
        """
        is the command which should be executed.
        """
        ...
    @Command.setter
    def Command(self, value: str) -> None:
        ...
    @property
    def DataSourceName(self) -> str:
        """
        is the name of a named datasource to use.
        """
        ...
    @DataSourceName.setter
    def DataSourceName(self, value: str) -> None:
        ...
    @property
    def EscapeProcessing(self) -> bool:
        """
        returns if escape processing is on or off.
        
        If escape scanning is on (the default), the driver will do escape substitution before sending the SQL to the database. This is only evaluated, if the CommandType is COMMAND.
        """
        ...
    @EscapeProcessing.setter
    def EscapeProcessing(self, value: bool) -> None:
        ...
    @property
    def MaxFieldSize(self) -> int:
        """
        returns the maximum number of bytes allowed for any column value.
        
        This limit is the maximum number of bytes that can be returned for any column value. The limit applies only to com.sun.star.sdbc.DataType.BINARY , com.sun.star.sdbc.DataType.VARBINARY , com.sun.star.sdbc.DataType.LONGVARBINARY , com.sun.star.sdbc.DataType.CHAR , com.sun.star.sdbc.DataType.VARCHAR , and com.sun.star.sdbc.DataType.LONGVARCHAR columns. If the limit is exceeded, the excess data is silently discarded. There is no limitation, if set to zero.
        """
        ...
    @MaxFieldSize.setter
    def MaxFieldSize(self, value: int) -> None:
        ...
    @property
    def MaxRows(self) -> int:
        """
        retrieves the maximum number of rows that a ResultSet can contain.
        
        If the limit is exceeded, the excess rows are silently dropped. There is no limitation, if set to zero.
        """
        ...
    @MaxRows.setter
    def MaxRows(self, value: int) -> None:
        ...
    @property
    def Password(self) -> str:
        """
        determines the user for whom to open the connection.
        """
        ...
    @Password.setter
    def Password(self, value: str) -> None:
        ...
    @property
    def QueryTimeOut(self) -> int:
        """
        retrieves the number of seconds the driver will wait for a Statement to execute.
        
        If the limit is exceeded, a com.sun.star.sdbc.SQLException is thrown. There is no limitation, if set to zero.
        """
        ...
    @QueryTimeOut.setter
    def QueryTimeOut(self, value: int) -> None:
        ...
    @property
    def ResultSetType(self) -> int:
        """
        determine the result set type.
        """
        ...
    @ResultSetType.setter
    def ResultSetType(self, value: int) -> None:
        ...
    @property
    def TransactionIsolation(self) -> int:
        """
        indicates the transaction isolation level, which should be used for the connection.
        """
        ...
    @TransactionIsolation.setter
    def TransactionIsolation(self, value: int) -> None:
        ...
    @property
    def TypeMap(self) -> XNameAccess_e2ab0cf6:
        """
        is the type map that will be used for the custom mapping of SQL structured types and distinct types.
        """
        ...
    @TypeMap.setter
    def TypeMap(self, value: XNameAccess_e2ab0cf6) -> None:
        ...
    @property
    def URL(self) -> str:
        """
        is the connection URL.
        
        Could be used instead of the DataSourceName.
        """
        ...
    @URL.setter
    def URL(self, value: str) -> None:
        ...
    @property
    def User(self) -> str:
        """
        determines the user for whom to open the connection.
        """
        ...
    @User.setter
    def User(self, value: str) -> None:
        ...

