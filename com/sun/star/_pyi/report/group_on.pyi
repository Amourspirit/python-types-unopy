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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.report
from typing_extensions import Literal


class GroupOn(object):
    """
    Const

    Specifies how to group data.

    See Also:
        `API GroupOn <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1report_1_1GroupOn.html>`_
    """
    DEFAULT: Literal[0]
    """
    The same value in the column value or expression.
    """
    PREFIX_CHARACTERS: Literal[1]
    """
    The same first nth of characters in the column value or expression.
    """
    YEAR: Literal[2]
    """
    Dates in the same calendar year.
    """
    QUARTAL: Literal[3]
    """
    Dates in the same calendar quarter.
    """
    MONTH: Literal[4]
    """
    Dates in the same month.
    """
    WEEK: Literal[5]
    """
    Dates in the same week.
    """
    DAY: Literal[6]
    """
    Dates on the same date.
    """
    HOUR: Literal[7]
    """
    Times in the same hour.
    """
    MINUTE: Literal[8]
    """
    Times in the same minute.
    """
    INTERVAL: Literal[9]
    """
    Values within an interval you specify.
    """

