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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.script.vba
from typing_extensions import Literal
"""
Const

Constants used to identify VBA document events.

If one of these events is fired, a specific VBA macro in a specific document code module will be executed.

Each event expects some specific arguments to be passed to XVBAEventProcessor.processVbaEvent().

See Also:
    `API VBAEventId <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1script_1_1vba_1_1VBAEventId.html>`_
"""
NO_EVENT: Literal[-1]
"""
An identifier not corresponding to any VBA document event.
"""
AUTO_NEW: Literal[1]
"""
New document opened from template.

No arguments.
"""
AUTO_OPEN: Literal[2]
"""
Document opened (loaded).

No arguments.
"""
AUTO_CLOSE: Literal[3]
"""
Document about to be closed.

No arguments.
"""
AUTO_EXEC: Literal[4]
"""
Application start.

No arguments.
"""
AUTO_EXIT: Literal[5]
"""
Application exit.

No arguments.
"""
DOCUMENT_NEW: Literal[1001]
"""
New text document opened from template.

No arguments.
"""
DOCUMENT_OPEN: Literal[1002]
"""
Text document opened (loaded).

No arguments.
"""
DOCUMENT_CLOSE: Literal[1003]
"""
Document about to be closed.

No arguments.
"""
WORKBOOK_ACTIVATE: Literal[2001]
"""
Document activated.

No arguments.
"""
WORKBOOK_DEACTIVATE: Literal[2002]
"""
Document deactivated.

No arguments.
"""
WORKBOOK_OPEN: Literal[2003]
"""
Document opened (loaded).

No arguments.
"""
WORKBOOK_BEFORECLOSE: Literal[2004]
"""
Document about to be closed.

Arguments: [out] boolean bCancel.
"""
WORKBOOK_BEFOREPRINT: Literal[2005]
"""
Document about to be printed.

Arguments: [out] boolean bCancel.
"""
WORKBOOK_BEFORESAVE: Literal[2006]
"""
Document about to be saved.

Arguments: boolean bSaveAs, [out] boolean bCancel.
"""
WORKBOOK_AFTERSAVE: Literal[2007]
"""
Document has been saved.

Arguments: boolean bSuccess.
"""
WORKBOOK_NEWSHEET: Literal[2008]
"""
New sheet inserted.

Arguments: short nSheet.
"""
WORKBOOK_WINDOWACTIVATE: Literal[2009]
"""
Document window has been activated.

Arguments: XController aController.
"""
WORKBOOK_WINDOWDEACTIVATE: Literal[2010]
"""
Document window has been deactivated.

Arguments: XController aController.
"""
WORKBOOK_WINDOWRESIZE: Literal[2011]
"""
Document window has been resized.

Arguments: XController aController.
"""
WORKSHEET_ACTIVATE: Literal[2101]
"""
Worksheet has been activated (made visible).

Arguments: short nSheet.
"""
WORKSHEET_DEACTIVATE: Literal[2102]
"""
Worksheet has been activated (made visible).

Arguments: short nSheet.
"""
WORKSHEET_BEFOREDOUBLECLICK: Literal[2103]
"""
Double click in the sheet.

Arguments: XRange/XSheetCellRangeContainer aRange, [out] boolean bCancel.
"""
WORKSHEET_BEFORERIGHTCLICK: Literal[2104]
"""
Right click in the sheet.

Arguments: XRange/XSheetCellRangeContainer aRange, [out] boolean bCancel.
"""
WORKSHEET_CALCULATE: Literal[2105]
"""
Cells in sheet have been recalculated.

Arguments: short nSheet.
"""
WORKSHEET_CHANGE: Literal[2106]
"""
Cells in sheet have been changed.

Arguments: XRange/XSheetCellRangeContainer aRange.
"""
WORKSHEET_SELECTIONCHANGE: Literal[2107]
"""
Selection in sheet has been changed.

Arguments: XRange/XSheetCellRangeContainer aRange.
"""
WORKSHEET_FOLLOWHYPERLINK: Literal[2108]
"""
Hyperlink has been clicked.

Arguments: XCell aCell.
"""
USERDEFINED_START: Literal[1000000]
"""
Implementations are allowed to use identifiers above this value for any internal purpose.
"""

