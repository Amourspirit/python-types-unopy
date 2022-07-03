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
# Namespace: com.sun.star.chart
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class ChartErrorIndicatorType(Enum):
    """
    Enum

    

    See Also:
        `API ChartErrorIndicatorType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#a1391f7495aa3a95d4bc29dbf29a809ea>`_
    """
    typeName: str = 'com.sun.star.chart.ChartErrorIndicatorType'

    LOWER: 'uno.Enum'
    """
    displays only the lower value.
    """
    NONE: 'uno.Enum'
    """
    error indicators are not displayed.
    
    displays no regression curve.
    
    no chart legend is displayed.
    
    displays no error indicators.
    """
    TOP_AND_BOTTOM: 'uno.Enum'
    """
    displays both the upper and lower values.
    """
    UPPER: 'uno.Enum'
    """
    displays only the upper value.
    """

