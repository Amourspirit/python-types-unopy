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
# Enum Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.table
# Libre Office Version: 7.2
from typing_extensions import Literal
from enum import Enum


class TableSortFieldType(Enum):
    """
    Enum Class

    

    See Also:
        `API TableSortFieldType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1table.html#a8f4f5a263cd762ae00ab0f462ed1ae1c>`_
    """
    ALPHANUMERIC: Literal['ALPHANUMERIC']
    """
    sort field contains text data.
    """
    AUTOMATIC: Literal['AUTOMATIC']
    """
    type is determined automatically.
    """
    NUMERIC: Literal['NUMERIC']
    """
    sort field contains numerical data.
    """

__all__ = ['TableSortFieldType']

