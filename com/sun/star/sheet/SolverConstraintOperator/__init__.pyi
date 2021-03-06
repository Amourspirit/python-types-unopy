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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
"""
Enum



See Also:
    `API SolverConstraintOperator <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#a491ab8ed5b7b5809e7be869d26b071cf>`_
"""
typeName: str = 'com.sun.star.sheet.SolverConstraintOperator'

BINARY: 'uno.Enum'
"""
The cell value is a binary value (0 or 1).
"""
EQUAL: 'uno.Enum'
"""
value has to be equal to the specified value.

The cell value is equal to the specified value.
"""
GREATER_EQUAL: 'uno.Enum'
"""
the value has to be greater than or equal to the specified value.

The cell value is greater or equal to the specified value.

value has to be greater than or equal to the specified value.
"""
INTEGER: 'uno.Enum'
"""
The cell value is an integer value.
"""
LESS_EQUAL: 'uno.Enum'
"""
the value has to be less than or equal to the specified value.

The cell value is less or equal to the specified value.

value has to be less than or equal to the specified value.
"""

