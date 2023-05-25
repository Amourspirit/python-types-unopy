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
# Namespace: com.sun.star.chart
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa


class X3DDisplay(XInterface_8f010a43):
    """
    gives access to 3D elements of a three-dimensional chart.

    See Also:
        `API X3DDisplay <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart_1_1X3DDisplay.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.chart.X3DDisplay'

    def getFloor(self) -> XPropertySet_bc180bfa:
        """
        This is only valid for three-dimensional diagrams.
        """
        ...
    def getWall(self) -> XPropertySet_bc180bfa:
        """
        This specifies the properties of the two side walls of the chart scene.
        
        Note that this property is also valid for two-dimensional diagrams. There the properties returned here affect the background rectangle of the diagram.
        """
        ...



