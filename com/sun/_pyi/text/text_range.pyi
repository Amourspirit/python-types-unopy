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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.text
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa
from ..beans.x_property_state import XPropertyState as XPropertyState_d55c0ccf
from ..container.x_content_enumeration_access import XContentEnumerationAccess as XContentEnumerationAccess_c71012d7
from ..style.character_properties import CharacterProperties as CharacterProperties_1d4f0ef3
from ..style.character_properties_asian import CharacterPropertiesAsian as CharacterPropertiesAsian_6d8a10df
from ..style.character_properties_complex import CharacterPropertiesComplex as CharacterPropertiesComplex_90ca11cb
from ..style.paragraph_properties import ParagraphProperties as ParagraphProperties_1e240efc
from ..style.paragraph_properties_asian import ParagraphPropertiesAsian as ParagraphPropertiesAsian_6e8c10e8
from ..style.paragraph_properties_complex import ParagraphPropertiesComplex as ParagraphPropertiesComplex_91de11d4
from .x_text_range import XTextRange as XTextRange_9a910ab7

class TextRange(CharacterProperties_1d4f0ef3, CharacterPropertiesAsian_6d8a10df, CharacterPropertiesComplex_90ca11cb, ParagraphProperties_1e240efc, ParagraphPropertiesAsian_6e8c10e8, ParagraphPropertiesComplex_91de11d4, XPropertySet_bc180bfa, XPropertyState_d55c0ccf, XContentEnumerationAccess_c71012d7, XTextRange_9a910ab7):
    """
    Service Class

    points to a sequence of characters within a Text.
    
    The service provides access to the string content and the properties of this range of text and the TextContent instances which are bound to this text range.
    
    A TextRange is also used for a text portion which is returned by the com.sun.star.container.XEnumeration for a single paragraph. Because this is the mechanism to use to export data, all formatting attributes and contents bound to this range have to be available from implementations of this service.

    See Also:
        `API TextRange <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1TextRange.html>`_
    """


