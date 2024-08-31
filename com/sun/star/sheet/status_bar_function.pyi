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


class StatusBarFunction:
    """
    Const

    used to specify the function used to calculate a result in the spreadsheet's status bar.

    See Also:
        `API StatusBarFunction <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1StatusBarFunction.html>`_
    """
    NONE: int = ...
    """
    nothing is calculated.
    """
    AVERAGE: int = ...
    """
    average of all numerical values is calculated.
    """
    COUNTNUMS: int = ...
    """
    all values, including non-numerical values, are counted.
    """
    COUNT: int = ...
    """
    numerical values are counted.
    """
    MAX: int = ...
    """
    maximum value of all numerical values is calculated.
    """
    MIN: int = ...
    """
    minimum value of all numerical values is calculated.
    """
    SUM: int = ...
    """
    sum of all numerical values is calculated.
    """

