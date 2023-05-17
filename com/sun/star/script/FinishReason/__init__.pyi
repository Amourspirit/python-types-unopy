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
import uno
from com.sun.star._pyi.script.finish_reason import FinishReason as PyiFinishReason
"""
Enum


See Also:
    `API FinishReason <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1script.html#a8ab52fac6ca48179fe55e9a6aa3a345d>`_
"""
typeName: str = 'com.sun.star.script.FinishReason'

Cancel: PyiFinishReason = ...
"""
script in the engine was cancelled.

script execution was cancelled.
"""
Error: PyiFinishReason = ...
"""
error occurred during script execution or compiling.
"""
OK: PyiFinishReason = ...
"""
script in the engine terminated normally.
"""

