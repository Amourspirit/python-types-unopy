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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class Rectangle(object):
    """
    Struct Class

    specifies a rectangular area by position and size.

    See Also:
        `API Rectangle <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1Rectangle.html>`_
    """
    typeName: Literal['com.sun.star.awt.Rectangle']

    def __init__(self, X: typing.Optional[int] = ..., Y: typing.Optional[int] = ..., Width: typing.Optional[int] = ..., Height: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            X (int, optional): X value.
            Y (int, optional): Y value.
            Width (int, optional): Width value.
            Height (int, optional): Height value.
        """
        ...


    @property
    def X(self) -> int:
        """
        specifies the x-coordinate.
        """
        ...

    @X.setter
    def X(self, value: int) -> None:
        ...

    @property
    def Y(self) -> int:
        """
        specifies the y-coordinate.
        """
        ...

    @Y.setter
    def Y(self, value: int) -> None:
        ...

    @property
    def Width(self) -> int:
        """
        specifies the width.
        """
        ...

    @Width.setter
    def Width(self, value: int) -> None:
        ...

    @property
    def Height(self) -> int:
        """
        specifies the height.
        """
        ...

    @Height.setter
    def Height(self, value: int) -> None:
        ...

