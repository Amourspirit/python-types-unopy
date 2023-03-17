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
# Libre Office Version: 7.4
# Namespace: com.sun.star.sdbc
from typing_extensions import Literal


class BestRowType(object):
    """
    Const

    determines the type of the best row identifier.

    See Also:
        `API BestRowType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sdbc_1_1BestRowType.html>`_
    """
    UNKNOWN: Literal[0]
    """
    indicates that the best row identifier may or may not be a pseudo-column.
    
    A possible value for the column PSEUDO_COLUMN in the com.sun.star.sdbc.XResultSet object returned by the method XDatabaseMetaData.getBestRowIdentifier().
    """
    NOT_PSEUDO: Literal[1]
    """
    indicates that the best row identifier is NOT a pseudo-column.
    
    A possible value for the column PSEUDO_COLUMN in the com.sun.star.sdbc.XResultSet object returned by the method XDatabaseMetaData.getBestRowIdentifier().
    """
    PSEUDO: Literal[2]
    """
    indicates that the best row identifier is a pseudo-column.
    
    A possible value for the column PSEUDO_COLUMN in the com.sun.star.sdbc.XResultSet object returned by the method XDatabaseMetaData.getBestRowIdentifier().
    """

