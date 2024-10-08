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
from .x_groups_supplier import XGroupsSupplier as XGroupsSupplier_e3410d48
from .x_tables_supplier import XTablesSupplier as XTablesSupplier_e1ad0d23
from .x_users_supplier import XUsersSupplier as XUsersSupplier_d6060cda
from .x_views_supplier import XViewsSupplier as XViewsSupplier_d5cd0cd6

class DatabaseDefinition(XGroupsSupplier_e3410d48, XTablesSupplier_e1ad0d23, XUsersSupplier_d6060cda, XViewsSupplier_d5cd0cd6):
    """
    Service Class

    could be used as an extension for performing data definition tasks on databases, and to control the access rights on database objects.
    
    It may be implemented by a database driver provider, to encapsulate the complexity of data definition, and to give a common way for data definition as the DDL of most DBMS differs.
    
    At least, the access to the tables of a database should be implemented. The implementation of other known database objects like views is optional.
    
    To control the access rights of users, there is the possibility to implement objects like users and groups.

    See Also:
        `API DatabaseDefinition <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1sdbcx_1_1DatabaseDefinition.html>`_
    """
    ...

