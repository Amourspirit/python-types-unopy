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
# Namespace: com.sun.star.linguistic2
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa

class XNumberText(ABC):
    """
    This interface allows to spell out numbers and money amounts.
    
    The current set of supported languages is:
    
    **since**
    
        LibreOffice 6.1

    See Also:
        `API XNumberText <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XNumberText.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.linguistic2.XNumberText']

    def getAvailableLanguages(self) -> 'typing.Tuple[Locale_70d308fa, ...]':
        """
        returns a list of all supported languages.
        """
        ...
    def getNumberText(self, aText: str, aLocale: 'Locale_70d308fa') -> str:
        """
        spell out numbers and money amounts
        
        Please note that text argument can contain prefixes separated by space, for example \"ordinal\" for ordinal numbers, \"ordinal-number\" for ordinal indicators and ISO 4217 currency codes.
        
        Language modules list the supported prefixes by the input text \"help\".

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...


