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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.chart2
# Libre Office Version: 2024.2
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class CurveStyleProto(Protocol):
    """Protocol for CurveStyle"""

    @property
    def typeName(self) -> Literal["com.sun.star.chart2.CurveStyle"]:
        ...
    value: Any
    B_SPLINES: CurveStyleProto
    CUBIC_SPLINES: CurveStyleProto
    LINES: CurveStyleProto
    NURBS: CurveStyleProto
    STEP_CENTER_X: CurveStyleProto
    STEP_CENTER_Y: CurveStyleProto
    STEP_END: CurveStyleProto
    STEP_START: CurveStyleProto

B_SPLINES: CurveStyleProto
"""
Data points are connected via a parametric, interpolating B-spline curve.
"""
CUBIC_SPLINES: CurveStyleProto
"""
Data points are connected via a smoothed cubic spline curve.

The data points themselves are part of to the curve.
"""
LINES: CurveStyleProto
"""
Lines between data points are not smoothed.
"""
NURBS: CurveStyleProto
"""
Non-uniform rational b-splines.
"""
STEP_CENTER_X: CurveStyleProto
"""
Data points are connected via a 3-segmented stepped line.

The lines is horizontal till the center of the X values.
"""
STEP_CENTER_Y: CurveStyleProto
"""
Data points are connected via a 3-segmented stepped line.

The lines is horizontal at the center of the Y values.
"""
STEP_END: CurveStyleProto
"""
Data points are connected via a 2-segmented stepped line.

The line ends horizontally.
"""
STEP_START: CurveStyleProto
"""
Data points are connected via a 2-segmented stepped line.

The line starts horizontally.
"""

