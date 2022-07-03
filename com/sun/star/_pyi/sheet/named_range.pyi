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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
from .x_cell_range_referrer import XCellRangeReferrer as XCellRangeReferrer_91c0e23
from .x_named_range import XNamedRange as XNamedRange_af450b4b

class NamedRange(XCellRangeReferrer_91c0e23, XNamedRange_af450b4b):
    """
    Service Class

    represents a named range in a spreadsheet document.
    
    In fact a named range is a named formula expression. A cell range address is one possible content of a named range.
    
    **since**
    
        OOo 3.0

    See Also:
        `API NamedRange <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1NamedRange.html>`_
    """
    @property
    def IsSharedFormula(self) -> bool:
        """
        Determines if this defined name represents a shared formula.
        
        This special property shall not be used externally. It is used by import and export filters for compatibility with spreadsheet documents containing shared formulas. Shared formulas are shared by several cells to save memory and to decrease file size.
        
        A defined name with this property set will not appear in the user interface of Calc, and its name will not appear in cell formulas. A formula referring to this defined name will show the formula definition contained in the name instead.
        
        **since**
        
            OOo 3.0
        """
        ...
    @property
    def TokenIndex(self) -> int:
        """
        returns the index used to refer to this name in token arrays.
        
        A token describing a defined name shall contain the op-code obtained from the FormulaMapGroupSpecialOffset.NAME offset and this index as data part.
        
        **since**
        
            OOo 3.0
        """
        ...


