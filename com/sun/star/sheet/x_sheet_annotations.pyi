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

from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
if typing.TYPE_CHECKING:
    from ..table.cell_address import CellAddress as CellAddress_ae5f0b56


class XSheetAnnotations(XIndexAccess_f0910d6d):
    """
    provides methods to access cell annotations via index and to insert and remove annotations.

    See Also:
        `API XSheetAnnotations <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XSheetAnnotations.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sheet.XSheetAnnotations'

    def insertNew(self, aPosition: CellAddress_ae5f0b56, aText: str) -> None:
        """
        creates a new annotation.
        
        This method creates a new annotation object, attaches it to the specified cell and inserts it into the collection.
        """
        ...
    def removeByIndex(self, nIndex: int) -> None:
        """
        removes a cell annotation from the collection.
        
        This method removes the annotation from its cell and from the collection.
        """
        ...


