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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class Size(object):
    """
    Struct Class

    specifies the 2-dimensional size of an area using width and height.

    See Also:
        `API Size <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1Size.html>`_
    """
    typeName: Literal['com.sun.star.awt.Size']

    def __init__(self, Width: typing.Optional[int] = ..., Height: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Width (int, optional): Width value.
            Height (int, optional): Height value.
        """
        ...


    @property
    def Width(self) -> int:
        """
        specifies the width.
        """
        ...


    @property
    def Height(self) -> int:
        """
        specifies the height.
        """
        ...


