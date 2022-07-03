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
# Libre Office Version: 7.3
# Namespace: com.sun.star.sheet
from typing_extensions import Literal
import typing
from .x_spreadsheets import XSpreadsheets as XSpreadsheets_c8f50c64
if typing.TYPE_CHECKING:
    from .x_spreadsheet_document import XSpreadsheetDocument as XSpreadsheetDocument_2a1f0f30

class XSpreadsheets2(XSpreadsheets_c8f50c64):
    """
    extends XSpreadsheets interface to import external sheets.
    
    **since**
    
        LibreOffice 3.5

    See Also:
        `API XSpreadsheets2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSpreadsheets2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XSpreadsheets2']

    def importSheet(self, srcDoc: 'XSpreadsheetDocument_2a1f0f30', srcName: str, nDestPosition: int) -> int:
        """
        copies a sheet from a source document.
        
        **since**
        
            LibreOffice 3.5

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...


