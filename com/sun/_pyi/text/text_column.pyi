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
# Namespace: com.sun.star.text
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class TextColumn(object):
    """
    Struct Class

    defines a single text column.

    See Also:
        `API TextColumn <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1TextColumn.html>`_
    """
    typeName: Literal['com.sun.star.text.TextColumn']

    def __init__(self, Width: typing.Optional[int] = ..., LeftMargin: typing.Optional[int] = ..., RightMargin: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Width (int, optional): Width value.
            LeftMargin (int, optional): LeftMargin value.
            RightMargin (int, optional): RightMargin value.
        """


    @property
    def Width(self) -> int:
        """
        contains the relative width of the column, including both margins.
        
        Width isn't a metric value, it's a relative value to the sum of the width of all columns.
        """


    @property
    def LeftMargin(self) -> int:
        """
        contains the left margin of the column.
        
        This is a metric value.
        """


    @property
    def RightMargin(self) -> int:
        """
        contains the right margin of the column.
        
        This is a metric value.
        """



__all__ = ['TextColumn']
