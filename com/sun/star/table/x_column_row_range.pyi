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
# Namespace: com.sun.star.table
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_table_columns import XTableColumns as XTableColumns_c66d0c31
    from .x_table_rows import XTableRows as XTableRows_a37e0afb


class XColumnRowRange(XInterface_8f010a43):
    """
    provides methods to access the collections of columns and rows of a cell range.

    See Also:
        `API XColumnRowRange <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1table_1_1XColumnRowRange.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.table.XColumnRowRange'

    def getColumns(self) -> XTableColumns_c66d0c31:
        """
        returns the collection of columns in the range.
        """
        ...
    def getRows(self) -> XTableRows_a37e0afb:
        """
        returns the collection of rows in the range.
        """
        ...


