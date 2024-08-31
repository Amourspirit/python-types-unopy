# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.chart
from __future__ import annotations
from .chart_axis_y_supplier import ChartAxisYSupplier as ChartAxisYSupplier_a9e0e4e
from .x_two_axis_y_supplier import XTwoAxisYSupplier as XTwoAxisYSupplier_fce40dee

class ChartTwoAxisYSupplier(ChartAxisYSupplier_a9e0e4e, XTwoAxisYSupplier_fce40dee):
    """
    Service Class

    a helper service for chart documents which supply primary and secondary y-axes.
    
    **since**
    
        OOo 3.0

    See Also:
        `API ChartTwoAxisYSupplier <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1ChartTwoAxisYSupplier.html>`_
    """
    @property
    def HasSecondaryYAxis(self) -> bool:
        """
        determines if the secondary y-axis is shown or hidden.
        """
        ...
    @HasSecondaryYAxis.setter
    def HasSecondaryYAxis(self, value: bool) -> None:
        ...
    @property
    def HasSecondaryYAxisDescription(self) -> bool:
        """
        determines for the secondary y-axis if the labels at the tick marks are shown or hidden.
        """
        ...
    @HasSecondaryYAxisDescription.setter
    def HasSecondaryYAxisDescription(self, value: bool) -> None:
        ...
    @property
    def HasSecondaryYAxisTitle(self) -> bool:
        """
        determines if the title of the secondary y-axis is shown or hidden.
        
        **since**
        
            OOo 3.0
        """
        ...
    @HasSecondaryYAxisTitle.setter
    def HasSecondaryYAxisTitle(self, value: bool) -> None:
        ...

