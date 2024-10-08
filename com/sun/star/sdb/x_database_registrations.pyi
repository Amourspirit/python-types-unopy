# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sdb
from __future__ import annotations
import typing

from abc import ABC
if typing.TYPE_CHECKING:
    from .x_database_registrations_listener import XDatabaseRegistrationsListener as XDatabaseRegistrationsListener_acf11262


class XDatabaseRegistrations(ABC):
    """
    provides access to the application-wide registered databases.
    
    This interface provides a mere wrapper around the respective configuration data, this way hiding the concrete configuration structure from its clients. You should, if possible at all, use this interface, instead of modifying or querying the configuration data directly.
    
    **since**
    
        OOo 3.3

    See Also:
        `API XDatabaseRegistrations <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1XDatabaseRegistrations.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sdb.XDatabaseRegistrations'

    def addDatabaseRegistrationsListener(self, Listener: XDatabaseRegistrationsListener_acf11262) -> None:
        """
        registers a listener which is notified of changes in the registered databases
        """
        ...
    def changeDatabaseLocation(self, Name: str, NewLocation: str) -> None:
        """
        changes the location of a given database registration

        Raises:
            : ````
            : ````
            com.sun.star.lang.IllegalAccessException: ``IllegalAccessException``
        """
        ...
    def getDatabaseLocation(self, Name: str) -> str:
        """
        returns the location of the database registered under the given name

        Raises:
            : ````
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    def getRegistrationNames(self) -> typing.Tuple[str, ...]:
        """
        returns the names of all registered databases
        """
        ...
    def hasRegisteredDatabase(self, Name: str) -> bool:
        """
        determines whether a database is registered under the given name.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def isDatabaseRegistrationReadOnly(self, Name: str) -> bool:
        """
        determines whether the registration data for a database given by name is read-only.
        
        In this case, attempts to revoke this registration will fail.

        Raises:
            : ````
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    def registerDatabaseLocation(self, Name: str, Location: str) -> None:
        """
        registers a database, given by location, under a given name

        Raises:
            : ````
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """
        ...
    def removeDatabaseRegistrationsListener(self, Listener: XDatabaseRegistrationsListener_acf11262) -> None:
        """
        revokes a previously registered listener
        """
        ...
    def revokeDatabaseLocation(self, Name: str) -> None:
        """
        revokes the registration of a database, given by name

        Raises:
            : ````
            : ````
            com.sun.star.lang.IllegalAccessException: ``IllegalAccessException``
        """
        ...


