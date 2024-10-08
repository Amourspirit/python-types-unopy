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


class ChartDataChangeTypeProto(Protocol):
    """Protocol for ChartDataChangeType"""

    @property
    def typeName(self) -> Literal["com.sun.star.chart.ChartDataChangeType"]:
        ...
    value: Any
    ALL: ChartDataChangeTypeProto
    COLUMN_DELETED: ChartDataChangeTypeProto
    COLUMN_INSERTED: ChartDataChangeTypeProto
    DATA_RANGE: ChartDataChangeTypeProto
    ROW_DELETED: ChartDataChangeTypeProto
    ROW_INSERTED: ChartDataChangeTypeProto

ALL: ChartDataChangeTypeProto
"""
Major changes were applied to the data.
"""
COLUMN_DELETED: ChartDataChangeTypeProto
"""
The column given in the ChartDataChangeEvent, was deleted.
"""
COLUMN_INSERTED: ChartDataChangeTypeProto
"""
The column given in the ChartDataChangeEvent, was inserted.
"""
DATA_RANGE: ChartDataChangeTypeProto
"""
The range of columns and rows, given in the ChartDataChangeEvent, has changed.
"""
ROW_DELETED: ChartDataChangeTypeProto
"""
The row given in the ChartDataChangeEvent, was deleted.
"""
ROW_INSERTED: ChartDataChangeTypeProto
"""
The row given in the ChartDataChangeEvent, was inserted.
"""

