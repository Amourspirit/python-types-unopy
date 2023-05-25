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
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .forbidden_characters import ForbiddenCharacters as ForbiddenCharacters_ce0dd5
    from ..lang.locale import Locale as Locale_70d308fa


class XForbiddenCharacters(XInterface_8f010a43):
    """
    provides access to forbidden character settings in a document.
    
    In some languages, particular characters are not allowed to be placed at the beginning or at the end of a text line.

    See Also:
        `API XForbiddenCharacters <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XForbiddenCharacters.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.i18n.XForbiddenCharacters'

    def getForbiddenCharacters(self, aLocale: Locale_70d308fa) -> ForbiddenCharacters_ce0dd5:
        """
        returns the forbidden characters for a given locale.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    def hasForbiddenCharacters(self, aLocale: Locale_70d308fa) -> bool:
        """
        determines if forbidden characters are set for a given locale.
        """
        ...
    def removeForbiddenCharacters(self, aLocale: Locale_70d308fa) -> None:
        """
        removes the setting of forbidden characters for a given locale.
        """
        ...
    def setForbiddenCharacters(self, aLocale: Locale_70d308fa, aForbiddenCharacters: ForbiddenCharacters_ce0dd5) -> None:
        """
        sets the forbidden characters for a given Locale.
        """
        ...



