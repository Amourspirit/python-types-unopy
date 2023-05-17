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
# Namespace: com.sun.star.text
# Libre Office Version: 7.4
from __future__ import annotations
import uno
from com.sun.star._pyi.text.writing_mode import WritingMode as PyiWritingMode
"""
Enum


See Also:
    `API WritingMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text.html#a46d11c2d08142ef2d32761c04d1aaa26>`_
"""
typeName: str = 'com.sun.star.text.WritingMode'

LR_TB: PyiWritingMode = ...
"""
text within lines is written left-to-right.

lines and blocks are placed top-to-bottom.

Typically, this is the writing mode for normal \"alphabetic\" text.
"""
RL_TB: PyiWritingMode = ...
"""
text within a line are written right-to-left.

Lines and blocks are placed top-to-bottom.

Typically, this writing mode is used in Arabic and Hebrew text.
"""
TB_RL: PyiWritingMode = ...
"""
text within a line is written top-to-bottom.

Lines and blocks are placed right-to-left.

Typically, this writing mode is used in Chinese and Japanese text.
"""

