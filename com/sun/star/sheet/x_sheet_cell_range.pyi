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
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing

from ..table.x_cell_range import XCellRange as XCellRange_a2f70ad5
if typing.TYPE_CHECKING:
    from .x_spreadsheet import XSpreadsheet as XSpreadsheet_bc910bf1


class XSheetCellRange(XCellRange_a2f70ad5):
    """
    provides access to the spreadsheet that contains a cell range.

    See Also:
        `API XSheetCellRange <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSheetCellRange.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sheet.XSheetCellRange'

    def getSpreadsheet(self) -> XSpreadsheet_bc910bf1:
        """
        returns the spreadsheet interface which contains the cell range.
        """
        ...



