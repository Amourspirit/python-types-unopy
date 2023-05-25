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

import uno
from abc import ABC


class XExternalSheetCache(ABC):
    """
    Primary interface for the com.sun.star.sheet.ExternalSheetCache service.
    
    **since**
    
        OOo 3.1

    See Also:
        `API XExternalSheetCache <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XExternalSheetCache.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sheet.XExternalSheetCache'

    def getAllColumns(self, nRow: int) -> uno.ByteSequence:
        """
        Given a row number, this method returns a list of all columns numbers that store cached cell values in that row.
        
        The column numbers are sorted in ascending order.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getAllRows(self) -> uno.ByteSequence:
        """
        It returns a list of all row numbers where a cached cell or cells exist.
        
        The row numbers are sorted in ascending order.
        """
        ...
    def getCellValue(self, nColumn: int, nRow: int) -> typing.Any:
        """
        It retrieves a cached value from a specified cell position.
        
        The cached value can be either string or double.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def setCellValue(self, nColumn: int, nRow: int, aValue: typing.Any) -> None:
        """
        It sets a cached value for a specified cell position.
        
        The value is expected to be either of type string or of type double. No other data types are supported.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

    @property
    def TokenIndex(self) -> int:
        """
        Index corresponding to this instance of an external sheet cache for usage in formula tokens.
        
        This index to the external sheet cache is expected in the SingleReference.Sheet member if it is part of an external reference token.
        
        Each external sheet cache has a unique index value inside the ExternalDocLink instance.
        """
        ...
    @TokenIndex.setter
    def TokenIndex(self, value: int) -> None:
        ...


