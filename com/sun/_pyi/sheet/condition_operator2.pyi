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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
from typing_extensions import Literal


class ConditionOperator2:
    """
    Const Class

    is used to specify the type of XSheetCondition2.

    See Also:
        `API ConditionOperator2 <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1ConditionOperator2.html>`_
    """
    NONE: Literal[0]
    """
    no condition is specified.
    """
    EQUAL: Literal[1]
    """
    value has to be equal to the specified value.
    """
    NOT_EQUAL: Literal[2]
    """
    the value must not be equal to the specified value.
    """
    GREATER: Literal[3]
    """
    the value has to be greater than the specified value.
    """
    GREATER_EQUAL: Literal[4]
    """
    the value has to be greater than or equal to the specified value.
    """
    LESS: Literal[5]
    """
    the value has to be less than the specified value.
    """
    LESS_EQUAL: Literal[6]
    """
    the value has to be less than or equal to the specified value.
    """
    BETWEEN: Literal[7]
    """
    the value has to be between the two specified values.
    """
    NOT_BETWEEN: Literal[8]
    """
    the value has to be outside of the two specified values.
    """
    FORMULA: Literal[9]
    """
    the specified formula has to give a non-zero result.
    """
    DUPLICATE: Literal[10]
    """
    Conditionally format duplicate values.
    """
    NOT_DUPLICATE: Literal[11]
    """
    Conditionally format non-duplicate values.
    """

__all__ = ['ConditionOperator2']
