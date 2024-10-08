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
# Namespace: com.sun.star.view
# Libre Office Version: 2024.2
from __future__ import annotations
from typing import Protocol, Any
from typing_extensions import Literal


class PrintableStateProto(Protocol):
    """Protocol for PrintableState"""

    @property
    def typeName(self) -> Literal["com.sun.star.view.PrintableState"]:
        ...
    value: Any
    JOB_ABORTED: PrintableStateProto
    JOB_COMPLETED: PrintableStateProto
    JOB_FAILED: PrintableStateProto
    JOB_SPOOLED: PrintableStateProto
    JOB_SPOOLING_FAILED: PrintableStateProto
    JOB_STARTED: PrintableStateProto

JOB_ABORTED: PrintableStateProto
"""
printing was aborted (e.g., by the user) while either printing or spooling.
"""
JOB_COMPLETED: PrintableStateProto
"""
printing (rendering the document) has finished, spooling has begun
"""
JOB_FAILED: PrintableStateProto
"""
printing ran into an error.
"""
JOB_SPOOLED: PrintableStateProto
"""
spooling has finished successfully.

This is the only state that can be considered as \"success\" for a print job.
"""
JOB_SPOOLING_FAILED: PrintableStateProto
"""
the document could be printed but not spooled.
"""
JOB_STARTED: PrintableStateProto
"""
printing (rendering the document) has begun
"""

