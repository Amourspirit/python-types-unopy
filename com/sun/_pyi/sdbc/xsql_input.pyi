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
# Namespace: com.sun.star.sdbc
from typing_extensions import Literal
import typing
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

class XSQLInput(XInterface_8f010a43):
    """
    represents an input stream that contains a stream of values representing an instance of a SQL structured or distinct type.
    
    This interface, used only for custom mapping, is used by the driver behind the scenes, and a programmer never directly invokes SQLInput methods.
    
    When the method getObject is called with an object of a service implementing the interface SQLData , the SDBC driver calls the method com.sun.star.sdbc.XSQLData.getSQLType() to determine the SQL type of the user-defined type (UDT) being custom mapped. The driver creates an instance of com.sun.star.sdbc.XSQLInput , populating it with the attributes of the UDT. The driver then passes the input stream to the method com.sun.star.sdbc.XSQLData.readSQL() , which in turn calls the XSQLInput.readXXX methods in its implementation for reading the attributes from the input stream.

    See Also:
        `API XSQLInput <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XSQLInput.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sdbc.XSQLInput']

    def readArray(self) -> 'XArray_708108fb':
        """
        reads an array from the stream.

        Raises:
            SQLException: ``SQLException``
        """
    def readBinaryStream(self) -> 'XInputStream_98d40ab4':
        """
        reads the next attribute in the stream as sequence of bytes.

        Raises:
            SQLException: ``SQLException``
        """
    def readBlob(self) -> 'XBlob_6773087b':
        """
        reads a BLOB from the stream.

        Raises:
            SQLException: ``SQLException``
        """
    def readBoolean(self) -> bool:
        """
        reads the next attribute in the stream as boolean.

        Raises:
            SQLException: ``SQLException``
        """
    def readByte(self) -> int:
        """
        reads the next attribute in the stream as byte.

        Raises:
            SQLException: ``SQLException``
        """
    def readBytes(self) -> 'typing.Tuple[int, ...]':
        """
        reads the next attribute in the stream as sequence of bytes.

        Raises:
            SQLException: ``SQLException``
        """
    def readCharacterStream(self) -> 'XInputStream_98d40ab4':
        """
        reads the next attribute in the stream as a Unicode string.

        Raises:
            SQLException: ``SQLException``
        """
    def readClob(self) -> 'XClob_6777087c':
        """
        reads a CLOB from the stream.

        Raises:
            SQLException: ``SQLException``
        """
    def readDate(self) -> 'Date_60040844':
        """
        reads the next attribute in the stream as date.

        Raises:
            SQLException: ``SQLException``
        """
    def readDouble(self) -> float:
        """
        reads the next attribute in the stream as double.

        Raises:
            SQLException: ``SQLException``
        """
    def readFloat(self) -> float:
        """
        reads the next attribute in the stream as float.

        Raises:
            SQLException: ``SQLException``
        """
    def readInt(self) -> int:
        """
        reads the next attribute in the stream as long.

        Raises:
            SQLException: ``SQLException``
        """
    def readLong(self) -> int:
        """
        reads the next attribute in the stream as hyper.

        Raises:
            SQLException: ``SQLException``
        """
    def readObject(self) -> object:
        """
        returns the datum at the head of the stream as an any.
        
        The actual type of the any returned is determined by the default type mapping, and any customizations present in this stream's type map.
        
        A type map is registered with the stream by the SDBC driver before the stream is passed to the application.
        
        When the datum at the head of the stream is a SQL NULL, the method returns VOID. If the datum is a SQL structured or distinct type, it determines the SQL type of the datum at the head of the stream, constructs an object of the appropriate service, and calls the method com.sun.star.sdbc.XSQLData.readSQL() on that object, which reads additional data from the stream using the protocol described for that method.

        Raises:
            SQLException: ``SQLException``
        """
    def readRef(self) -> 'XRef_5f110819':
        """
        reads a REF(&lt;structured-type&gt;) from the stream.

        Raises:
            SQLException: ``SQLException``
        """
    def readShort(self) -> int:
        """
        reads the next attribute in the stream as short.

        Raises:
            SQLException: ``SQLException``
        """
    def readString(self) -> str:
        """
        reads the next attribute in the stream as string.

        Raises:
            SQLException: ``SQLException``
        """
    def readTime(self) -> 'Time_604e0855':
        """
        reads the next attribute in the stream as time.

        Raises:
            SQLException: ``SQLException``
        """
    def readTimestamp(self) -> 'DateTime_84de09d3':
        """
        reads the next attribute in the stream as datetime.

        Raises:
            SQLException: ``SQLException``
        """
    def wasNull(self) -> bool:
        """
        determines whether the last value read was null.

        Raises:
            SQLException: ``SQLException``
        """

__all__ = ['XSQLInput']

