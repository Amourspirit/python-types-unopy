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
# Namespace: com.sun.star.util
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa
    from .alias_programmatic_pair import AliasProgrammaticPair as AliasProgrammaticPair_2a930f22

class XLocalizedAliases(XInterface_8f010a43):
    """
    is the interface for binding programmatic names to aliases.
    
    Aliases can be provided in several locales for the same programmatic name.

    See Also:
        `API XLocalizedAliases <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XLocalizedAliases.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.util.XLocalizedAliases']

    def bindAlias(self, programmaticName: str, locale: 'Locale_70d308fa', alias: str) -> None:
        """
        registers an alias for a programmatic name.

        Raises:
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """
        ...
    def listAliases(self, locale: 'Locale_70d308fa') -> 'typing.Tuple[AliasProgrammaticPair_2a930f22, ...]':
        """
        retrieves a list of all registered aliases for a certain language.
        """
        ...
    def lookupAlias(self, locale: 'Locale_70d308fa', Alias: str) -> str:
        """
        retrieves a registered programmatic name identified by an alias.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    def lookupProgrammatic(self, locale: 'Locale_70d308fa', programmatic: str) -> str:
        """
        retrieves a given alias for a programmatic name.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    def rebindAliases(self, currentProgrammatic: str, newProgrammatic: str) -> None:
        """
        rebinds all aliases registered to a given URL to a new one.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """
        ...
    def renameAlias(self, locale: 'Locale_70d308fa', oldName: str, aNewName: str) -> None:
        """
        renames an alias for a programmatic name.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """
        ...
    def unbindAlias(self, locale: 'Locale_70d308fa', alias: str) -> None:
        """
        revokes an alias for a programmatic name.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    def unbindAliases(self, programmaticName: str) -> None:
        """
        removes all aliases for a programmatic name.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...


