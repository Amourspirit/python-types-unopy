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
# Namespace: com.sun.star.reflection
# Libre Office Version: 2024.2
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class ParamModeProto(Protocol):
    """Protocol for ParamMode"""

    @property
    def typeName(self) -> Literal["com.sun.star.reflection.ParamMode"]:
        ...
    value: Any
    IN: ParamModeProto
    INOUT: ParamModeProto
    OUT: ParamModeProto

IN: ParamModeProto
"""
parameter serves as pure input for a called method
"""
INOUT: ParamModeProto
"""
parameter serves as input as well as output; data can transferred in both directions
"""
OUT: ParamModeProto
"""
parameter serves as pure output for the callee (in addition to the return value)
"""

