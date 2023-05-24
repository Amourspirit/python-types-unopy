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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.chart2
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_coordinate_system import XCoordinateSystem as XCoordinateSystem_7ff0e31


class XChartType(XInterface_8f010a43):
    """

    See Also:
        `API XChartType <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1XChartType.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.chart2.XChartType'

    def createCoordinateSystem(self, DimensionCount: int) -> XCoordinateSystem_7ff0e31:
        """
        Creates a coordinate systems that fits the chart-type with its current settings and for the given dimension.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getChartType(self) -> str:
        """
        A string representation of the chart type.
        
        This needs to be the service-name which can be used to create a chart type.
        """
        ...
    def getRoleOfSequenceForSeriesLabel(self) -> str:
        """
        Returns the role of the XLabeledDataSequence of which the label will be taken to identify the DataSeries in dialogs or the legend.
        """
        ...
    def getSupportedMandatoryRoles(self) -> typing.Tuple[str, ...]:
        """
        Returns a sequence of roles that are understood by this chart type.
        
        All roles must be listed in the order in which they are usually parsed. This ensures that gluing sequences together and splitting them up apart again results in the same structure as before.
        
        Note, that this does not involve optional roles, like error-bars.
        """
        ...
    def getSupportedOptionalRoles(self) -> typing.Tuple[str, ...]:
        """
        Returns a sequence of roles that are understood in addition to the mandatory roles (see XChartType.getSupportedMandatoryRoles()).
        
        An example for an optional role are error-bars.
        """
        ...
    def getSupportedPropertyRoles(self) -> typing.Tuple[str, ...]:
        """
        Returns a sequence with supported property mapping roles.
        
        An example for a property mapping role is FillColor.
        """
        ...


