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
    from ..lang.locale import Locale as Locale_70d308fa
    from .dictionary_type import DictionaryType as DictionaryType_2ba50f2d
    from .x_dictionary_entry import XDictionaryEntry as XDictionaryEntry_49ef0ff5
    from .x_dictionary_event_listener import XDictionaryEventListener as XDictionaryEventListener_d74c132b

class XDictionary(XNamed_a6520b08):
    """
    This interfaces enables the object to access personal dictionaries.
    
    Personal dictionaries are used to supply additional information for spell checking and hyphenation (see com.sun.star.linguistic2.XDictionaryEntry). Only active dictionaries with an appropriate language are used for that purpose. The entries of an active, positive dictionary are words that are required to be recognized as correct during the spell checking process. Additionally, they will be used for hyphenation. Entries of a negative dictionary are required to be recognized as negative words, for example, words that should not be used, during SPELLCHECK. An entry in a negative dictionary may supply a proposal for a word to be used instead of the one being used.

    See Also:
        `API XDictionary <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XDictionary.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.linguistic2.XDictionary']

    def add(self, aWord: str, bIsNegative: bool, aRplcText: str) -> bool:
        """
        is used to make an entry in the dictionary.
        
        If an entry already exists, the dictionary remains unchanged and FALSE will be returned.
        
        In positive dictionaries only positive entries can be made, and in negative ones only negative entries.
        """
    def addDictionaryEventListener(self, xListener: 'XDictionaryEventListener_d74c132b') -> bool:
        """
        adds an entry to the list of dictionary event listeners.
        
        On dictionary events, each entry in the listener list will be notified via a call to com.sun.star.linguistic2.XDictionaryEventListener.processDictionaryEvent().
        """
    def addEntry(self, xDicEntry: 'XDictionaryEntry_49ef0ff5') -> bool:
        """
        is used to add an entry to the dictionary.
        
        If an entry already exists, the dictionary remains unchanged and FALSE will be returned.
        
        In positive dictionaries only positive entries can be made, and in negative ones only negative entries.
        """
    def clear(self) -> None:
        """
        removes all entries from the dictionary.
        """
    def getCount(self) -> int:
        """
        """
    def getDictionaryType(self) -> 'DictionaryType_2ba50f2d':
        """
        returns the type of the dictionary.
        """
    def getEntries(self) -> 'typing.Tuple[XDictionaryEntry_49ef0ff5, ...]':
        """
        This function should no longer be used since with the expansion of the maximum number of allowed entries the result may become unreasonable large!
        """
    def getEntry(self, aWord: str) -> 'XDictionaryEntry_49ef0ff5':
        """
        searches for an entry that matches the given word.
        """
    def getLocale(self) -> 'Locale_70d308fa':
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
        removes an entry from the dictionary.
        """
    def removeDictionaryEventListener(self, xListener: 'XDictionaryEventListener_d74c132b') -> bool:
        """
        removes an entry from the list of dictionary event listeners.
        """
    def setActive(self, bActivate: bool) -> None:
        """
        specifies whether the dictionary should be used or not .
        """
    def setLocale(self, aLocale: 'Locale_70d308fa') -> None:
        """
        is used to set the language of the dictionary.
        """

__all__ = ['XDictionary']

