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
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing

from abc import ABC
if typing.TYPE_CHECKING:
    from .formula_op_code_map_entry import FormulaOpCodeMapEntry as FormulaOpCodeMapEntry_37da0f61
    from .formula_token import FormulaToken as FormulaToken_bd1c0bf8


class XFormulaOpCodeMapper(ABC):
    """
    gives access to spreadsheet compiler token interns.

    See Also:
        `API XFormulaOpCodeMapper <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XFormulaOpCodeMapper.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sheet.XFormulaOpCodeMapper'

    def getAvailableMappings(self, Language: int, Groups: int) -> typing.Tuple[FormulaOpCodeMapEntry_37da0f61, ...]:
        """
        returns a sequence of map entries for all available elements of a given formula language.
        
        Each element of the formula language in parameter Language is mapped to a FormulaToken containing the internal OpCode used by the spreadsheet application in FormulaToken.OpCode and by contract maybe additional information in FormulaToken.Data. See getMappings() for more details.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getMappings(self, Names: typing.Tuple[str, ...], Language: int) -> typing.Tuple[FormulaToken_bd1c0bf8, ...]:
        """
        returns a sequence of tokens matching the input sequence of strings in order.
        
        Each string element in parameter Names according to the formula language in parameter Language is mapped to a FormulaToken containing the internal OpCode used by the spreadsheet application in FormulaToken.OpCode and by contract maybe additional information in FormulaToken.Data.
        
        The order of the FormulaToken sequence returned matches the input order of the string sequence.
        
        An unknown Name string gets the OpCode value of OpCodeUnknown assigned.
        
        Additional information in FormulaToken.Data is returned for:

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

    @property
    def OpCodeExternal(self) -> int:
        """
        OpCode value used for external Add-In functions.
        
        Needed to be able to identify which of the function names map to an Add-In implementation where this OpCode is used in the returned mapping and the programmatic name is available as additional information.
        """
        ...
    @OpCodeExternal.setter
    def OpCodeExternal(self, value: int) -> None:
        ...
    @property
    def OpCodeUnknown(self) -> int:
        """
        OpCode value used for unknown functions.
        
        Used to identify which of the function names queried with getMappings() are unknown to the implementation.
        """
        ...
    @OpCodeUnknown.setter
    def OpCodeUnknown(self, value: int) -> None:
        ...

