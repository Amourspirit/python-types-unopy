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
# Namespace: com.sun.star.script
# Libre Office Version: 7.4
from __future__ import annotations
from com.sun.star import UnoEnumProto

class InterruptReasonProto(UnoEnumProto):
    BreakPoint: UnoEnumProto
    Cancel: UnoEnumProto
    CompileError: UnoEnumProto
    RuntimeError: UnoEnumProto
    Step: UnoEnumProto
    StepOut: UnoEnumProto
    StepOver: UnoEnumProto
    StepStatement: UnoEnumProto

BreakPoint: InterruptReasonProto
"""
script stopped at a breakpoint.
"""
Cancel: InterruptReasonProto
"""
script in the engine was cancelled.

script execution was cancelled.
"""
CompileError: InterruptReasonProto
"""
script has invalid syntax.
"""
RuntimeError: InterruptReasonProto
"""
runtime error occurred during script execution.
"""
Step: InterruptReasonProto
"""
script stops because only one scripting engine command was executed.
"""
StepOut: InterruptReasonProto
"""
script stops because it leaves a function.
"""
StepOver: InterruptReasonProto
"""
script stops because one step was executed.
"""
StepStatement: InterruptReasonProto
"""
script stop because one step was executed.
"""

