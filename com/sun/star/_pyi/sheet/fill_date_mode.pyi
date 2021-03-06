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
from enum import Enum

class FillDateMode(Enum):
    """
    Enum

    

    See Also:
        `API FillDateMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#a2ea1aac24b8de3ac28ac5a6ec79a80ca>`_
    """
    typeName: str = 'com.sun.star.sheet.FillDateMode'

    FILL_DATE_DAY: 'uno.Enum'
    """
    for every new value a single day is added.
    """
    FILL_DATE_MONTH: 'uno.Enum'
    """
    for every new value one month is added (day keeps unchanged).
    """
    FILL_DATE_WEEKDAY: 'uno.Enum'
    """
    for every new value a single day is added, but Saturdays and Sundays are skipped.
    """
    FILL_DATE_YEAR: 'uno.Enum'
    """
    for every new value one year is added (day and month keep unchanged).
    """

