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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class CurveStyle(Enum):
    """
    Enum

    

    See Also:
        `API CurveStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1chart2.html#a6eee32347565343ce84b84adb82da419>`_
    """
    typeName: str = 'com.sun.star.chart2.CurveStyle'

    B_SPLINES: 'uno.Enum'
    """
    Data points are connected via a parametric, interpolating B-spline curve.
    """
    CUBIC_SPLINES: 'uno.Enum'
    """
    Data points are connected via a smoothed cubic spline curve.
    
    The data points themselves are part of to the curve.
    """
    LINES: 'uno.Enum'
    """
    Lines between data points are not smoothed.
    """
    NURBS: 'uno.Enum'
    """
    Non-uniform rational b-splines.
    """
    STEP_CENTER_X: 'uno.Enum'
    """
    Data points are connected via a 3-segmented stepped line.
    
    The lines is horizontal till the center of the X values.
    """
    STEP_CENTER_Y: 'uno.Enum'
    """
    Data points are connected via a 3-segmented stepped line.
    
    The lines is horizontal at the center of the Y values.
    """
    STEP_END: 'uno.Enum'
    """
    Data points are connected via a 2-segmented stepped line.
    
    The line ends horizontally.
    """
    STEP_START: 'uno.Enum'
    """
    Data points are connected via a 2-segmented stepped line.
    
    The line starts horizontally.
    """

