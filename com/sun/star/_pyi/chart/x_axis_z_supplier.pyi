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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.chart
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
    from ..drawing.x_shape import XShape as XShape_8fd00a3d

class XAxisZSupplier(XInterface_8f010a43):
    """
    gives access to the z-axis of a chart.

    See Also:
        `API XAxisZSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart_1_1XAxisZSupplier.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.chart.XAxisZSupplier']

    def getZAxis(self) -> 'XPropertySet_bc180bfa':
        """
        The returned property set contains scaling properties as well as formatting properties.
        """
        ...
    def getZAxisTitle(self) -> 'XShape_8fd00a3d':
        """
        """
        ...
    def getZHelpGrid(self) -> 'XPropertySet_bc180bfa':
        """
        """
        ...
    def getZMainGrid(self) -> 'XPropertySet_bc180bfa':
        """
        """
        ...


