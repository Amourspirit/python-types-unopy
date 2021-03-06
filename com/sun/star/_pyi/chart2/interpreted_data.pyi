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
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from .x_data_series import XDataSeries as XDataSeries_b8150b89
from .data.x_labeled_data_sequence import XLabeledDataSequence as XLabeledDataSequence_7e1a10c8


class InterpretedData(object):
    """
    Struct Class

    offers tooling to interpret different data sources in a structural and chart-type-dependent way.

    See Also:
        `API InterpretedData <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1InterpretedData.html>`_
    """
    typeName: Literal['com.sun.star.chart2.InterpretedData']

    def __init__(self, Series: typing.Optional[typing.Tuple[typing.Tuple[XDataSeries_b8150b89, ...], ...]] = ..., Categories: typing.Optional[XLabeledDataSequence_7e1a10c8] = ...) -> None:
        """
        Constructor

        Arguments:
            Series (typing.Tuple[typing.Tuple[XDataSeries, ...], ...], optional): Series value.
            Categories (XLabeledDataSequence, optional): Categories value.
        """
        ...


    @property
    def Series(self) -> typing.Tuple[typing.Tuple[XDataSeries_b8150b89, ...], ...]:
        ...


    @property
    def Categories(self) -> XLabeledDataSequence_7e1a10c8:
        ...


