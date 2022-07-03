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
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing
from .chart_data_value import ChartDataValue as ChartDataValue_d3310c83


class ChartDataRow(object):
    """
    Struct Class

    describes a single data row, specified by its name and a sequence of data points.
    
    This struct is currently used nowhere.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API ChartDataRow <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart_1_1ChartDataRow.html>`_
    """
    typeName: Literal['com.sun.star.chart.ChartDataRow']

    def __init__(self, Points: typing.Optional[typing.Tuple[typing.Tuple[ChartDataValue_d3310c83, ...], ...]] = ..., Name: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Points (typing.Tuple[typing.Tuple[ChartDataValue, ...], ...], optional): Points value.
            Name (str, optional): Name value.
        """
        ...


    @property
    def Points(self) -> typing.Tuple[typing.Tuple[ChartDataValue_d3310c83, ...], ...]:
        """
        The points contained in this data row.
        """
        ...


    @property
    def Name(self) -> str:
        """
        The name of the data row.
        """
        ...


