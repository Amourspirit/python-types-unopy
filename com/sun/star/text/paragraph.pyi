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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.text
from __future__ import annotations
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..beans.x_property_state import XPropertyState as XPropertyState_d55c0ccf
from ..beans.x_tolerant_multi_property_set import XTolerantMultiPropertySet as XTolerantMultiPropertySet_7bd4114e
from ..container.x_enumeration_access import XEnumerationAccess as XEnumerationAccess_4bac0ffc
from ..style.character_properties import CharacterProperties as CharacterProperties_1d4f0ef3
from ..style.character_properties_asian import CharacterPropertiesAsian as CharacterPropertiesAsian_6d8a10df
from ..style.character_properties_complex import CharacterPropertiesComplex as CharacterPropertiesComplex_90ca11cb
from ..style.paragraph_properties import ParagraphProperties as ParagraphProperties_1e240efc
from ..style.paragraph_properties_asian import ParagraphPropertiesAsian as ParagraphPropertiesAsian_6e8c10e8
from ..style.paragraph_properties_complex import ParagraphPropertiesComplex as ParagraphPropertiesComplex_91de11d4
from .text_content import TextContent as TextContent_a6810b4d
from .text_table import TextTable as TextTable_90440a5a

class Paragraph(TextTable_90440a5a, TextContent_a6810b4d, CharacterProperties_1d4f0ef3, CharacterPropertiesComplex_90ca11cb, CharacterPropertiesAsian_6d8a10df, ParagraphProperties_1e240efc, ParagraphPropertiesComplex_91de11d4, ParagraphPropertiesAsian_6e8c10e8, XPropertySet_bc180bfa, XPropertyState_d55c0ccf, XEnumerationAccess_4bac0ffc, XTolerantMultiPropertySet_7bd4114e):
    """
    Service Class

    is a piece of text which can take its own paragraph-specific attributes (technically, properties).
    
    **since**
    
        OOo 2.0

    See Also:
        `API Paragraph <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1Paragraph.html>`_
    """
    ...

