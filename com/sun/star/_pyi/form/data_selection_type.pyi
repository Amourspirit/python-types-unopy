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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.form
# Libre Office Version: 7.4
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class DataSelectionType(Enum):
    """
    Enum

    

    See Also:
        `API DataSelectionType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1form.html#abce772d425e368c8a4f81abe7afa7279>`_
    """
    typeName: str = 'com.sun.star.form.DataSelectionType'

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

