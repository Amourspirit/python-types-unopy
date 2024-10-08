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
# Namespace: com.sun.star.ui
# Libre Office Version: 2024.2
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class DockingAreaProto(Protocol):
    """Protocol for DockingArea"""

    @property
    def typeName(self) -> Literal["com.sun.star.ui.DockingArea"]:
        ...
    value: Any
    DOCKINGAREA_BOTTOM: DockingAreaProto
    DOCKINGAREA_DEFAULT: DockingAreaProto
    DOCKINGAREA_LEFT: DockingAreaProto
    DOCKINGAREA_RIGHT: DockingAreaProto
    DOCKINGAREA_TOP: DockingAreaProto

DOCKINGAREA_BOTTOM: DockingAreaProto
"""
the bottom docking area above the status bar.
"""
DOCKINGAREA_DEFAULT: DockingAreaProto
"""
a default docking area.

It depends on the implementation how to treat this value.
"""
DOCKINGAREA_LEFT: DockingAreaProto
"""
the left side docking area.
"""
DOCKINGAREA_RIGHT: DockingAreaProto
"""
the right side docking area.
"""
DOCKINGAREA_TOP: DockingAreaProto
"""
the top docking area below the menu bar.
"""

