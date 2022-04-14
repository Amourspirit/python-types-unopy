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
from ..container.x_named import XNamed as XNamed_a6520b08
if typing.TYPE_CHECKING:
    from .dictionary_type import DictionaryType as DictionaryType_2ba50f2d
    from .x_dictionary_entry import XDictionaryEntry as XDictionaryEntry_49ef0ff5
    from .x_dictionary_event_listener import XDictionaryEventListener as XDictionaryEventListener_d74c132b

class XDictionary1(XNamed_a6520b08):
    """
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XDictionary1 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XDictionary1.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.linguistic2.XDictionary1']

    def add(self, aWord: str, bIsNegative: bool, aRplcText: str) -> bool:
        """
        """
    def addDictionaryEventListener(self, xListener: 'XDictionaryEventListener_d74c132b') -> bool:
        """
        """
    def addEntry(self, xDicEntry: 'XDictionaryEntry_49ef0ff5') -> bool:
        """
        """
    def clear(self) -> None:
        """
        """
    def getCount(self) -> int:
        """
        """
    def getDictionaryType(self) -> 'DictionaryType_2ba50f2d':
        """
        """
    def getEntries(self) -> 'typing.Tuple[XDictionaryEntry_49ef0ff5, ...]':
        """
        """
    def getEntry(self, aWord: str) -> 'XDictionaryEntry_49ef0ff5':
        """
        """
    def getLanguage(self) -> int:
        """
        """
    def isActive(self) -> bool:
        """
        """
    def isFull(self) -> bool:
        """
        """
    def remove(self, aWord: str) -> bool:
        """
        """
    def removeDictionaryEventListener(self, xListener: 'XDictionaryEventListener_d74c132b') -> bool:
        """
        """
    def setActive(self, bActivate: bool) -> None:
        """
        """
    def setLanguage(self, nLang: int) -> None:
        """
        """

__all__ = ['XDictionary1']

