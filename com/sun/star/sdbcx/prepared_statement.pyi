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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.sdbcx
from __future__ import annotations
from ..sdbc.prepared_statement import PreparedStatement as PreparedStatement_eef40d8c

class PreparedStatement(PreparedStatement_eef40d8c):
    """
    Service Class

    extends the definition of the service com.sun.star.sdbc.PreparedStatement with a flag for the usage of bookmarks.

    See Also:
        `API PreparedStatement <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbcx_1_1PreparedStatement.html>`_
    """
    @property
    def UseBookmarks(self) -> bool:
        """
        returns if a result set should allow the navigation with bookmarks or not.
        
        The default is FALSE.
        """
        ...
    @UseBookmarks.setter
    def UseBookmarks(self, value: bool) -> None:
        ...

