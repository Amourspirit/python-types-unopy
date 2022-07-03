# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class TextContentAnchorType(Enum):
    """
    Enum

    

    See Also:
        `API TextContentAnchorType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text.html#a470b1caeda4ff15fee438c8ff9e3d834>`_
    """
    typeName: str = 'com.sun.star.text.TextContentAnchorType'

    AS_CHARACTER: 'uno.Enum'
    """
    The object is anchored instead of a character.
    """
    AT_CHARACTER: 'uno.Enum'
    """
    The object is anchored to a character.
    """
    AT_FRAME: 'uno.Enum'
    """
    The object is anchored to a text frame.
    """
    AT_PAGE: 'uno.Enum'
    """
    The object is anchored to the page.
    """
    AT_PARAGRAPH: 'uno.Enum'
    """
    The anchor of the object is set at the top left position of the paragraph.
    """

