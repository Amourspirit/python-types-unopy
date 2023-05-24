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
# Namespace: com.sun.star.sdb
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa


class XSQLQueryComposer(XInterface_8f010a43):
    """
    should be provided by a tool which simplifies the handling with SQL select statements.
    
    The interface can be used for composing SELECT statements without knowing the structure of the used query.

    See Also:
        `API XSQLQueryComposer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1XSQLQueryComposer.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sdb.XSQLQueryComposer'

    def appendFilterByColumn(self, column: XPropertySet_bc180bfa) -> None:
        """
        appends a new filter condition by a com.sun.star.sdb.DataColumn providing the name and the value for the filter.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def appendOrderByColumn(self, column: XPropertySet_bc180bfa, ascending: bool) -> None:
        """
        appends an additional part to the sort order criteria of the select statement.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def getComposedQuery(self) -> str:
        """
        returns the query composed with filters and sort criteria.
        """
        ...
    def getFilter(self) -> str:
        """
        returns the currently used filter.
        
        The filter criteria returned is part of the where condition of the select command, but it does not contain the where token.
        """
        ...
    def getOrder(self) -> str:
        """
        returns the currently used sort order.
        
        The order criteria returned is part of the ORDER BY clause of the select command, but it does not contain the ORDER BY keyword .
        """
        ...
    def getQuery(self) -> str:
        """
        returns the query used for composing.
        """
        ...
    def getStructuredFilter(self) -> typing.Tuple[typing.Tuple[PropertyValue_c9610c73, ...], ...]:
        """
        returns the currently used filter.
        
        The filter criteria is split into levels. Each level represents the OR criteria. Within each level, the filters are provided as an AND criteria with the name of the column and the filter condition. The filter condition is of type string.
        """
        ...
    def setFilter(self, filter: str) -> None:
        """
        makes it possible to set a filter condition for the query.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def setOrder(self, order: str) -> None:
        """
        makes it possible to set a sort condition for the query.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...
    def setQuery(self, command: str) -> None:
        """
        sets a new query for the composer, which may be expanded by filters and sort criteria.

        Raises:
            com.sun.star.sdbc.SQLException: ``SQLException``
        """
        ...


