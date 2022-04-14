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


class CellVertJustify(Enum):
    """
    Enum Class

    

    See Also:
        `API CellVertJustify <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1table.html#a17834bec5bf9ac4432141dee1c03b50b>`_
    """
    BOTTOM: Literal['BOTTOM']
    """
    contents are aligned to the lower edge of the cell.
    """
    CENTER: Literal['CENTER']
    """
    contents are horizontally centered.
    
    contents are aligned to the vertical middle of the cell.
    """
    STANDARD: Literal['STANDARD']
    """
    default alignment is used (left for numbers, right for text).
    
    default alignment is used.
    
    contents are printed from left to right.
    """
    TOP: Literal['TOP']
    """
    contents are aligned with the upper edge of the cell.
    """

__all__ = ['CellVertJustify']

