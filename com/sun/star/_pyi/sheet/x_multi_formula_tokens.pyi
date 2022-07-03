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
from abc import ABC
if typing.TYPE_CHECKING:
    from .formula_token import FormulaToken as FormulaToken_bd1c0bf8

class XMultiFormulaTokens(ABC):
    """
    gives access to multiple sets of formula tokens.
    
    A service implementing this interface can internally set an arbitrary number of formula token sequences. The number of allowed formula token sequences must be returned by the com.sun.star.sheet.XMultiFormulaTokens.getCount() method. When the client code tries to access formula tokens at index that is outside the allowed index range, the implementation shall return an com.sun.star.lang.IndexOutOfBoundsException.

    See Also:
        `API XMultiFormulaTokens <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XMultiFormulaTokens.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XMultiFormulaTokens']

    def getCount(self) -> int:
        """
        returns the number of formulas allowed in this formula token set.
        """
        ...
    def getTokens(self, nIndex: int) -> 'typing.Tuple[FormulaToken_bd1c0bf8, ...]':
        """
        returns the formula at specified index as sequence of tokens.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def setTokens(self, nIndex: int, aTokens: 'typing.Tuple[FormulaToken_bd1c0bf8, ...]') -> None:
        """
        sets the formula at specified index as sequence of tokens.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...


