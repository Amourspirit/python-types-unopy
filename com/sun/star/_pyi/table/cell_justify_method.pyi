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
# Namespace: com.sun.star.table
from typing_extensions import Literal


class CellJustifyMethod(object):
    """
    Const

    Specifies how text inside a cell is justified.
    
    The justification methods closely follow the methods described under the text-justify property of the CSS Text Level 3 specification. The latest version of the aforementioned specification is found here http://www.w3.org/TR/css3-text/.

    See Also:
        `API CellJustifyMethod <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1table_1_1CellJustifyMethod.html>`_
    """
    AUTO: Literal[0]
    """
    Automatic.
    """
    DISTRIBUTE: Literal[1]
    """
    When applied in the direction of text flow, characters in each line are distributed at equal intervals so that the ends of each line are aligned with the start and end edges of the cell.
    
    When applied in the perpendicular direction of text flow, the lines are distributed at equal intervals so that the first and last lines are aligned with the start and end edges of the cell.
    """

