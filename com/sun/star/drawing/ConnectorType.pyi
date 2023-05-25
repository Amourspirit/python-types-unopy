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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.4
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class ConnectorTypeProto(Protocol):
    """Protocol for ConnectorType"""

    @property
    def typeName(self) -> Literal["com.sun.star.drawing.ConnectorType"]:
        ...
    value: Any
    CURVE: ConnectorTypeProto
    LINE: ConnectorTypeProto
    LINES: ConnectorTypeProto
    STANDARD: ConnectorTypeProto

CURVE: ConnectorTypeProto
"""
the ConnectorShape is drawn as a curve
"""
LINE: ConnectorTypeProto
"""
the ConnectorShape is drawn as a straight line

This is the PolygonKind for a LineShape.
"""
LINES: ConnectorTypeProto
"""
the connector is drawn with three lines
"""
STANDARD: ConnectorTypeProto
"""
the graphic is rendered in the default color style of the output device,

use the length measurement.

the connector is drawn with three lines, with the middle line perpendicular to the other two
"""

