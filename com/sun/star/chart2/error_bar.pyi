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
from .data.x_data_sink import XDataSink as XDataSink_dbc40c7b
from .data.x_data_source import XDataSource as XDataSource_f6340d57
from ..drawing.line_properties import LineProperties as LineProperties_f13f0da9

class ErrorBar(LineProperties_f13f0da9, XDataSink_dbc40c7b, XDataSource_f6340d57):
    """
    Service Class


    See Also:
        `API ErrorBar <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart2_1_1ErrorBar.html>`_
    """
    @property
    def ErrorBarStyle(self) -> int:
        """
        """
        ...
    @ErrorBarStyle.setter
    def ErrorBarStyle(self, value: int) -> None:
        ...
    @property
    def NegativeError(self) -> float:
        """
        """
        ...
    @NegativeError.setter
    def NegativeError(self, value: float) -> None:
        ...
    @property
    def PositiveError(self) -> float:
        """
        """
        ...
    @PositiveError.setter
    def PositiveError(self, value: float) -> None:
        ...
    @property
    def ShowNegativeError(self) -> bool:
        """
        """
        ...
    @ShowNegativeError.setter
    def ShowNegativeError(self, value: bool) -> None:
        ...
    @property
    def ShowPositiveError(self) -> bool:
        """
        """
        ...
    @ShowPositiveError.setter
    def ShowPositiveError(self, value: bool) -> None:
        ...
    @property
    def Weight(self) -> float:
        """
        The weight for the standard deviation.
        """
        ...
    @Weight.setter
    def Weight(self, value: float) -> None:
        ...
