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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.text
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
"""
Const

this set of constants describes different modes for text grids

See Also:
    `API TextGridMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text_1_1TextGridMode.html>`_
"""
NONE: Literal[0]
"""
no text grid
"""
LINES: Literal[1]
"""
line positions will be determined by the grid
"""
LINES_AND_CHARS: Literal[2]
"""
character and line positions will be determined by the grid
"""

