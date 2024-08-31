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
# Namespace: com.sun.star.form
# Libre Office Version: 2024.2
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class NavigationBarModeProto(Protocol):
    """Protocol for NavigationBarMode"""

    @property
    def typeName(self) -> Literal["com.sun.star.form.NavigationBarMode"]:
        ...
    value: Any
    CURRENT: NavigationBarModeProto
    NONE: NavigationBarModeProto
    PARENT: NavigationBarModeProto

CURRENT: NavigationBarModeProto
"""
a navigation bar is provided and navigation will be performed on the current/active form.

pressing the TAB key from the last control moves the focus to the first control in the tab order of the same record.

This is the default and most often encountered mode.
"""
NONE: NavigationBarModeProto
"""
no navigation bar is provided and navigation on the current form is only possible with the keyboard (TAB/SHIFT TAB).

Note that when this mode is set, a simultaneous TabulatorCycle value of TabulatorCycle.CURRENT means that you cannot travel between records anymore.
"""
PARENT: NavigationBarModeProto
"""
a navigation bar is provided and navigation will be performed on the parent of the current/active form.

This option is usually used for forms containing a grid control only. In such a form, the control has its own navigation elements, so there is no need to use the navigation bar for the form, but rather for its parent.
"""

