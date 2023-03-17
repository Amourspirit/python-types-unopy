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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.table
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class CellAddress(object):
    """
    Struct Class

    contains a cell address within a spreadsheet document.

    See Also:
        `API CellAddress <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1table_1_1CellAddress.html>`_
    """
    typeName: Literal['com.sun.star.table.CellAddress']

    def __init__(self, Sheet: typing.Optional[int] = ..., Column: typing.Optional[int] = ..., Row: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Sheet (int, optional): Sheet value.
            Column (int, optional): Column value.
            Row (int, optional): Row value.
        """
        ...


    @property
    def Sheet(self) -> int:
        """
        is the index of the sheet that contains the cell.
        """
        ...


    @property
    def Column(self) -> int:
        """
        is the index of the column where the cell is located.
        """
        ...


    @property
    def Row(self) -> int:
        """
        is the index of the row where the cell is located.
        """
        ...


