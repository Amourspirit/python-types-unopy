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
# Namespace: com.sun.star.chart
# Libre Office Version: 2024.2
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class ChartLegendExpansionProto(Protocol):
    """Protocol for ChartLegendExpansion"""

    @property
    def typeName(self) -> Literal["com.sun.star.chart.ChartLegendExpansion"]:
        ...
    value: Any
    BALANCED: ChartLegendExpansionProto
    CUSTOM: ChartLegendExpansionProto
    HIGH: ChartLegendExpansionProto
    WIDE: ChartLegendExpansionProto

BALANCED: ChartLegendExpansionProto
"""
The legend entries are arranged in a way that the aspect ratio of the resulting legend is as near to 1 as possible.
"""
CUSTOM: ChartLegendExpansionProto
"""
The size of the legend is given explicitly.
"""
HIGH: ChartLegendExpansionProto
"""
The legend entries are stacked in a single column if possible.

If not enough space is available further columns are added.

This is usually used for legends that are displayed on the left or right hand side of the page.
"""
WIDE: ChartLegendExpansionProto
"""
The legend entries are arranged in a single row if possible.

If not enough space is available further rows are added.

This is usually used for legends that are displayed at the top or bottom of the page.
"""

