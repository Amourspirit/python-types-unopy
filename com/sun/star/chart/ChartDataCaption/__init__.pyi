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

These values specify how the captions of data points are displayed.

**since**

    LibreOffice 7.1

See Also:
    `API ChartDataCaption <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart_1_1ChartDataCaption.html>`_
"""
NONE: Literal[0]
"""
No captions are displayed.
"""
VALUE: Literal[1]
"""
The caption contains the value of the data point in the number format of the axis that is attached to the respective data series.
"""
PERCENT: Literal[2]
"""
The caption contains the value of the data point in percent of all data points of one category.

That means, if a data point is the first one of a series, the percentage is calculated by using the first data points of all available series.
"""
TEXT: Literal[4]
"""
The caption contains the category name of the category to which a data point belongs.
"""
FORMAT: Literal[8]
"""
The number formatter is always used for displaying the value as value.

So this setting is deprecated.
"""
SYMBOL: Literal[16]
"""
The symbol of data column/row is additionally displayed in the caption.
"""
CUSTOM: Literal[32]
"""
The caption contains a custom text, which belongs to a data point label.

**since**

    LibreOffice 7.1
"""
DATA_SERIES: Literal[64]
"""
The name of the data series is additionally displayed in the caption.

**since**

    LibreOffice 7.2
"""

