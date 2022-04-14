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
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class LanguageCountryInfo(object):
    """
    Struct Class

    The language and country identifiers and descriptive names of the loaded locale data returned by XLocaleData.getLanguageCountryInfo().

    See Also:
        `API LanguageCountryInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1LanguageCountryInfo.html>`_
    """
    typeName: Literal['com.sun.star.i18n.LanguageCountryInfo']

    def __init__(self, Language: typing.Optional[str] = ..., LanguageDefaultName: typing.Optional[str] = ..., Country: typing.Optional[str] = ..., CountryDefaultName: typing.Optional[str] = ..., Variant: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Language (str, optional): Language value.
            LanguageDefaultName (str, optional): LanguageDefaultName value.
            Country (str, optional): Country value.
            CountryDefaultName (str, optional): CountryDefaultName value.
            Variant (str, optional): Variant value.
        """


    @property
    def Language(self) -> str:
        """
        ISO-639 language code, for example, \"en\" or \"de\".
        """


    @property
    def LanguageDefaultName(self) -> str:
        """
        Descriptive language name, for example, \"English\" or \"German\".
        """


    @property
    def Country(self) -> str:
        """
        ISO-3166 country code, for example, \"US\" or \"DE\".
        """


    @property
    def CountryDefaultName(self) -> str:
        """
        Descriptive country name, for example, \"United States\" or \"Germany\".
        """


    @property
    def Variant(self) -> str:
        """
        A variant name.
        """



__all__ = ['LanguageCountryInfo']
