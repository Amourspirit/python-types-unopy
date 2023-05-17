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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.i18n
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .x_index_entry_supplier import XIndexEntrySupplier as XIndexEntrySupplier_1cb0dfe
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa


class XExtendedIndexEntrySupplier(XIndexEntrySupplier_1cb0dfe):
    """
    This interface provides information for creating \"Table of Index\".
    
    It is derived from com.sun.star.i18n.XIndexEntrySupplier and provides following additional functionalities.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XExtendedIndexEntrySupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XExtendedIndexEntrySupplier.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.i18n.XExtendedIndexEntrySupplier']

    def compareIndexEntry(self, aIndexEntry1: str, aPhoneticEntry1: str, aLocale1: 'Locale_70d308fa', aIndexEntry2: str, aPhoneticEntry2: str, aLocale2: 'Locale_70d308fa') -> int:
        """
        Compares index entries.
        
        Note that loadAlgorithm should be called before calling this function.
        """
        ...
    def getAlgorithmList(self, aLocale: 'Locale_70d308fa') -> 'typing.Tuple[str, ...]':
        """
        Returns index algorithm list for specific locale.
        """
        ...
    def getIndexKey(self, aIndexEntry: str, aPhoneticEntry: str, aLocale: 'Locale_70d308fa') -> str:
        """
        Returns index key.
        
        Note that loadAlgorithm should be called before calling this function.
        """
        ...
    def getLocaleList(self) -> 'typing.Tuple[Locale_70d308fa, ...]':
        """
        Returns locale list for which the IndexEntrySupplier provides service.
        """
        ...
    def getPhoneticCandidate(self, aIndexEntry: str, aLocale: 'Locale_70d308fa') -> str:
        """
        Returns phonetic candidate for index entry for the locale.
        """
        ...
    def loadAlgorithm(self, aLocale: 'Locale_70d308fa', aIndexAlgorithm: str, nCollatorOptions: int) -> bool:
        """
        Loads index algorithm for the locale.
        """
        ...
    def usePhoneticEntry(self, aLocale: 'Locale_70d308fa') -> bool:
        """
        Checks if Phonetic Entry should be used for the locale.
        """
        ...


