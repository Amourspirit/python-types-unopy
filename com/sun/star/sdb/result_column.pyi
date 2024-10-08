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
# Namespace: com.sun.star.sdb
from __future__ import annotations
from .column_settings import ColumnSettings as ColumnSettings_bbba0c00
from ..sdbcx.column import Column as Column_7b1d098a

class ResultColumn(ColumnSettings_bbba0c00, Column_7b1d098a):
    """
    Service Class

    describes a column of a result set.

    See Also:
        `API ResultColumn <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1ResultColumn.html>`_
    """
    @property
    def CatalogName(self) -> str:
        """
        gets a column's table's catalog name.
        """
        ...
    @CatalogName.setter
    def CatalogName(self, value: str) -> None:
        ...
    @property
    def DisplaySize(self) -> int:
        """
        indicates the column's normal max width in chars.
        """
        ...
    @DisplaySize.setter
    def DisplaySize(self, value: int) -> None:
        ...
    @property
    def IsCaseSensitive(self) -> bool:
        """
        indicates that a column is case sensitive.
        """
        ...
    @IsCaseSensitive.setter
    def IsCaseSensitive(self, value: bool) -> None:
        ...
    @property
    def IsDefinitelyWritable(self) -> bool:
        """
        indicates whether a write on the column will definitely succeed.
        """
        ...
    @IsDefinitelyWritable.setter
    def IsDefinitelyWritable(self, value: bool) -> None:
        ...
    @property
    def IsReadOnly(self) -> bool:
        """
        indicates whether a column is definitely, not writable.
        """
        ...
    @IsReadOnly.setter
    def IsReadOnly(self, value: bool) -> None:
        ...
    @property
    def IsSearchable(self) -> bool:
        """
        indicates whether the column can be used in a Where clause.
        """
        ...
    @IsSearchable.setter
    def IsSearchable(self, value: bool) -> None:
        ...
    @property
    def IsSigned(self) -> bool:
        """
        indicates whether values in the column are signed numbers.
        """
        ...
    @IsSigned.setter
    def IsSigned(self, value: bool) -> None:
        ...
    @property
    def IsWritable(self) -> bool:
        """
        indicates whether it is possible for a write on the column to succeed.
        """
        ...
    @IsWritable.setter
    def IsWritable(self, value: bool) -> None:
        ...
    @property
    def Label(self) -> str:
        """
        gets the suggested column title for use in printouts and displays.
        """
        ...
    @Label.setter
    def Label(self, value: str) -> None:
        ...
    @property
    def SchemaName(self) -> str:
        """
        gets a column's schema name.
        """
        ...
    @SchemaName.setter
    def SchemaName(self, value: str) -> None:
        ...
    @property
    def ServiceName(self) -> str:
        """
        returns the fully-qualified name of the service whose instances are manufactured if the method com.sun.star.sdbc.XRow.getObject)= is called to retrieve a value from the column.
        """
        ...
    @ServiceName.setter
    def ServiceName(self, value: str) -> None:
        ...
    @property
    def TableName(self) -> str:
        """
        gets a column's table name.
        """
        ...
    @TableName.setter
    def TableName(self, value: str) -> None:
        ...

