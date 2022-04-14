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
# Namespace: com.sun.star.table
from typing_extensions import Literal
from .x_cell_range import XCellRange as XCellRange_a2f70ad5

class XCellCursor(XCellRange_a2f70ad5):
    """
    provides methods to control the position of a cell cursor.

    See Also:
        `API XCellCursor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1table_1_1XCellCursor.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.table.XCellCursor']

    def gotoEnd(self) -> None:
        """
        points the cursor to a single cell which is the end of a contiguous series of (filled) cells.
        """
    def gotoNext(self) -> None:
        """
        points the cursor to the next unprotected cell.
        
        If the sheet is not protected, this is the next cell to the right.
        """
    def gotoOffset(self, nColumnOffset: int, nRowOffset: int) -> None:
        """
        moves the origin of the cursor relative to the current position.
        """
    def gotoPrevious(self) -> None:
        """
        points the cursor to the previous unprotected cell.
        
        If the sheet is not protected, this is the next cell to the left.
        """
    def gotoStart(self) -> None:
        """
        points the cursor to a single cell which is the beginning of a contiguous series of (filled) cells.
        """

__all__ = ['XCellCursor']

