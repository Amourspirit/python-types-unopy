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
# Namespace: com.sun.star.text
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XTextTableCursor(XInterface_8f010a43):
    """
    The TextTableCursor provide methods to navigate through the table structure, to merge and split cells.

    See Also:
        `API XTextTableCursor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XTextTableCursor.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.text.XTextTableCursor'

    def getRangeName(self) -> str:
        """
        The name is the cell name of the top left table cell of the range concatenated by \":\" with the table cell name of the bottom left table cell of the cell range. If the range consists of one table cell only then the name of that table cell is returned.
        """
        ...
    def goDown(self, nCount: int, bExpand: bool) -> bool:
        """
        moves the cursor to the bottom neighbor cell.
        """
        ...
    def goLeft(self, nCount: int, bExpand: bool) -> bool:
        """
        moves the cursor to the left neighbor.
        """
        ...
    def goRight(self, nCount: int, bExpand: bool) -> bool:
        """
        moves the cursor to the right neighbor.
        """
        ...
    def goUp(self, nCount: int, bExpand: bool) -> bool:
        """
        moves the cursor to the top neighbor.
        """
        ...
    def gotoCellByName(self, aCellName: str, bExpand: bool) -> bool:
        """
        moves the cursor to the cell with the specified name.
        """
        ...
    def gotoEnd(self, bExpand: bool) -> None:
        """
        moves the cursor to the bottom right cell of the table.
        """
        ...
    def gotoStart(self, bExpand: bool) -> None:
        """
        moves the cursor to the top left cell of the table.
        """
        ...
    def mergeRange(self) -> bool:
        """
        merges the selected range of cells.
        """
        ...
    def splitRange(self, nCount: int, bHorizontal: bool) -> bool:
        """
        splits the range of cells.
        """
        ...


