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
# Libre Office Version: 7.4
# Namespace: com.sun.star.sheet
from typing_extensions import Literal


class MoveDirection(object):
    """
    Const

    used to specify the direction of moving the current selection i.e.
    
    after a cell has been left with Enter.

    See Also:
        `API MoveDirection <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1sheet_1_1MoveDirection.html>`_
    """
    DOWN: Literal[0]
    """
    specifies that the selection moves one cell down.
    """
    RIGHT: Literal[1]
    """
    specifies that the selection moves one cell right.
    """
    UP: Literal[2]
    """
    specifies that the selection moves one cell up.
    """
    LEFT: Literal[3]
    """
    specifies that the selection moves one cell left.
    """

