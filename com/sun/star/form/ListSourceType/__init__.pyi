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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.form
# Libre Office Version: 7.4
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
"""
Enum



See Also:
    `API ListSourceType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1form.html#a52e06ed91fb133bc98c089a401a724fb>`_
"""
typeName: str = 'com.sun.star.form.ListSourceType'

QUERY: 'uno.Enum'
"""
The control should be filled with the results of a database query.
"""
SQL: 'uno.Enum'
"""
The control should be filled with the results of a database statement.
"""
SQLPASSTHROUGH: 'uno.Enum'
"""
The control should be filled with the results of a database statement, which is not evaluated by the database engine.
"""
TABLE: 'uno.Enum'
"""
The control should be filled with the data of a table.
"""
TABLEFIELDS: 'uno.Enum'
"""
The control should be filled with the field names of a database table.
"""
VALUELIST: 'uno.Enum'
"""
The control should be filled with a list of string values.
"""

