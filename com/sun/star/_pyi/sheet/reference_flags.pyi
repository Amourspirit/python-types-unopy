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
# Libre Office Version: 7.2
# Namespace: com.sun.star.sheet
from typing_extensions import Literal


class ReferenceFlags(object):
    """
    Const

    defines flags for references.
    
    The values can be combined.

    See Also:
        `API ReferenceFlags <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1ReferenceFlags.html>`_
    """
    COLUMN_RELATIVE: Literal[1]
    """
    selects a relative column reference.
    """
    COLUMN_DELETED: Literal[2]
    """
    marks a deleted column reference.
    """
    ROW_RELATIVE: Literal[4]
    """
    selects a relative row reference.
    """
    ROW_DELETED: Literal[8]
    """
    marks a deleted row reference.
    """
    SHEET_RELATIVE: Literal[16]
    """
    selects a relative sheet reference.
    """
    SHEET_DELETED: Literal[32]
    """
    marks a deleted sheet reference.
    """
    SHEET_3D: Literal[64]
    """
    selects a 3D sheet reference.
    """
    RELATIVE_NAME: Literal[128]
    """
    marks a reference from a relative range name.
    """

