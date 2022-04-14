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
# Namespace: com.sun.star.resource
from typing_extensions import Literal
import typing
from .x_string_resource_resolver import XStringResourceResolver as XStringResourceResolver_92cb11d9
if typing.TYPE_CHECKING:
    from ..lang.locale import Locale as Locale_70d308fa

class XStringResourceManager(XStringResourceResolver_92cb11d9):
    """
    Interface to manage a resource string table containing a set of strings for different locales.
    
    The interface is derived from com.sun.star.resource.XStringResourceResolver that allows to access the string table but not to modify it. This interface also allows to modify the string table.
    
    It's designed to be used in the context of creating a string table, e.g. from a string table editor or from a Dialog Editor designing localized dialogs.

    See Also:
        `API XStringResourceManager <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1resource_1_1XStringResourceManager.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.resource.XStringResourceManager']

    def getUniqueNumericId(self) -> int:
        """
        Provides a numeric id that is unique within all Resource IDs used in the string table.
        
        This method takes into account all Resource IDs starting with a decimal number and only evaluates the ID until the first non digit character is reached. This allows to extend unique IDs with individual identifiers without breaking the mechanism of this method.
        
        Examples: ID \"42\" -> numeric id 42 ID \"0foo\" -> numeric id 0 ID \"111.MyId.Something.Else\" -> numeric id 111 ID \"No Digits\" -> not considered for numeric id
        
        The id returned will be 0 for an empty string table and it will be reset to 0 if all locales are removed. In all other cases this method returns the maximum numeric id used so far at the beginning of a Resource ID incremented by 1. When calling this method more than once always the same number will be returned until this number is really used at the beginning of a new Resource ID passed to setString() or setStringForLocale().
        
        As the numeric id is guaranteed to be unique for the complete string table all locales are taken into account. So using this methods will force the implementation to load all locale data that may not have been loaded so far.

        Raises:
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
    def isReadOnly(self) -> bool:
        """
        Returns the resource's read only state.
        """
    def newLocale(self, locale: 'Locale_70d308fa') -> None:
        """
        Creates a new locale.
        
        For each existing ResourceID an empty string will be created. The first locale created will automatically be the first default locale. Otherwise strings for all already created IDs will be copied from the default locale.

        Raises:
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
    def removeId(self, ResourceID: str) -> None:
        """
        Removes a Resource ID including the corresponding string for the current locale.

        Raises:
            com.sun.star.resource.MissingResourceException: ``MissingResourceException``
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
    def removeIdForLocale(self, ResourceID: str, locale: 'Locale_70d308fa') -> None:
        """
        Removes a Resource ID including the corresponding string for s specific locale.

        Raises:
            com.sun.star.resource.MissingResourceException: ``MissingResourceException``
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
    def removeLocale(self, locale: 'Locale_70d308fa') -> None:
        """
        Removes a locale completely including the corresponding strings for each locale.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
    def setCurrentLocale(self, Locale: 'Locale_70d308fa', FindClosestMatch: bool) -> None:
        """
        Sets the locale to be used.
        
        If true: If the exact locale that should be set is not available the method tries to find the closest match. E.g. if en_US is re- quired but not available, en would be the next choice. Finally the default locale will be used TRUE.
        
        If false: If the exact locale that should be set is not available a com.sun.star.lang.IllegalArgumentException is thrown.
        
        If false: If the exact locale that should be set is not available a com.sun.star.lang.IllegalArgumentException is thrown.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def setDefaultLocale(self, Locale: 'Locale_70d308fa') -> None:
        """
        Sets the default locale to be used.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
    def setString(self, ResourceID: str, Str: str) -> None:
        """
        Associates a String to a Resource ID for the current locale.
        
        If an entry for the Resource ID already exists, the string associated with it will be overwritten, otherwise a new entry will be created.

        Raises:
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """
    def setStringForLocale(self, ResourceID: str, Str: str, locale: 'Locale_70d308fa') -> None:
        """
        Associates a String to a Resource ID for a specific locale.
        
        If an entry for the Resource ID already exists, the string associated with it will be overwritten, otherwise a new entry will be created.
        
        It's not recommended to use this method to get the best performance as the implementation may be optimized for the use of the current locale.

        Raises:
            com.sun.star.lang.NoSupportException: ``NoSupportException``
        """

__all__ = ['XStringResourceManager']

