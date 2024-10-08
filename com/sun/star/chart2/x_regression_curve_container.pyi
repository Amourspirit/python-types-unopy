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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.chart2
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_regression_curve import XRegressionCurve as XRegressionCurve_fa3c0dca


class XRegressionCurveContainer(XInterface_8f010a43):
    """

    See Also:
        `API XRegressionCurveContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1chart2_1_1XRegressionCurveContainer.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.chart2.XRegressionCurveContainer'

    def addRegressionCurve(self, aRegressionCurve: XRegressionCurve_fa3c0dca) -> None:
        """
        add a regression curve to the container

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getRegressionCurves(self) -> typing.Tuple[XRegressionCurve_fa3c0dca, ...]:
        """
        retrieve all regression curves
        """
        ...
    def removeRegressionCurve(self, aRegressionCurve: XRegressionCurve_fa3c0dca) -> None:
        """
        removes one regression curve from the container.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    def setRegressionCurves(self, aRegressionCurves: typing.Tuple[XRegressionCurve_fa3c0dca, ...]) -> None:
        """
        set all regression curves

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...


