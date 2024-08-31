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
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..container.x_enumeration_access import XEnumerationAccess as XEnumerationAccess_4bac0ffc
from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
from .x_sub_total_descriptor import XSubTotalDescriptor as XSubTotalDescriptor_19fd0ec6

class SubTotalDescriptor(XPropertySet_bc180bfa, XEnumerationAccess_4bac0ffc, XIndexAccess_f0910d6d, XSubTotalDescriptor_19fd0ec6):
    """
    Service Class

    represents a description of how subtotals are created.
    
    The descriptor contains properties and a collection of subtotal fields which control the behavior of operation.

    See Also:
        `API SubTotalDescriptor <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1SubTotalDescriptor.html>`_
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
    def EnableSort(self) -> bool:
        """
        specifies if the contents of the fields will be sorted to groups while performing a subtotal operation.
        """
        ...
    @EnableSort.setter
    def EnableSort(self, value: bool) -> None:
        ...
    @property
    def EnableUserSortList(self) -> bool:
        """
        specifies if a user defined sorting list is used.
        """
        ...
    @EnableUserSortList.setter
    def EnableUserSortList(self, value: bool) -> None:
        ...
    @property
    def InsertPageBreaks(self) -> bool:
        """
        specifies if page breaks are inserted after each group change.
        """
        ...
    @InsertPageBreaks.setter
    def InsertPageBreaks(self, value: bool) -> None:
        ...
    @property
    def IsCaseSensitive(self) -> bool:
        """
        specifies if the case of letters is important when comparing entries.
        """
        ...
    @IsCaseSensitive.setter
    def IsCaseSensitive(self, value: bool) -> None:
        ...
    @property
    def MaxFieldCount(self) -> int:
        """
        returns the maximum number of subtotal fields the descriptor can hold.
        
        This read-only property indicates the maximum count of fields the current implementation supports.
        """
        ...
    @MaxFieldCount.setter
    def MaxFieldCount(self, value: int) -> None:
        ...
    @property
    def SortAscending(self) -> bool:
        """
        specifies the sorting order if SubTotalDescriptor.EnableSort is set to TRUE.
        """
        ...
    @SortAscending.setter
    def SortAscending(self, value: bool) -> None:
        ...
    @property
    def UserSortListIndex(self) -> int:
        """
        specifies which user defined sorting list is used.
        
        This property is only used if SubTotalDescriptor.EnableUserSortList is TRUE.
        """
        ...
    @UserSortListIndex.setter
    def UserSortListIndex(self, value: int) -> None:
        ...

