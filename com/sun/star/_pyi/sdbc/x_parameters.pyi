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
# Namespace: com.sun.star.sdbc
from typing_extensions import Literal
import typing
import uno
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from .x_array import XArray as XArray_708108fb
    from .x_blob import XBlob as XBlob_6773087b
    from .x_clob import XClob as XClob_6777087c
    from .x_ref import XRef as XRef_5f110819
    from ..util.date import Date as Date_60040844
    from ..util.date_time import DateTime as DateTime_84de09d3
    from ..util.time import Time as Time_604e0855

class XParameters(XInterface_8f010a43):
    """
    is used for parameter setting, commonly implemented in conjunction with PreparedStatements.
    
    Note: The setXXX methods for setting IN parameter values must specify types that are compatible with the defined SQL type of the input parameter. For instance, if the IN parameter has SQL type Integer, then the method com.sun.star.sdbc.XParameters.setInt() should be used.
    
    If arbitrary parameter type conversions are required, the method com.sun.star.sdbc.XParameters.setObject() should be used with a target SQL type. Example of setting a parameter; con is an active connection.

    See Also:
        `API XParameters <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XParameters.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sdbc.XParameters']

    def clearParameters(self) -> None:
        """
        clears the current parameter values immediately.
        
        In general, parameter values remain in force for repeated use of a Statement. Setting a parameter value automatically clears its previous value. However, in some cases it is useful to immediately release the resources used by the current parameter values; this can be done by calling clearParameters.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setArray(self, parameterIndex: int, x: 'XArray_708108fb') -> None:
        """
        sets an Array parameter.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setBinaryStream(self, parameterIndex: int, x: 'XInputStream_98d40ab4', length: int) -> None:
        """
        sets the designated parameter to the given input stream, which will have the specified number of bytes.
        
        When a very large binary value is input to a LONGVARBINARY or LONGVARCHAR parameter, it may be more practical to send it via an com.sun.star.io.XInputStream . SDBC will read the data from the stream as needed, until it reaches end-of-file.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setBlob(self, parameterIndex: int, x: 'XBlob_6773087b') -> None:
        """
        sets a BLOB parameter.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setBoolean(self, parameterIndex: int, x: bool) -> None:
        """
        sets the designated parameter to a boolean value.
        
        The driver converts this to a SQL BIT value when it sends it to the database.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setByte(self, parameterIndex: int, x: int) -> None:
        """
        sets the designated parameter to a byte value.
        
        The driver converts this to a SQL TINYINT value when it sends it to the database.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setBytes(self, parameterIndex: int, x: uno.ByteSequence) -> None:
        """
        sets the designated parameter to a sequence of bytes.
        
        The driver converts this to a SQL VARBINARY or LONGVARBINARY (depending on the argument's size relative to the driver's limits on VARBINARYs) when it sends it to the database.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setCharacterStream(self, parameterIndex: int, x: 'XInputStream_98d40ab4', length: int) -> None:
        """
        sets the designated parameter to the given input stream, which will have the specified number of bytes.
        
        When a very large binary value is input to a LONGVARCHAR parameter, it may be more practical to send it via a com.sun.star.io.XInputStream . SDBC will read the data from the stream as needed, until it reaches end-of-file.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setClob(self, parameterIndex: int, x: 'XClob_6777087c') -> None:
        """
        sets a CLOB parameter.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setDate(self, parameterIndex: int, x: 'Date_60040844') -> None:
        """
        sets the designated parameter to a date value.
        
        The driver converts this to a SQL DATE value when it sends it to the database.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setDouble(self, parameterIndex: int, x: float) -> None:
        """
        sets the designated parameter to a double value.
        
        The driver converts this to a SQL DOUBLE value when it sends it to the database.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setFloat(self, parameterIndex: int, x: float) -> None:
        """
        sets the designated parameter to a float value.
        
        The driver converts this to a SQL FLOAT value when it sends it to the database.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setInt(self, parameterIndex: int, x: int) -> None:
        """
        sets the designated parameter to a long value.
        
        The driver converts this to a SQL INTEGER value when it sends it to the database.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setLong(self, parameterIndex: int, x: int) -> None:
        """
        sets the designated parameter to a hyper value.
        
        The driver converts this to a SQL BIGINT value when it sends it to the database.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setNull(self, parameterIndex: int, sqlType: int) -> None:
        """
        sets the designated parameter to SQL NULL.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setObject(self, parameterIndex: int, x: object) -> None:
        """
        sets the value of a parameter using an any.
        
        The given object will be converted to the targetSqlType before being sent to the database. If the object has a custom mapping (is of a class implementing SQLData), the SDBC driver should call its method writeSQL to write it to the SQL data stream. If, on the other hand, the object is of a service implementing Ref, Blob, Clob, Struct, or Array, the driver should pass it to the database as a value of the corresponding SQL type.
        
        Note that this method may be used to pass database-specific abstract data types.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setObjectNull(self, parameterIndex: int, sqlType: int, typeName: str) -> None:
        """
        sets the designated parameter to SQL NULL.
        
        This version of setNull should be used for user-named types and REF type parameters. Examples of user-named types include: STRUCT, DISTINCT, OBJECT, and named array types.
        
        Note: To be portable, applications must give the SQL type code and the fully-qualified SQL type name when specifying a NULL user-defined or REF parameter. In the case of a user-named type the name is the type name of the parameter itself. For a REF parameter the name is the type name of the referenced type. If a SDBC driver does not need the type code or type name information, it may ignore it. Although it is intended for user-named and Ref parameters, this method may be used to set a null parameter of any JDBC type. If the parameter does not have a user-named or REF type, the given typeName is ignored.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setObjectWithInfo(self, parameterIndex: int, x: object, targetSqlType: int, scale: int) -> None:
        """
        set a value from the Datatype ANY for a parameter.
        
        The given object will be converted to the targetSqlType before being sent to the database. If the object has a custom mapping (is of a class implementing SQLData), the SDBC driver should call its method writeSQL to write it to the SQL data stream. If, on the other hand, the object is of a service implementing Ref, Blob, Clob, Struct, or Array, the driver should pass it to the database as a value of the corresponding SQL type.
        
        Note that this method may be used to pass database-specific abstract data types.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setRef(self, parameterIndex: int, x: 'XRef_5f110819') -> None:
        """
        sets a REF(&lt;structured-type&gt;) parameter.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setShort(self, parameterIndex: int, x: int) -> None:
        """
        sets the designated parameter to a short value.
        
        The driver converts this to a SQL SMALLINT value when it sends it to the database.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setString(self, parameterIndex: int, x: str) -> None:
        """
        sets the designated parameter to a string value.
        
        The driver converts this to a SQL VARCHAR or LONGVARCHAR value (depending on the argument's size relative to the driver's limits on VARCHARs) when it sends it to the database.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setTime(self, parameterIndex: int, x: 'Time_604e0855') -> None:
        """
        sets the designated parameter to a time value.
        
        The driver converts this to a SQL TIME value when it sends it to the database.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def setTimestamp(self, parameterIndex: int, x: 'DateTime_84de09d3') -> None:
        """
        sets the designated parameter to a datetime value.
        
        The driver converts this to a SQL TIMESTAMP value when it sends it to the database.

        Raises:
            SQLException: ``SQLException``
        """
        ...


