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


class SheetLinkModeProto(Protocol):
    """Protocol for SheetLinkMode"""

    @property
    def typeName(self) -> Literal["com.sun.star.sheet.SheetLinkMode"]:
        ...
    value: Any
    NONE: SheetLinkModeProto
    NORMAL: SheetLinkModeProto
    VALUE: SheetLinkModeProto

NONE: SheetLinkModeProto
"""
no cells are moved.

sheet is not linked.

new values are used without changes.

nothing is calculated.

nothing is imported.

no condition is specified.
"""
NORMAL: SheetLinkModeProto
"""
all contents (values and formulas) are copied.
"""
VALUE: SheetLinkModeProto
"""
instead of using formulas, the result values are copied.
"""

