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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart
from typing_extensions import Literal
import typing
from .x_chart_data import XChartData as XChartData_a3580ade

class XChartDataArray(XChartData_a3580ade):
    """
    gives access to data represented as an array of rows.
    
    Can be obtained from interface XChartDocument via method getData().
    
    If used for an XYDiagram, the row number 0 represents the x-values.

    See Also:
        `API XChartDataArray <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart_1_1XChartDataArray.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.chart.XChartDataArray']

    def getColumnDescriptions(self) -> 'typing.Tuple[str, ...]':
        """
        retrieves the description texts for all columns.
        """
        ...
    def getData(self) -> 'typing.Tuple[typing.Tuple[float, ...], ...]':
        """
        retrieves the numerical data as a nested sequence of values.
        """
        ...
    def getRowDescriptions(self) -> 'typing.Tuple[str, ...]':
        """
        retrieves the description texts for all rows.
        """
        ...
    def setColumnDescriptions(self, aColumnDescriptions: 'typing.Tuple[str, ...]') -> None:
        """
        sets the description texts for all columns.
        """
        ...
    def setData(self, aData: 'typing.Tuple[typing.Tuple[float, ...], ...]') -> None:
        """
        sets the chart data as an array of numbers.
        """
        ...
    def setRowDescriptions(self, aRowDescriptions: 'typing.Tuple[str, ...]') -> None:
        """
        sets the description texts for all rows.
        """
        ...


