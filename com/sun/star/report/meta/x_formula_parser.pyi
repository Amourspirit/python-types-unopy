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
# Namespace: com.sun.star.report.meta
from __future__ import annotations
import typing

from ...beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ...lang.x_component import XComponent as XComponent_98dc0ab5
from ...sheet.x_formula_parser import XFormulaParser as XFormulaParser_d54d0cbc
if typing.TYPE_CHECKING:
    from ...sheet.formula_op_code_map_entry import FormulaOpCodeMapEntry as FormulaOpCodeMapEntry_37da0f61
    from ...sheet.x_formula_op_code_mapper import XFormulaOpCodeMapper as XFormulaOpCodeMapper_27ff0eee


class XFormulaParser(XPropertySet_bc180bfa, XComponent_98dc0ab5, XFormulaParser_d54d0cbc):
    """
    identifies a XFormulaParser which allows to retrieve the meta data of all supported functions.

    See Also:
        `API XFormulaParser <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1report_1_1meta_1_1XFormulaParser.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.report.meta.XFormulaParser'

    @property
    def FormulaOpCodeMapper(self) -> XFormulaOpCodeMapper_27ff0eee:
        """
        return the mapper for op codes.
        """
        ...
    @FormulaOpCodeMapper.setter
    def FormulaOpCodeMapper(self, value: XFormulaOpCodeMapper_27ff0eee) -> None:
        ...
    @property
    def OpCodeMap(self) -> typing.Tuple[FormulaOpCodeMapEntry_37da0f61, ...]:
        """
        The complete mapping of Names to OpCodes.
        
        Names and symbols not defined here lead to a parser/print error.
        """
        ...
    @OpCodeMap.setter
    def OpCodeMap(self, value: typing.Tuple[FormulaOpCodeMapEntry_37da0f61, ...]) -> None:
        ...

