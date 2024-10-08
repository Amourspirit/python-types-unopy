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
from .x_axis_z_supplier import XAxisZSupplier as XAxisZSupplier_d44c0cb5

class ChartAxisZSupplier(XAxisZSupplier_d44c0cb5):
    """
    Service Class

    A helper service for chart documents which supply a z-axis.

    See Also:
        `API ChartAxisZSupplier <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1chart_1_1ChartAxisZSupplier.html>`_
    """
    @property
    def HasZAxis(self) -> bool:
        """
        Determines if the z-axis is shown or hidden.
        """
        ...
    @HasZAxis.setter
    def HasZAxis(self, value: bool) -> None:
        ...
    @property
    def HasZAxisDescription(self) -> bool:
        """
        Determines if the description of the z-axis is shown or hidden.
        """
        ...
    @HasZAxisDescription.setter
    def HasZAxisDescription(self, value: bool) -> None:
        ...
    @property
    def HasZAxisGrid(self) -> bool:
        """
        Determines if the major grid of the z-axis is shown or hidden.
        """
        ...
    @HasZAxisGrid.setter
    def HasZAxisGrid(self, value: bool) -> None:
        ...
    @property
    def HasZAxisHelpGrid(self) -> bool:
        """
        Determines if the minor grid of the z-axis is shown or hidden.
        """
        ...
    @HasZAxisHelpGrid.setter
    def HasZAxisHelpGrid(self, value: bool) -> None:
        ...
    @property
    def HasZAxisTitle(self) -> bool:
        """
        Determines if the title of the z-axis is shown or hidden.
        """
        ...
    @HasZAxisTitle.setter
    def HasZAxisTitle(self, value: bool) -> None:
        ...

