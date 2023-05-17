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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from com.sun.star._pyi.chart.chart_data_change_type import ChartDataChangeType as PyiChartDataChangeType
"""
Enum


See Also:
    `API ChartDataChangeType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart.html#a37b4d47e7d1600aa406ad115a39fe1da>`_
"""
typeName: str = 'com.sun.star.chart.ChartDataChangeType'

ALL: PyiChartDataChangeType = ...
"""
Major changes were applied to the data.
"""
COLUMN_DELETED: PyiChartDataChangeType = ...
"""
The column given in the ChartDataChangeEvent, was deleted.
"""
COLUMN_INSERTED: PyiChartDataChangeType = ...
"""
The column given in the ChartDataChangeEvent, was inserted.
"""
DATA_RANGE: PyiChartDataChangeType = ...
"""
The range of columns and rows, given in the ChartDataChangeEvent, has changed.
"""
ROW_DELETED: PyiChartDataChangeType = ...
"""
The row given in the ChartDataChangeEvent, was deleted.
"""
ROW_INSERTED: PyiChartDataChangeType = ...
"""
The row given in the ChartDataChangeEvent, was inserted.
"""

