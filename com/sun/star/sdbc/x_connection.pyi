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

from .x_closeable import XCloseable as XCloseable_98290a86
if typing.TYPE_CHECKING:
    from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
    from .x_database_meta_data import XDatabaseMetaData as XDatabaseMetaData_eafd0d12
    from .x_prepared_statement import XPreparedStatement as XPreparedStatement_fbc80de4
    from .x_statement import XStatement as XStatement_98e90ab1


class XConnection(XCloseable_98290a86):
    """
    represents a connection (session) with a specific database.
    
    Within the context of a Connection, SQL statements are executed and results are returned.
    
    A Connection's database is able to provide information describing its tables, its supported SQL grammar, its stored procedures, and the capabilities of this connection. This information is obtained with the com.sun.star.sdbc.XDatabaseMetaData.getMetaData() method.

    See Also:
        `API XConnection <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XConnection.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sdbc.XConnection'

    def commit(self) -> None:
        """
        makes all changes made since the previous commit/rollback permanent and releases any database locks currently held by the Connection.
        
        This method should be used only when auto-commit mode has been disabled.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def createStatement(self) -> XStatement_98e90ab1:
        """
        creates a new com.sun.star.sdbc.Statement object for sending SQL statements to the database.
        
        SQL statements without parameters are normally executed using Statement objects. If the same SQL statement is executed many times, it is more efficient to use a com.sun.star.sdbc.PreparedStatement.
        
        Result sets created using the returned Statement will have forward-only type, and read-only concurrency, by default.
        
        Escape processing for the SQL-Statement is enabled, by default.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def getAutoCommit(self) -> bool:
        """
        gets the current auto-commit state.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def getCatalog(self) -> str:
        """
        returns the Connection's current catalog name.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def getMetaData(self) -> XDatabaseMetaData_eafd0d12:
        """
        gets the metadata regarding this connection's database.
        
        A Connection's database is able to provide information describing its tables, its supported SQL grammar, its stored procedures, the capabilities of this connection, and so on. This information is made available through a DatabaseMetaData object.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def getTransactionIsolation(self) -> int:
        """
        gets this Connection's current transaction isolation level.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def getTypeMap(self) -> XNameAccess_e2ab0cf6:
        """
        gets the type map object associated with this connection.
        
        Only drivers which implement the custom type mapping facility will return an object otherwise NULL could be returned.
        
        Unless the application has added an entry to the type map, the map returned will be empty.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def isClosed(self) -> bool:
        """
        tests to see if a connection is closed.
        
        Note:  A Connection is automatically closed if no one references it anymore. Certain fatal errors also result in a closed Connection.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def isReadOnly(self) -> bool:
        """
        tests to see if the connection is in read-only mode.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def nativeSQL(self, sql: str) -> str:
        """
        converts the given SQL statement into the system's native SQL grammar.
        
        A driver may convert the JDBC SQL grammar into its system's native SQL grammar prior to sending it; this method returns the native form of the statement that the driver would have sent.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def prepareCall(self, sql: str) -> XPreparedStatement_fbc80de4:
        """
        creates a com.sun.star.sdbc.CallableStatement object for calling database stored procedures.
        
        The CallableStatement provides methods for setting up its IN and OUT parameters, and methods for executing the call to a stored procedure.
        
        Note:  This method is optimized for handling stored procedure call statements. Some drivers may send the call statement to the database when the method prepareCall is done; others may wait until the CallableStatement is executed. This has no direct effect on users; however, it does affect which method throws certain SQLExceptions. Result sets created using the returned CallableStatement will have forward-only type and read-only concurrency, by default.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def prepareStatement(self, sql: str) -> XPreparedStatement_fbc80de4:
        """
        creates a com.sun.star.sdbc.PreparedStatement object for sending parameterized SQL statements to the database.
        
        A SQL statement with or without IN parameters can be pre-compiled and stored in a PreparedStatement object. This object can then be used to efficiently execute this statement multiple times.
        
        Note:  This method is optimized for handling parametric SQL statements that benefit from precompilation. If the driver supports precompilation, the method prepareStatement will send the statement to the database for precompilation. Some drivers may not support precompilation. In this case, the statement may not be sent to the database until the com.sun.star.sdbc.PreparedStatement is executed. This has no direct effect on users; however, it does affect which method throws certain SQLExceptions.
        
        Result sets created using the returned PreparedStatement will have forward-only type and read-only concurrency, by default.
        
        Escape processing for the SQL-Statement is enabled, by default.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def rollback(self) -> None:
        """
        drops all changes made since the previous commit/rollback and releases any database locks currently held by this Connection.
        
        This method should be used only when auto-commit has been disabled.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setAutoCommit(self, autoCommit: bool) -> None:
        """
        sets this connection's auto-commit mode.
        
        If a connection is in auto-commit mode, then all its SQL statements will be executed and committed as individual transactions. Otherwise, its SQL statements are grouped into transactions that are terminated by a call to either the method com.sun.star.sdbc.XConnection.commit() or the method com.sun.star.sdbc.XConnection.rollback(). By default, new connections are in auto-commit mode.
        
        The commit occurs when the statement completes or the next execute occurs, whichever comes first. In the case of statements returning a ResultSet, the statement completes when the last row of the ResultSet has been retrieved or the ResultSet has been closed. In advanced cases, a single statement may return multiple results as well as output parameter values. In these cases the commit occurs when all results and output parameter values have been retrieved.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setCatalog(self, catalog: str) -> None:
        """
        sets a catalog name in order to select a subspace of this Connection's database in which to work.
        
        If the driver does not support catalogs, it will silently ignore this request.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setReadOnly(self, readOnly: bool) -> None:
        """
        puts this connection in read-only mode as a hint to enable database optimizations.
        
        Note:  This method cannot be called while in the middle of a transaction. Calling setReadOnly with TRUE does not necessarily cause writes to be prohibited.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setTransactionIsolation(self, level: int) -> None:
        """
        attempts to change the transaction isolation level to the one given.
        
        The constants defined in com.sun.star.sdbc.TransactionIsolation are the possible transaction isolation levels.
        
        Note:  This method cannot be called while in the middle of a transaction.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setTypeMap(self, typeMap: XNameAccess_e2ab0cf6) -> None:
        """
        installs the given type map as the type map for this connection.
        
        The type map will be used for the custom mapping of SQL structured types and distinct types.
        
        Only if the driver supports custom type mapping is the setting of a map allowed.

        Raises:
            SQLException: ``SQLException``
        """
        ...


