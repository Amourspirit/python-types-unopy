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
from typing import Protocol, Any
from typing_extensions import Literal


class TextContentAnchorTypeProto(Protocol):
    """Protocol for TextContentAnchorType"""

    @property
    def typeName(self) -> Literal["com.sun.star.text.TextContentAnchorType"]:
        ...
    value: Any
    AS_CHARACTER: TextContentAnchorTypeProto
    AT_CHARACTER: TextContentAnchorTypeProto
    AT_FRAME: TextContentAnchorTypeProto
    AT_PAGE: TextContentAnchorTypeProto
    AT_PARAGRAPH: TextContentAnchorTypeProto

AS_CHARACTER: TextContentAnchorTypeProto
"""
The object is anchored instead of a character.
"""
AT_CHARACTER: TextContentAnchorTypeProto
"""
The object is anchored to a character.
"""
AT_FRAME: TextContentAnchorTypeProto
"""
The object is anchored to a text frame.
"""
AT_PAGE: TextContentAnchorTypeProto
"""
The object is anchored to the page.
"""
AT_PARAGRAPH: TextContentAnchorTypeProto
"""
The anchor of the object is set at the top left position of the paragraph.
"""
