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
from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
if typing.TYPE_CHECKING:
    from .border import Border as Border_7b2c097f
    from ..table.cell_address import CellAddress as CellAddress_ae5f0b56
    from ..table.cell_range_address import CellRangeAddress as CellRangeAddress_ec450d43

class XNamedRanges(XNameAccess_e2ab0cf6):
    """
    provides access to the members in a collection of named ranges and to insert and remove them.

    See Also:
        `API XNamedRanges <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XNamedRanges.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XNamedRanges']

    def addNewByName(self, aName: str, aContent: str, aPosition: 'CellAddress_ae5f0b56', nType: int) -> None:
        """
        adds a new named range to the collection.
        
        A cell range address is one possible content of a named range.
        
        This parameter will be zero for any common named range.
        """
        ...
    def addNewFromTitles(self, aSource: 'CellRangeAddress_ec450d43', aBorder: 'Border_7b2c097f') -> None:
        """
        creates named cell ranges from titles in a cell range.
        
        The names for the named ranges are taken from title cells in the top or bottom row, or from the cells of the left or right column of the range (depending on the parameter aBorder. The named ranges refer to single columns or rows in the inner part of the original range, excluding the labels.
        
        Example: The source range is A1:B3. The named ranges shall be created using row titles. This requires Border.TOP for the second parameter. The method creates two named ranges. The name of the first is equal to the content of cell A1 and contains the range $Sheet.$A$2:$A$3 (excluding the title cell). The latter named range is named using cell B1 and contains the cell range address $Sheet.$B$2:$B$3.
        """
        ...
    def outputList(self, aOutputPosition: 'CellAddress_ae5f0b56') -> None:
        """
        writes a list of all named ranges into the document.
        
        The first column of the list contains the names. The second column contains the contents of the named ranges.
        """
        ...
    def removeByName(self, aName: str) -> None:
        """
        removes a named range from the collection.
        """
        ...


