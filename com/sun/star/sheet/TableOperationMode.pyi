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
# Namespace: com.sun.star.sheet
# Libre Office Version: 2024.2
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class TableOperationModeProto(Protocol):
    """Protocol for TableOperationMode"""

    @property
    def typeName(self) -> Literal["com.sun.star.sheet.TableOperationMode"]:
        ...
    value: Any
    BOTH: TableOperationModeProto
    COLUMN: TableOperationModeProto
    ROW: TableOperationModeProto

BOTH: TableOperationModeProto
"""
is applied to rows and columns.

In this mode, the row and the column contain values. A formula using both row and column values is specified separately.
"""
COLUMN: TableOperationModeProto
"""
the field is used as a column field.

is applied to the columns.

In this mode, the column contains values and the row contains formulas.
"""
ROW: TableOperationModeProto
"""
the field is used as a row field.

is applied to the rows.

In this mode, the row contains values and the column contains formulas.
"""

