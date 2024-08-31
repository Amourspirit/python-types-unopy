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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.i18n
from __future__ import annotations
import typing

from .x_transliteration import XTransliteration as XTransliteration_daf70ce3


class XExtendedTransliteration(XTransliteration_daf70ce3):
    """
    This interface provides character conversions like case folding or Hiragana to Katakana.
    
    It is derived from com.sun.star.i18n.XTransliteration and provides additional functionality for character to character and string to string without offset parameter transliteration. These should be used for performance reason if their full-blown counterparts aren't needed.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XExtendedTransliteration <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XExtendedTransliteration.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.i18n.XExtendedTransliteration'

    def transliterateChar2Char(self, cChar: str) -> str:
        """
        Transliterate a character to a character.
        
        If the output contains multiple characters, for example when transliterating German sharp \"s\" (the one that looks like a Greek Beta) to upper case \"SS\", MultipleCharsOutputException will be thrown, the caller must catch the exception and then call XTransliteration.transliterateChar2String() to obtain the correct result.

        Raises:
            MultipleCharsOutputException: ``MultipleCharsOutputException``
        """
        ...
    def transliterateChar2String(self, cChar: str) -> str:
        """
        Transliterate a character to a string.
        """
        ...
    def transliterateString2String(self, aStr: str, nStartPos: int, nCount: int) -> str:
        """
        Transliterate a substring.
        
        The functionality is the same as com.sun.star.i18n.XTransliteration.transliterate() but omits the offset parameter to improve performance.
        """
        ...


