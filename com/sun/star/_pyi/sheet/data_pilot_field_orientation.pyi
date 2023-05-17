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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.4
from __future__ import annotations
import uno


class DataPilotFieldOrientation(uno.Enum):
    """
    Enum


    See Also:
        `API DataPilotFieldOrientation <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet.html#a686c797e7cb837947558aa11c946245a>`_
    """
    typeName: str = 'com.sun.star.sheet.DataPilotFieldOrientation'

    COLUMN: DataPilotFieldOrientation = ...
    """
    the field is used as a column field.
    
    is applied to the columns.
    """
    DATA: DataPilotFieldOrientation = ...
    """
    the field is used as a data field.
    """
    HIDDEN: DataPilotFieldOrientation = ...
    """
    the field is not used in the table.
    """
    PAGE: DataPilotFieldOrientation = ...
    """
    the field is used as a page field.
    """
    ROW: DataPilotFieldOrientation = ...
    """
    the field is used as a row field.
    
    is applied to the rows.
    """

