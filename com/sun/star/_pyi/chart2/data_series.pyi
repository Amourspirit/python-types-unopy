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
# Libre Office Version: 7.2
# Namespace: com.sun.star.chart2
import typing
import uno
from .data_point_properties import DataPointProperties as DataPointProperties_24a00efd
from .x_data_series import XDataSeries as XDataSeries_b8150b89
from .x_regression_curve_container import XRegressionCurveContainer as XRegressionCurveContainer_8801116d
from .data.x_data_sink import XDataSink as XDataSink_dbc40c7b
from .data.x_data_source import XDataSource as XDataSource_f6340d57
if typing.TYPE_CHECKING:
    from .stacking_direction import StackingDirection as StackingDirection_8060e21

class DataSeries(DataPointProperties_24a00efd, XDataSeries_b8150b89, XRegressionCurveContainer_8801116d, XDataSink_dbc40c7b, XDataSource_f6340d57):
    """
    Service Class

    reflects the model data of the object that has all the information for a DataRenderer to create a visible data series in a chart.
    
    It combines one or more DataSequences which are interpreted by evaluating their role-string.
    
    **since**
    
        LibreOffice 7.0

    See Also:
        `API DataSeries <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1DataSeries.html>`_
    """
    @property
    def AttributedDataPoints(self) -> uno.ByteSequence:
        """
        This service will be used to render this data series.
        
        This service name can be used to determine which DataSeries are of the same type.
        
        The result of the DataSeries.DataSequenceRoles depends on the renderer service set here.
        
        a sequence of indexes denoting which data points have set properties that differ from the default.
        
        The default values are determined by the properties set at the DataPointProperties of the data series.
        
        If the sequence is empty, that means that all data points look alike. They are formatted using the property values set in the data series.
        
        The indexes in this sequence match the indexes used by the XIndexContainer.
        
        This property is especially useful for large data series with only some formatted data points, because you do not have to iterate over all elements.
        """
        ...
    @property
    def DeletedLegendEntries(self) -> uno.ByteSequence:
        """
        A sequence of indexes denoting which data points shouldn't be shown in the legend.
        
        **since**
        
            LibreOffice 7.0
        """
        ...
    @property
    def AttachedAxisIndex(self) -> int:
        """
        This property describes whether the series should be shown at the main value axis or at the secondary value axis.
        
        Having this property not set or setting it to 0 means that this data series will be scaled at the primary y-axis ( of the coordinate system in which this series is hosted ).
        
        Setting this property to 1 means that this series should be scaled at the secondary y-axis. If there is no secondary axis the main axis should be used for scaling instead.
        
        If you want to scale a series at a different x or z axis you need to create an additional coordinate system and host this series there.
        """
        ...
    @property
    def ShowCustomLeaderLines(self) -> bool:
        """
        This property describes whether the data point and the data label are connected with a leader line.
        
        **since**
        
            LibreOffice 7.1
        """
        ...
    @property
    def ShowLegendEntry(self) -> bool:
        """
        This property describes whether the legend entry for the the data series should be shown.
        
        **since**
        
            LibreOffice 6.3
        """
        ...
    @property
    def StackingDirection(self) -> 'StackingDirection_8060e21':
        """
        indicates whether this series should be stacked with respect to the previous series.
        """
        ...
    @property
    def VaryColorsByPoint(self) -> bool:
        """
        If TRUE, the data points of this series get different colors by default, like in a pie chart.
        """
        ...


