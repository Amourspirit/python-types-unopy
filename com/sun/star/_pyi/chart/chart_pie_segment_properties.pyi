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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.chart
from .chart_data_point_properties import ChartDataPointProperties as ChartDataPointProperties_677c10bd

class ChartPieSegmentProperties(ChartDataPointProperties_677c10bd):
    """
    Service Class

    specifies all the properties for the graphic object of a pie segment.

    See Also:
        `API ChartPieSegmentProperties <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1ChartPieSegmentProperties.html>`_
    """
    @property
    def SegmentOffset(self) -> int:
        """
        reflects the offset of a pie segment in percent of the radius.
        
        The default value for all the segments of a PieDiagram is 0. If you change this value from 0 to 100 the segment is pulled out from the center by its radius.
        
        Currently this property is supported by two dimensional pie diagrams only.
        """
        ...


