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
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing
from ..table.table_sort_descriptor import TableSortDescriptor as TableSortDescriptor_18ef0ebf
if typing.TYPE_CHECKING:
    from ..table.cell_address import CellAddress as CellAddress_ae5f0b56

class SheetSortDescriptor(TableSortDescriptor_18ef0ebf):
    """
    Service Class

    a description of how a cell range is to be sorted.
    
    This service extends the com.sun.star.table.TableSortDescriptor service with spreadsheet specific properties.

    See Also:
        `API SheetSortDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1SheetSortDescriptor.html>`_
    """
    @property
    def BindFormatsToContent(self) -> bool:
        """
        specifies if cell formats are moved with the contents they belong to.
        """
        ...
    @BindFormatsToContent.setter
    def BindFormatsToContent(self, value: bool) -> None:
        ...
    @property
    def CopyOutputData(self) -> bool:
        """
        specifies if the sorted data should be copied to another position in the document.
        """
        ...
    @CopyOutputData.setter
    def CopyOutputData(self, value: bool) -> None:
        ...
    @property
    def IsUserListEnabled(self) -> bool:
        """
        specifies if a user defined sorting list is used.
        """
        ...
    @IsUserListEnabled.setter
    def IsUserListEnabled(self, value: bool) -> None:
        ...
    @property
    def OutputPosition(self) -> CellAddress_ae5f0b56:
        """
        specifies the position where sorted data are to be copied.
        
        This property is only used, if SheetSortDescriptor.CopyOutputData is TRUE.
        """
        ...
    @OutputPosition.setter
    def OutputPosition(self, value: CellAddress_ae5f0b56) -> None:
        ...
    @property
    def UserListIndex(self) -> int:
        """
        specifies which user defined sorting list is used.
        
        This property is only used, if SheetSortDescriptor.IsUserListEnabled is TRUE.
        """
        ...
    @UserListIndex.setter
    def UserListIndex(self, value: int) -> None:
        ...

