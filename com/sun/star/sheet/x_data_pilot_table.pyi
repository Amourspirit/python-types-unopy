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

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..table.cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43


class XDataPilotTable(XInterface_8f010a43):
    """
    provides methods to control a data pilot table which has already been created.

    See Also:
        `API XDataPilotTable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XDataPilotTable.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sheet.XDataPilotTable'

    def getOutputRange(self) -> CellRangeAddress_ec450d43:
        """
        returns the address of the cell range that contains the data pilot table.
        """
        ...
    def refresh(self) -> None:
        """
        recreates the data pilot table with current data from the source cell range.
        """
        ...


