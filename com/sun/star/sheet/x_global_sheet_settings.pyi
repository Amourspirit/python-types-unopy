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

from abc import ABC


class XGlobalSheetSettings(ABC):
    """
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API XGlobalSheetSettings <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XGlobalSheetSettings.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sheet.XGlobalSheetSettings'

    @property
    def UserLists(self) -> typing.Tuple[str, ...]:
        """
        contains the string lists used for sorting and filling.
        
        Each string contains the members of a list, separated by commas.
        """
        ...
    @UserLists.setter
    def UserLists(self, value: typing.Tuple[str, ...]) -> None:
        ...
    @property
    def DoAutoComplete(self) -> bool:
        """
        specifies whether automatic completion of text in a cell is used.
        """
        ...
    @DoAutoComplete.setter
    def DoAutoComplete(self, value: bool) -> None:
        ...
    @property
    def EnterEdit(self) -> bool:
        """
        specifies whether the enter key can be used to start editing a cell.
        """
        ...
    @EnterEdit.setter
    def EnterEdit(self, value: bool) -> None:
        ...
    @property
    def ExpandReferences(self) -> bool:
        """
        specifies whether formula references are extended when cells are inserted below or to the right of them.
        """
        ...
    @ExpandReferences.setter
    def ExpandReferences(self, value: bool) -> None:
        ...
    @property
    def ExtendFormat(self) -> bool:
        """
        specifies whether cell formatting is extended when entering data.
        """
        ...
    @ExtendFormat.setter
    def ExtendFormat(self, value: bool) -> None:
        ...
    @property
    def LinkUpdateMode(self) -> int:
        """
        specifies the update mode for external linked data.
        
        0 = always
        
        1 = never
        
        2 = on demand
        """
        ...
    @LinkUpdateMode.setter
    def LinkUpdateMode(self, value: int) -> None:
        ...
    @property
    def MarkHeader(self) -> bool:
        """
        specifies whether the current selection is highlighted in column and row headers.
        """
        ...
    @MarkHeader.setter
    def MarkHeader(self, value: bool) -> None:
        ...
    @property
    def Metric(self) -> int:
        """
        contains the metric for all spreadsheet documents.
        """
        ...
    @Metric.setter
    def Metric(self, value: int) -> None:
        ...
    @property
    def MoveDirection(self) -> int:
        """
        contains the direction the cursor moves after entering cells.
        """
        ...
    @MoveDirection.setter
    def MoveDirection(self, value: int) -> None:
        ...
    @property
    def MoveSelection(self) -> bool:
        """
        specifies whether the cursor is moved after entering into cells.
        """
        ...
    @MoveSelection.setter
    def MoveSelection(self, value: bool) -> None:
        ...
    @property
    def PrintAllSheets(self) -> bool:
        """
        specifies whether all sheets or only selected sheets are printed.
        """
        ...
    @PrintAllSheets.setter
    def PrintAllSheets(self, value: bool) -> None:
        ...
    @property
    def PrintEmptyPages(self) -> bool:
        """
        specifies whether empty pages are printed.
        """
        ...
    @PrintEmptyPages.setter
    def PrintEmptyPages(self, value: bool) -> None:
        ...
    @property
    def RangeFinder(self) -> bool:
        """
        specifies whether ranges are highlighted on the sheet when editing a formula.
        """
        ...
    @RangeFinder.setter
    def RangeFinder(self, value: bool) -> None:
        ...
    @property
    def ReplaceCellsWarning(self) -> bool:
        """
        specifies whether a warning is shown before replacing cells (i.e.
        
        when pasting from clipboard).
        """
        ...
    @ReplaceCellsWarning.setter
    def ReplaceCellsWarning(self, value: bool) -> None:
        ...
    @property
    def Scale(self) -> int:
        """
        contains the default scale for new spreadsheet documents (in percent).
        
        There are several special values:
        
        -1 = Optimal width
        
        -2 = Show whole page
        
        -3 = Page width
        """
        ...
    @Scale.setter
    def Scale(self, value: int) -> None:
        ...
    @property
    def StatusBarFunction(self) -> int:
        """
        contains the function that is displayed in the status bar.
        """
        ...
    @StatusBarFunction.setter
    def StatusBarFunction(self, value: int) -> None:
        ...
    @property
    def UsePrinterMetrics(self) -> bool:
        """
        specifies whether printer metrics are used for display.
        """
        ...
    @UsePrinterMetrics.setter
    def UsePrinterMetrics(self, value: bool) -> None:
        ...
    @property
    def UseTabCol(self) -> bool:
        """
        specifies whether the enter key moves the cursor to the column it was in before using the tab key to change columns.
        """
        ...
    @UseTabCol.setter
    def UseTabCol(self, value: bool) -> None:
        ...


