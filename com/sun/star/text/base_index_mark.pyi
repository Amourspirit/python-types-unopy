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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.text
from __future__ import annotations
from .text_content import TextContent as TextContent_a6810b4d

class BaseIndexMark(TextContent_a6810b4d):
    """
    Service Class

    is a TextRange which is explicitly marked as an index entry.
    
    This is the base service of index marks for DocumentIndex, ContentIndex, and UserIndex.

    See Also:
        `API BaseIndexMark <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1BaseIndexMark.html>`_
    """
    @property
    def AlternativeText(self) -> str:
        """
        the string that will be inserted into the corresponding index.
        
        If AlternativeText is empty then the string that is marked by the TextRange is inserted into the index.
        """
        ...
    @AlternativeText.setter
    def AlternativeText(self, value: str) -> None:
        ...
