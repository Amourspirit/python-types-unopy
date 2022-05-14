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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.sdbc
from typing_extensions import Literal


class IndexType(object):
    """
    Const

    indicates the type of index.

    See Also:
        `API IndexType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdbc_1_1IndexType.html>`_
    """
    STATISTIC: Literal[0]
    """
    A possible value for column TYPE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc.XDatabaseMetaData.getIndexInfo().
    
    Identifies table statistics that are returned in conjunction with a table's index description.
    """
    CLUSTERED: Literal[1]
    """
    A possible value for column TYPE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc.XDatabaseMetaData.getIndexInfo().
    
    Indicates that this table index is a clustered index.
    """
    HASHED: Literal[2]
    """
    A possible value for column TYPE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc.XDatabaseMetaData.getIndexInfo().
    
    Indicates that this table index is a hashed index.
    """
    OTHER: Literal[3]
    """
    A possible value for column TYPE in the com.sun.star.sdbc.XResultSet object returned by the method com.sun.star.sdbc.XDatabaseMetaData.getIndexInfo().
    
    Indicates that this table index is not a clustered index, a hashed index, or table statistics; it is something other than these.
    """

