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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart2
from __future__ import annotations
import typing
from .chart_type import ChartType as ChartType_a2640ae0
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class CandleStickChartType(ChartType_a2640ae0):
    """
    Service Class

    chart type service for candlestick charts.

    See Also:
        `API CandleStickChartType <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1CandleStickChartType.html>`_
    """
    @property
    def BlackDay(self) -> XPropertySet_bc180bfa:
        """
        If the candlestick chart shows Japanese candlesticks, that is the property Japanese is TRUE, the property set given here contains the formatting attributes of the black boxes, i.e.
        
        the boxes shown for falling values.
        
        The com.sun.star.beans.XPropertySet given here must support the services com.sun.star.drawing.FillProperties and com.sun.star.drawing.LineProperties.
        """
        ...
    @BlackDay.setter
    def BlackDay(self, value: XPropertySet_bc180bfa) -> None:
        ...
    @property
    def Japanese(self) -> bool:
        """
        If this property is TRUE, the candlesticks are shown as Japanese candlesticks.
        
        This implies that the property ShowFirst is also TRUE.
        
        Japanese candlesticks show the first and last value as boxes. A rising course (i.e. if the last value is greater than the first one) is shown by a white box. A falling course is shown by a black box.
        
        Default is FALSE.
        """
        ...
    @Japanese.setter
    def Japanese(self, value: bool) -> None:
        ...
    @property
    def ShowFirst(self) -> bool:
        """
        If this property is TRUE, the first value (which would be the opening course in a stock chart) is shown in the chart.
        
        This also makes the role \"values-first\" mandatory.
        
        This property is only evaluated for non-Japanese candlestick charts, as Japanese candlesticks always require to show the first value.
        
        Default is FALSE.
        """
        ...
    @ShowFirst.setter
    def ShowFirst(self, value: bool) -> None:
        ...
    @property
    def ShowHighLow(self) -> bool:
        """
        If this property is TRUE, the low and high values are shown in the chart.
        
        This also makes the roles \"values-min\" and \"values-max\" mandatory.
        
        Default is TRUE.
        """
        ...
    @ShowHighLow.setter
    def ShowHighLow(self, value: bool) -> None:
        ...
    @property
    def WhiteDay(self) -> XPropertySet_bc180bfa:
        """
        If the candlestick chart shows Japanese candlesticks, that is the property Japanese is TRUE, the property set given here contains the formatting attributes of the white boxes, i.e.
        
        the boxes shown for rising values.
        
        The com.sun.star.beans.XPropertySet given here must support the services com.sun.star.drawing.FillProperties and com.sun.star.drawing.LineProperties.
        """
        ...
    @WhiteDay.setter
    def WhiteDay(self, value: XPropertySet_bc180bfa) -> None:
        ...

