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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sheet
from __future__ import annotations
from .spreadsheet_document_settings import SpreadsheetDocumentSettings as SpreadsheetDocumentSettings_a1641229
from .x_function_access import XFunctionAccess as XFunctionAccess_e2000d11

class FunctionAccess(SpreadsheetDocumentSettings_a1641229, XFunctionAccess_e2000d11):
    """
    Service Class

    allows generic access to all spreadsheet functions.
    
    **since**
    
        OOo 3.3

    See Also:
        `API FunctionAccess <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sheet_1_1FunctionAccess.html>`_
    """
    @property
    def IsArrayFunction(self) -> bool:
        """
        specifies whether the function call is performed as array function call.
        
        If set to TRUE, the result of the function call will be calculated similar to array formulas in a spreadsheet document. The return value of the function call will usually be a sequence of sequences containing the values of the resulting array. Example: If the function ABS is called for a 3x2 cell range, the result will be a 3x2 array containing the absolute values of the numbers contained in the specified cell range.
        
        If set to FALSE, the result of the function call will be calculated similar to simple cell formulas in a spreadsheet document. The return value of the function call will usually be a single value. Of course, some functions always return an array, for example the MUNIT function.
        
        For compatibility with older versions, the default value of this property is TRUE.
        
        **since**
        
            OOo 3.3
        """
        ...
    @IsArrayFunction.setter
    def IsArrayFunction(self, value: bool) -> None:
        ...

