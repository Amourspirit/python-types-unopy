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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.util
# Libre Office Version: 7.3
from typing_extensions import Literal
from .search_options import SearchOptions as SearchOptions_bd140c08
from .search_algorithms import SearchAlgorithms as SearchAlgorithms_e2c00d36
from ..lang.locale import Locale as Locale_70d308fa
import typing


class SearchOptions2(SearchOptions_bd140c08):
    """
    Struct Class

    This augments com.sun.star.util.SearchOptions to be able to specify additional search algorithms for use with com.sun.star.util.XTextSearch2.
    
    **since**
    
        LibreOffice 5.2

    See Also:
        `API SearchOptions2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1SearchOptions2.html>`_
    """
    typeName: Literal['com.sun.star.util.SearchOptions2']

    def __init__(self, algorithmType: typing.Optional[SearchAlgorithms_e2c00d36] = ..., searchFlag: typing.Optional[int] = ..., searchString: typing.Optional[str] = ..., replaceString: typing.Optional[str] = ..., Locale: typing.Optional[Locale_70d308fa] = ..., changedChars: typing.Optional[int] = ..., deletedChars: typing.Optional[int] = ..., insertedChars: typing.Optional[int] = ..., transliterateFlags: typing.Optional[int] = ..., AlgorithmType2: typing.Optional[int] = ..., WildcardEscapeCharacter: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            algorithmType (SearchAlgorithms, optional): algorithmType value.
            searchFlag (int, optional): searchFlag value.
            searchString (str, optional): searchString value.
            replaceString (str, optional): replaceString value.
            Locale (Locale, optional): Locale value.
            changedChars (int, optional): changedChars value.
            deletedChars (int, optional): deletedChars value.
            insertedChars (int, optional): insertedChars value.
            transliterateFlags (int, optional): transliterateFlags value.
            AlgorithmType2 (int, optional): AlgorithmType2 value.
            WildcardEscapeCharacter (int, optional): WildcardEscapeCharacter value.
        """


    @property
    def AlgorithmType2(self) -> int:
        """
        Search type, one of com.sun.star.util.SearchAlgorithms2 constants.
        
        This is preferred over the content of the SearchAlgorithms SearchOptions.algorithmType enum field.
        """


    @property
    def WildcardEscapeCharacter(self) -> int:
        """
        The escape character to be used with a com.sun.star.util.SearchAlgorithms2.WILDCARD search.
        
        A Unicode character, if not 0 escapes the special meaning of a question mark, asterisk or escape character that follows immediately after the escape character. If 0 defines no escape character is used.
        
        Common values are '\\' (U+005C REVERSE SOLIDUS) aka backslash in text processing context, or '~' (U+007E TILDE) in spreadsheet processing context.
        """

