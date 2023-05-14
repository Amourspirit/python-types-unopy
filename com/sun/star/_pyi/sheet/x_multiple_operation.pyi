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
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .table_operation_mode import TableOperationMode as TableOperationMode_b970e3f
    from ..table.cell_address import CellAddress as CellAddress_ae5f0b56
    from ..table.cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43

class XMultipleOperation(XInterface_8f010a43):
    """
    provides a method to apply a Multiple Operations Table to the cell range.

    See Also:
        `API XMultipleOperation <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XMultipleOperation.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XMultipleOperation']

    def setTableOperation(self, aFormulaRange: 'CellRangeAddress_ec450d43', nMode: 'TableOperationMode_b970e3f', aColumnCell: 'CellAddress_ae5f0b56', aRowCell: 'CellAddress_ae5f0b56') -> None:
        """
        creates a table of formulas (a \"Multiple Operations Table\").
        
        The specified formulas are repeated, with references to the specified cells replaced by references to values in the first column and/or row of the range.
        """
        ...


