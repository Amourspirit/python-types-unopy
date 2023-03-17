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
# Libre Office Version: 7.4
# Namespace: com.sun.star.table
from typing_extensions import Literal
from .x_cell import XCell as XCell_70d408e8

class XMergeableCell(XCell_70d408e8):
    """
    provides methods to access information about a cell that is mergeable with other sells.

    See Also:
        `API XMergeableCell <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1table_1_1XMergeableCell.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.table.XMergeableCell']

    def getColumnSpan(self) -> int:
        """
        returns the number of rows this cell spans.
        """
        ...
    def getRowSpan(self) -> int:
        """
        returns the number of columns this cell spans.
        """
        ...
    def isMerged(self) -> bool:
        """
        returns TRUE if this cell is merged with another cell.
        """
        ...


