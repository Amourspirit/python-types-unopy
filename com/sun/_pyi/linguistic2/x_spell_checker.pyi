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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.linguistic2
from typing_extensions import Literal
import typing
from .x_supported_locales import XSupportedLocales as XSupportedLocales_5bda1056
if typing.TYPE_CHECKING:
    from ..beans.property_values import PropertyValues as PropertyValues_d6470ce6
    from ..lang.locale import Locale as Locale_70d308fa
    from .x_spell_alternatives import XSpellAlternatives as XSpellAlternatives_6ad110bf

class XSpellChecker(XSupportedLocales_5bda1056):
    """
    This interface allows for spell checking.
    
    It is possible to simply check if a word, in a specified language, is correct or additionally, if it was misspelled, some proposals how it might be correctly written.

    See Also:
        `API XSpellChecker <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XSpellChecker.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.linguistic2.XSpellChecker']

    def isValid(self, aWord: str, aLocale: 'Locale_70d308fa', aProperties: 'PropertyValues_d6470ce6') -> bool:
        """
        checks if a word is spelled correctly in a given language.
        
        If aLocale is not supported an IllegalArgumentException exception is raised.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def spell(self, aWord: str, aLocale: 'Locale_70d308fa', aProperties: 'PropertyValues_d6470ce6') -> 'XSpellAlternatives_6ad110bf':
        """
        This method checks if a word is spelled correctly in a given language.
        
        If the language is not supported an IllegalArgumentException exception is raised.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """

__all__ = ['XSpellChecker']

