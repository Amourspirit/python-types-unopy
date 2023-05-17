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
# Namespace: com.sun.star.chart
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
"""
Const


**since**

    OOo 3.4

See Also:
    `API ChartAxisType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart_1_1ChartAxisType.html>`_
"""
AUTOMATIC: Literal[0]
"""
the type of the axis is chosen automatically dependent on the chart type, the dimension and the underlying data
"""
CATEGORY: Literal[1]
"""
the axis represent discrete category texts if chart type and the dimension allows
"""
DATE: Literal[2]
"""
the axis shows dates if the given data and chart type and the dimension allows
"""

