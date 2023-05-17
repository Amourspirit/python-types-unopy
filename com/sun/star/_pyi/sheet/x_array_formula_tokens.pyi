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
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from abc import ABC
if typing.TYPE_CHECKING:
    from .formula_token import FormulaToken as FormulaToken_bd1c0bf8


class XArrayFormulaTokens(ABC):
    """
    gives access to an array formula as token sequence.

    See Also:
        `API XArrayFormulaTokens <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XArrayFormulaTokens.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.sheet.XArrayFormulaTokens']

    def getArrayTokens(self) -> 'typing.Tuple[FormulaToken_bd1c0bf8, ...]':
        """
        returns the array formula as sequence of tokens.
        """
        ...
    def setArrayTokens(self, aTokens: 'typing.Tuple[FormulaToken_bd1c0bf8, ...]') -> None:
        """
        sets the array formula as sequence of tokens.
        """
        ...


