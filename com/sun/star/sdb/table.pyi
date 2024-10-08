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
# Namespace: com.sun.star.sdb
from __future__ import annotations
from .data_settings import DataSettings as DataSettings_a3000b0c
from ..sdbcx.table import Table as Table_71780904

class Table(DataSettings_a3000b0c, Table_71780904):
    """
    Service Class

    extends the service com.sun.star.sdbcx.Table with additional display information, sorting, and filtering criteria.

    See Also:
        `API Table <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdb_1_1Table.html>`_
    """
    @property
    def Privileges(self) -> int:
        """
        indicates the privileges for the table.
        """
        ...
    @Privileges.setter
    def Privileges(self, value: int) -> None:
        ...

