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
# Namespace: com.sun.star.chart2.data
from __future__ import annotations
import typing

from ...beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_data_provider import XDataProvider as XDataProvider_122f0e31
from .x_range_xml_conversion import XRangeXMLConversion as XRangeXMLConversion_6cef1070
from ...lang.x_component import XComponent as XComponent_98dc0ab5
from ...lang.x_initialization import XInitialization as XInitialization_d46c0cca
from ...sdbc.x_parameters import XParameters as XParameters_a36c0b10
from ...sdbc.x_row_set import XRowSet as XRowSet_7a090960
if typing.TYPE_CHECKING:
    from ...sdbc.x_connection import XConnection as XConnection_a36a0b0c


class XDatabaseDataProvider(XPropertySet_bc180bfa, XDataProvider_122f0e31, XRangeXMLConversion_6cef1070, XComponent_98dc0ab5, XInitialization_d46c0cca, XParameters_a36c0b10, XRowSet_7a090960):
    """
    identifies a XDataProvider for result sets.

    See Also:
        `API XDatabaseDataProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1data_1_1XDatabaseDataProvider.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.chart2.data.XDatabaseDataProvider'

    @property
    def ActiveConnection(self) -> XConnection_a36a0b0c:
        """
        specifies the active connection which is used to create the resulting report.
        """
        ...
    @ActiveConnection.setter
    def ActiveConnection(self, value: XConnection_a36a0b0c) -> None:
        ...
    @property
    def ApplyFilter(self) -> bool:
        """
        indicates whether the filter should be applied or not, default is FALSE.
        """
        ...
    @ApplyFilter.setter
    def ApplyFilter(self, value: bool) -> None:
        ...
    @property
    def Command(self) -> str:
        """
        is the command which should be executed, the type of command depends on the CommandType.
        
        In case of a CommandType of CommandType.COMMAND, means in case the Command specifies an SQL statement, the inherited com.sun.star.sdbc.RowSet.EscapeProcessing becomes relevant:It then can be to used to specify whether the SQL statement should be analyzed on the client side before sending it to the database server.The default value for com.sun.star.sdbc.RowSet.EscapeProcessing is TRUE. By switching it to FALSE, you can pass backend-specific SQL statements, which are not standard SQL, to your database.
        """
        ...
    @Command.setter
    def Command(self, value: str) -> None:
        ...
    @property
    def CommandType(self) -> int:
        """
        specifies the type of the command to be executed to retrieve a result set.
        
        Command needs to be interpreted depending on the value of this property.
        
        This property is only meaningful together with the Command property, thus either both or none of them are present.
        """
        ...
    @CommandType.setter
    def CommandType(self, value: int) -> None:
        ...
    @property
    def DataSourceName(self) -> str:
        """
        is the name of the data source to use, this could be a named data source or the URL of a data access component.
        """
        ...
    @DataSourceName.setter
    def DataSourceName(self, value: str) -> None:
        ...
    @property
    def DetailFields(self) -> typing.Tuple[str, ...]:
        """
        is used for subreports and contains the names of the columns of the subreport which are related to the master fields of the parent report.
        
        Entries in this sequence can either denote column names in the sub report, or parameter names.For instance, you could base the report on the SQL statement SELECT * FROM invoices WHERE cust_ref = :cid, and add cid to the DetailFields property. In this case, the parameter will be filled from the corresponding master field.Alternatively, you could simply base your report on the table invoices, and add the column name cust_ref to the DetailFields. In this case, and implicit filter clause WHERE cust_ref = :<new_param_name> will be created, and the artificial parameter will be filled from the corresponding master field.If a string in this property denotes both a column name and a parameter name, it is undefined which way it is interpreted, but implementations of the service are required to either decide for the parameter or the column, and proceed as usual.
        
        The columns specified herein typically represent a part of the primary key fields or their aliases of the detail report.
        
        If the report is no sub report (e.g. its parent is not a report itself), this property is not evaluated.
        """
        ...
    @DetailFields.setter
    def DetailFields(self, value: typing.Tuple[str, ...]) -> None:
        ...
    @property
    def EscapeProcessing(self) -> bool:
        """
        specifies if the Command should be analyzed on the client side before sending it to the database server.
        
        The default value of this property is TRUE. By switching it to FALSE, you can pass backend-specific SQL statements, which are not standard SQL, to your database.
        
        This property is usually present together with the Command and CommandType properties, and is evaluated if and only if CommandType equals CommandType.COMMAND.
        """
        ...
    @EscapeProcessing.setter
    def EscapeProcessing(self, value: bool) -> None:
        ...
    @property
    def Filter(self) -> str:
        """
        specifies an additional filter to optionally use.
        
        The Filter string has to form a SQL WHERE-clause, without the WHERE-string itself.
        
        If a DataSourceName, Command and CommandType are specified, a RowSet can be created with this information. If the results provided by the row set are to be additionally filtered, the Filter property can be used.
        
        Note that the Filter property does not make sense if a resultSet has been specified in the DataAccessDescriptor.
        """
        ...
    @Filter.setter
    def Filter(self, value: str) -> None:
        ...
    @property
    def GroupBy(self) -> str:
        """
        additional group by for the row set
        """
        ...
    @GroupBy.setter
    def GroupBy(self, value: str) -> None:
        ...
    @property
    def HavingClause(self) -> str:
        """
        additional having clause for the row set
        """
        ...
    @HavingClause.setter
    def HavingClause(self, value: str) -> None:
        ...
    @property
    def MasterFields(self) -> typing.Tuple[str, ...]:
        """
        is used for subreports and contains the names of columns of the parent report.
        
        These columns are typically the foreign key fields of the parent report. The values of these columns are used to identify the data for the subreport. Each time the parent report changes its current row, the subreport requeries it's data based on the values of the master fields.
        
        If the report is no sub report (e.g. its parent is not a report itself), this property is not evaluated.
        """
        ...
    @MasterFields.setter
    def MasterFields(self, value: typing.Tuple[str, ...]) -> None:
        ...
    @property
    def Order(self) -> str:
        """
        is an additional sort order definition for a row set.
        """
        ...
    @Order.setter
    def Order(self, value: str) -> None:
        ...
    @property
    def RowLimit(self) -> int:
        """
        specifies the maximal count of rows which should be fetched.
        
        A value of zero implies that no limit exists.
        """
        ...
    @RowLimit.setter
    def RowLimit(self, value: int) -> None:
        ...

