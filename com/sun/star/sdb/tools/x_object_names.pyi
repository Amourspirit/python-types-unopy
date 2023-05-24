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
# Namespace: com.sun.star.sdb.tools
from __future__ import annotations
import typing

from abc import ABC


class XObjectNames(ABC):
    """
    encapsulates functionality which you might find useful when writing a database application which deals with query and table names.
    
    The most important task fulfilled by this instance is that it hides different naming restrictions from you, which are caused by server-side or client side specialties.
    
    For instance, it can validate names against the characters allowed in the object names of a connection. Also, it relieves you from caring whether a database supports queries in a SELECT statement's FROM part (known as \"queries in queries\"). In such databases, query and table names share a common namespace, thus they must be unique. Using this interface, you can easily ensure this uniqueness.
    
    All of the functionality present in this interface depends on a connection, thus it entry point for obtaining it is a com.sun.star.sdb.Connection service.
    
    The component itself does not have life-time control mechanisms, i.e. you cannot explicitly dispose it (com.sun.star.lang.XComponent.dispose()), and you cannot be notified when it dies.However, if your try to access any of its methods or attributes, after the connection which was used to create it was closed, a com.sun.star.lang.DisposedException will be thrown.
    
    **since**
    
        OOo 2.0.4

    See Also:
        `API XObjectNames <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1tools_1_1XObjectNames.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sdb.tools.XObjectNames'

    def checkNameForCreate(self, CommandType: int, Name: str) -> None:
        """
        checks whether a given name is allowed for a to-be-created table or query in the database.
        
        This method basically does the same checks as isNameUsed() and isNameValid(). In case the given name is not allowed, it throws an exception. This error can be presented to the user, to give it a common experience in all cases where he's required to enter an object name.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def convertToSQLName(self, Name: str) -> str:
        """
        converts the given object name to a name which is valid in the database.
        
        The conversion takes place by converting every character which is neither allowed by the SQL-92 standard, nor part of the special characters supported by the database, with an underscore character (_).
        """
        ...
    def isNameUsed(self, CommandType: int, Name: str) -> bool:
        """
        checks whether a given name is used as table respectively query name in the database.
        
        If in the database, tables and queries share a common namespace, this will be respected by this function.
        
        As before, the information you obtain by calling this method might be obsolete in the very moment you evaluate this, in case another process or thread interferes. However, it's usually sufficiently up-to-date for purpose of using it in a database application driven by user interactions.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def isNameValid(self, CommandType: int, Name: str) -> bool:
        """
        checks whether a given name is valid as table or query name
        
        For tables, the name must consist of characters allowed by the SQL-92 standard, plus characters allowed by the connection as extra name characters.
        
        For queries, names are nearly arbitrary, except that usual quoting characters must not be part of the name.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def suggestName(self, CommandType: int, BaseName: str) -> str:
        """
        suggests a (unique) table or query name
        
        If in the database, tables and queries share a common namespace, this will be respected by this function.
        
        Note that in an multi-threaded environment, the name you obtain here is not absolutely guaranteed to be unique. It is unique at the very moment the function returns to you. But already when you evaluate the returned value, it might not be unique anymore, if another process or thread created a query or table with this name.
        
        This implies that you cannot rely on the name's uniqueness, but you can use it as first guess to present to the user. In most cases, it will still be sufficient when you are actually creating the table respectively query.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...


