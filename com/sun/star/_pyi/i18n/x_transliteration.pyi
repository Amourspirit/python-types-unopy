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
# Libre Office Version: 7.4
# Namespace: com.sun.star.i18n
from typing_extensions import Literal
import typing
import uno
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .transliteration_modules import TransliterationModules as TransliterationModules_32090f64
    from .transliteration_modules_new import TransliterationModulesNew as TransliterationModulesNew_6260108e
    from ..lang.locale import Locale as Locale_70d308fa

class XTransliteration(XInterface_8f010a43):
    """
    Character conversions like case folding or Hiragana to Katakana.
    
    Transliteration is a character to character conversion but it is not always a one to one mapping between characters. Transliteration modules are primarily used by collation, and search and replace modules to perform approximate search. It can also be used to format the numbers in different numbering systems.
    
    In order to select transliteration modules for different purposes, they are classified with attributes of TransliterationType.
    
    For Western languages there would be three transliteration modules available to compare two mixed case strings: upper to lower, lower to upper, and ignore case.
    
    A typical calling sequence of transliteration is
    
    or another one is

    See Also:
        `API XTransliteration <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XTransliteration.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.i18n.XTransliteration']

    def compareString(self, aStr1: str, aStr2: str) -> int:
        """
        Compare 2 strings as per this transliteration.
        
        It translates both strings before comparing them.
        """
        ...
    def compareSubstring(self, aStr1: str, nOff1: int, nLen1: int, aStr2: str, nOff2: int, nLen2: int) -> int:
        """
        Compare 2 substrings as per this transliteration.
        
        It translates both substrings before comparing them.
        """
        ...
    def equals(self, aStr1: str, nPos1: int, nCount1: int, rMatch1: int, aStr2: str, nPos2: int, nCount2: int, rMatch2: int) -> bool:
        """
        Match two substrings and find if they are equivalent as per this transliteration.
        
        This method can be called if the object has TransliterationType IGNORE attribute.
        
        Returns the number of matched code points in any case, even if strings are not equal, for example: equals( \"a\", 0, 1, nMatch1, \"aaa\", 0, 3, nMatch2 ) returns FALSE and nMatch:=1 and nMatch2:=1 equals( \"aab\", 0, 3, nMatch1, \"aaa\", 0, 3, nMatch2 ) returns FALSE and nMatch:=2 and nMatch2:=2

        * ``rMatch1`` is an out direction argument.
        * ``rMatch2`` is an out direction argument.
        """
        ...
    def folding(self, aInStr: str, nStartPos: int, nCount: int, rOffset: uno.ByteSequence) -> str:
        """

        * ``rOffset`` is an out direction argument.
        """
        ...
    def getAvailableModules(self, aLocale: 'Locale_70d308fa', nType: int) -> 'typing.Tuple[str, ...]':
        """
        List the available transliteration modules for a given locale.
        
        It can be filtered based on its type.
        """
        ...
    def getName(self) -> str:
        """
        Unique ASCII name to identify a module.
        
        This name is used to get its localized name for menus, dialogs etc. The behavior is undefined for TransliterationType.CASCADE modules.
        """
        ...
    def getType(self) -> int:
        """
        Return the attribute(s) associated with this transliteration object, as defined in TransliterationType.
        
        The value is determined by the transliteration modules. For example, for UPPERCASE_LOWERCASE, a ONE_TO_ONE is returned, for IGNORE_CASE, IGNORE is returned.
        """
        ...
    def loadModule(self, eModType: 'TransliterationModules_32090f64', aLocale: 'Locale_70d308fa') -> None:
        """
        Load instance of predefined module - old style method.
        """
        ...
    def loadModuleByImplName(self, aImplName: str, aLocale: 'Locale_70d308fa') -> None:
        """
        Load instance of UNO registered module.
        
        Each transliteration module is registered under a different service name. The convention for the service name is com.sun.star.i18n.Transliteration.l10n.{implName}. The {implName} is a unique name used to identify a module. The implName is used to get a localized name for the transliteration module. The implName is used in locale data to list the available transliteration modules for the locale. There are some transliteration modules that are always available. The names of those modules are listed as enum TransliterationModules names. For modules not listed there it is possible to load them directly by their implName.
        """
        ...
    def loadModuleNew(self, aModType: 'typing.Tuple[TransliterationModulesNew_6260108e, ...]', aLocale: 'Locale_70d308fa') -> None:
        """
        Load a sequence of instances of predefined modules - supersedes method XTransliteration.loadModule().
        """
        ...
    def loadModulesByImplNames(self, aImplNameList: 'typing.Tuple[str, ...]', aLocale: 'Locale_70d308fa') -> None:
        """
        Load a sequence of instances of transliteration modules.
        
        Output of one module is fed as input to the next module in the sequence. The object created by this call has TransliterationType CASCADE and IGNORE types.
        """
        ...
    def transliterate(self, aInStr: str, nStartPos: int, nCount: int, rOffset: uno.ByteSequence) -> str:
        """
        Transliterate a substring.
        
        This method can be called if the object doesn't have TransliterationType IGNORE attribute.

        * ``rOffset`` is an out direction argument.
        """
        ...
    def transliterateRange(self, aStr1: str, aStr2: str) -> 'typing.Tuple[str, ...]':
        """
        Transliterate one set of characters to another.
        
        This method is intended for getting corresponding ranges and can be called if the object has TransliterationType IGNORE attribute.
        
        For example: generic CASE_IGNORE transliterateRange( \"a\", \"i\" ) returns {\"A\",\"I\",\"a\",\"i\"}, transliterateRange( \"a\", \"a\" ) returns {\"A\",\"A\",\"a\",\"a\"}.
        
        Use this transliteration to create regular expressions like [a-i] --> [A-Ia-i].
        """
        ...


