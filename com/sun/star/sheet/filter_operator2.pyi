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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sheet
import typing


class FilterOperator2:
    """
    Const

    specifies the type of a single condition in a filter descriptor.
    
    This constants group extends the FilterOperator enum by additional filter operators.
    
    **since**
    
        OOo 3.2

    See Also:
        `API FilterOperator2 <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1FilterOperator2.html>`_
    """
    EMPTY: int = ...
    """
    selects empty entries.
    """
    NOT_EMPTY: int = ...
    """
    selects non-empty entries.
    """
    EQUAL: int = ...
    """
    value has to be equal to the specified value.
    """
    NOT_EQUAL: int = ...
    """
    value must not be equal to the specified value.
    """
    GREATER: int = ...
    """
    value has to be greater than the specified value.
    """
    GREATER_EQUAL: int = ...
    """
    value has to be greater than or equal to the specified value.
    """
    LESS: int = ...
    """
    value has to be less than the specified value.
    """
    LESS_EQUAL: int = ...
    """
    value has to be less than or equal to the specified value.
    """
    TOP_VALUES: int = ...
    """
    selects a specified number of entries with the greatest values.
    """
    TOP_PERCENT: int = ...
    """
    selects a specified percentage of entries with the greatest values.
    """
    BOTTOM_VALUES: int = ...
    """
    selects a specified number of entries with the lowest values.
    """
    BOTTOM_PERCENT: int = ...
    """
    selects a specified percentage of entries with the lowest values.
    """
    CONTAINS: int = ...
    """
    selects contains entries.
    """
    DOES_NOT_CONTAIN: int = ...
    """
    selects does-not-contain entries.
    """
    BEGINS_WITH: int = ...
    """
    selects begins-with entries.
    """
    DOES_NOT_BEGIN_WITH: int = ...
    """
    selects does-not-begin-with entries.
    """
    ENDS_WITH: int = ...
    """
    selects ends-with entries.
    """
    DOES_NOT_END_WITH: int = ...
    """
    selects does-not-end-with entries.
    """

