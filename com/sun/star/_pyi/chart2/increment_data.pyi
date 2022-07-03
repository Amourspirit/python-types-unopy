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
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing
from .sub_increment import SubIncrement as SubIncrement_c5630c1b


class IncrementData(object):
    """
    Struct Class

    An IncrementData describes how tickmarks are positioned on the scale of an axis.

    See Also:
        `API IncrementData <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1IncrementData.html>`_
    """
    typeName: Literal['com.sun.star.chart2.IncrementData']

    def __init__(self, SubIncrements: typing.Optional[typing.Tuple[SubIncrement_c5630c1b, ...]] = ..., Distance: typing.Optional[object] = ..., PostEquidistant: typing.Optional[object] = ..., BaseValue: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            SubIncrements (typing.Tuple[SubIncrement, ...], optional): SubIncrements value.
            Distance (object, optional): Distance value.
            PostEquidistant (object, optional): PostEquidistant value.
            BaseValue (object, optional): BaseValue value.
        """
        ...


    @property
    def SubIncrements(self) -> typing.Tuple[SubIncrement_c5630c1b, ...]:
        """
        SubIncrements describes the positioning of further sub tickmarks on the scale of an axis.
        
        The first SubIncrement in this sequence determines how the distance between two neighboring main tickmarks is divided for positioning of further sub tickmarks. Every following SubIncrement determines the positions of subsequent tickmarks in relation to their parent tickmarks given by the preceding SubIncrement.
        """
        ...


    @property
    def Distance(self) -> object:
        """
        if the any contains a double value this is used as a fixed Distance value.
        
        Otherwise, if the any is empty or contains an incompatible type, the Distance is meant to be calculated automatically by the view component representing the model containing this increment.
        """
        ...


    @property
    def PostEquidistant(self) -> object:
        """
        PostEquidistant rules whether the member Distance describes a distance before or after the scaling is applied.
        
        If PostEquidistant equals TRUE Distance is given in values after XScaling is applied, thus resulting main tickmarks will always look equidistant on the screen. If PostEquidistant equals FALSE Distance is given in values before XScaling is applied.
        """
        ...


    @property
    def BaseValue(self) -> object:
        """
        if the any contains a double value this is used as a fixed BaseValue.
        
        Otherwise, if the any is empty or contains an incompatible type, the BaseValue is meant to be calculated automatically by the view component representing the model containing this increment.
        """
        ...


