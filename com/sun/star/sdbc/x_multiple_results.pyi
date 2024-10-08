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
# Namespace: com.sun.star.sdbc
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_result_set import XResultSet as XResultSet_98e30aa7


class XMultipleResults(XInterface_8f010a43):
    """
    is used for inspecting multiple results produced by the execution of a SQL statement.
    
    Under some (uncommon) situations a single SQL statement may return multiple result sets and/or update counts. Normally you can ignore this unless you are (1) executing a stored procedure that you know may return multiple results or (2) you are dynamically executing an unknown SQL string. The methods com.sun.star.sdbc.XMultipleResults.getMoreResults() , com.sun.star.sdbc.XMultipleResults.getResultSet() and com.sun.star.sdbc.XMultipleResults.getUpdateCount() let you navigate through multiple results.

    See Also:
        `API XMultipleResults <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XMultipleResults.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sdbc.XMultipleResults'

    def getMoreResults(self) -> bool:
        """
        moves to a Statement's next result.
        
        It returns TRUE if this result is a ResultSet. This method also implicitly closes any current ResultSet obtained with getResultSet.
        
        There are no more results when (!getMoreResults() &amp;&amp; getUpdateCount() == -1).

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def getResultSet(self) -> XResultSet_98e30aa7:
        """
        returns the current result as a com.sun.star.sdbc.ResultSet object.
        
        This method should be called only once per result.

        Raises:
            SQLException: ``SQLException``
        """
        ...
    def getUpdateCount(self) -> int:
        """
        returns the current result as an update count.
        
        If the result is a ResultSet or there are no more results, -1 is returned. This method should be called only once per result.

        Raises:
            SQLException: ``SQLException``
        """
        ...


