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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart
# Libre Office Version: 7.2
from typing_extensions import Literal
from enum import Enum


class ChartAxisPosition(Enum):
    """
    Enum Class

    

    See Also:
        `API ChartAxisPosition <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#aa2815fba34da31acb139c7be75fda078>`_
    """
    END: Literal['END']
    """
    Cross the other axes at their maximum scale value.
    """
    START: Literal['START']
    """
    Cross the other axes at their minimum scale value.
    """
    VALUE: Literal['VALUE']
    """
    Cross the other axes at the value specified in the property CrossoverValue.
    """
    ZERO: Literal['ZERO']
    """
    Cross the other axes at zero.
    
    If zero is not contained in the current scale the value is used which is nearest to zero.
    """

__all__ = ['ChartAxisPosition']

