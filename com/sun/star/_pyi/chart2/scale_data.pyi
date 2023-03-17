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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing
from ..chart.time_increment import TimeIncrement as TimeIncrement_c7e70c4e
from .axis_orientation import AxisOrientation as AxisOrientation_ecba0d6d
from .increment_data import IncrementData as IncrementData_d2000c6b
from .x_scaling import XScaling as XScaling_97500a65
from .data.x_labeled_data_sequence import XLabeledDataSequence as XLabeledDataSequence_7e1a10c8


class ScaleData(object):
    """
    Struct Class


    See Also:
        `API ScaleData <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1ScaleData.html>`_
    """
    typeName: Literal['com.sun.star.chart2.ScaleData']

    def __init__(self, Minimum: typing.Optional[object] = ..., Maximum: typing.Optional[object] = ..., Origin: typing.Optional[object] = ..., Orientation: typing.Optional[AxisOrientation_ecba0d6d] = ..., Scaling: typing.Optional[XScaling_97500a65] = ..., Categories: typing.Optional[XLabeledDataSequence_7e1a10c8] = ..., AxisType: typing.Optional[int] = ..., AutoDateAxis: typing.Optional[bool] = ..., ShiftedCategoryPosition: typing.Optional[bool] = ..., IncrementData: typing.Optional[IncrementData_d2000c6b] = ..., TimeIncrement: typing.Optional[TimeIncrement_c7e70c4e] = ...) -> None:
        """
        Constructor

        Arguments:
            Minimum (object, optional): Minimum value.
            Maximum (object, optional): Maximum value.
            Origin (object, optional): Origin value.
            Orientation (AxisOrientation, optional): Orientation value.
            Scaling (XScaling, optional): Scaling value.
            Categories (XLabeledDataSequence, optional): Categories value.
            AxisType (int, optional): AxisType value.
            AutoDateAxis (bool, optional): AutoDateAxis value.
            ShiftedCategoryPosition (bool, optional): ShiftedCategoryPosition value.
            IncrementData (IncrementData, optional): IncrementData value.
            TimeIncrement (TimeIncrement, optional): TimeIncrement value.
        """
        ...


    @property
    def Minimum(self) -> object:
        """
        if the any contains a double value this is used as a fixed maximum.
        
        Otherwise, if the any is empty or contains an incompatible type, the maximum is automatic.
        
        If the maximum is automatic, this means, each view that represents the model containing this scale, has to calculate a maximum by its own means.
        """
        ...


    @property
    def Maximum(self) -> object:
        """
        if the any contains a double value this is used as a fixed minimum.
        
        Otherwise, if the any is empty or contains an incompatible type, the minimum is automatic.
        
        If the minimum is automatic, this means, each view that represents the model containing this scale, has to calculate a minimum by its own means.
        """
        ...


    @property
    def Origin(self) -> object:
        """
        The Origin indicates where other axes cross this axis.
        
        If the any contains a double value that value is used. Otherwise an appropriate value has to be calculated by that instances using Origin.
        """
        ...


    @property
    def Orientation(self) -> AxisOrientation_ecba0d6d:
        """
        Axis orientation (standard or reversed).
        
        If used at the Y axis in pie charts or doughnut charts, specifies the rotation direction of the pie. The value AxisOrientation.MATHEMATICAL rotates the pie counterclockwise, the value AxisOrientation.REVERSE rotates the pie clockwise.
        
        Note: Is this a good place for the axis orientation? Two axes may use the same scale, but point into two different directions.
        """
        ...


    @property
    def Scaling(self) -> XScaling_97500a65:
        ...


    @property
    def Categories(self) -> XLabeledDataSequence_7e1a10c8:
        ...


    @property
    def AxisType(self) -> int:
        """
        describes the type of the axis.
        
        It can be a real number axis or a category axis or something else. AxisType is one value out of the constant group AxisType.
        """
        ...


    @property
    def AutoDateAxis(self) -> bool:
        """
        if true an AxisType CATEGORY is interpreted as DATE if the underlying data given in Categories are dates
        """
        ...


    @property
    def ShiftedCategoryPosition(self) -> bool:
        """
        describes whether data points on category or date axis are placed between tickmarks or not if true the maximum on the scale will be expanded for one interval
        """
        ...


    @property
    def IncrementData(self) -> IncrementData_d2000c6b:
        """
        increment data to be used for not date-time axis
        """
        ...


    @property
    def TimeIncrement(self) -> TimeIncrement_c7e70c4e:
        """
        increment data to be used in case of date-time axis
        """
        ...


