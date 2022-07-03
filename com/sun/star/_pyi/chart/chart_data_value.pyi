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
# Namespace: com.sun.star.chart
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class ChartDataValue(object):
    """
    Struct Class

    describes a single data value, including the error
    
    This struct is currently used nowhere.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API ChartDataValue <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart_1_1ChartDataValue.html>`_
    """
    typeName: Literal['com.sun.star.chart.ChartDataValue']

    def __init__(self, Value: typing.Optional[float] = ..., HighError: typing.Optional[float] = ..., LowError: typing.Optional[float] = ...) -> None:
        """
        Constructor

        Arguments:
            Value (float, optional): Value value.
            HighError (float, optional): HighError value.
            LowError (float, optional): LowError value.
        """
        ...


    @property
    def Value(self) -> float:
        """
        value by itself.
        """
        ...


    @property
    def HighError(self) -> float:
        """
        highest possible error value.
        """
        ...


    @property
    def LowError(self) -> float:
        """
        lowest possible error value.
        """
        ...


