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
# Namespace: com.sun.star.table
from __future__ import annotations
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from .x_cell_range import XCellRange as XCellRange_a2f70ad5

class TableRow(XPropertySet_bc180bfa, XCellRange_a2f70ad5):
    """
    Service Class

    represents a special cell range containing all cells of a single specific row in a table or spreadsheet.

    See Also:
        `API TableRow <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1table_1_1TableRow.html>`_
    """
    @property
    def Height(self) -> int:
        """
        contains the height of the row (in 1/100 mm).
        
        When hidden, it returns the height which the row would have, if it were visible.
        """
        ...
    @Height.setter
    def Height(self, value: int) -> None:
        ...
    @property
    def IsStartOfNewPage(self) -> bool:
        """
        is TRUE, if there is a manual vertical page break attached to the row.
        """
        ...
    @IsStartOfNewPage.setter
    def IsStartOfNewPage(self, value: bool) -> None:
        ...
    @property
    def IsVisible(self) -> bool:
        """
        is TRUE, if the row is visible.
        """
        ...
    @IsVisible.setter
    def IsVisible(self, value: bool) -> None:
        ...
    @property
    def OptimalHeight(self) -> bool:
        """
        is TRUE, if the row always keeps its optimal height.
        """
        ...
    @OptimalHeight.setter
    def OptimalHeight(self, value: bool) -> None:
        ...

