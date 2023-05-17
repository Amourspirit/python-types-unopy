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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .chart_data_change_event import ChartDataChangeEvent as ChartDataChangeEvent_25480ece


class XChartDataChangeEventListener(XEventListener_c7230c4a):
    """
    makes it possible to receive events when chart data changes.

    See Also:
        `API XChartDataChangeEventListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart_1_1XChartDataChangeEventListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.chart.XChartDataChangeEventListener']

    def chartDataChanged(self, aEvent: 'ChartDataChangeEvent_25480ece') -> None:
        """
        is called whenever chart data changes in value or structure.
        
        This interface must be implemented by components that wish to get notified of changes in chart data. They can be registered at an XChartData component.
        """
        ...


