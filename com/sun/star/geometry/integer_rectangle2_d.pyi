# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.geometry
# Libre Office Version: 2024.2
import typing


class IntegerRectangle2D(object):
    """
    Struct Class

    This structure contains the necessary information for a two-dimensional rectangle.
    
    **since**
    
        OOo 2.0

    See Also:
        `API IntegerRectangle2D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1geometry_1_1IntegerRectangle2D.html>`_
    """
    typeName: str = 'com.sun.star.geometry.IntegerRectangle2D'

    def __init__(self, X1: typing.Optional[int] = ..., Y1: typing.Optional[int] = ..., X2: typing.Optional[int] = ..., Y2: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            X1 (int, optional): X1 value.
            Y1 (int, optional): Y1 value.
            X2 (int, optional): X2 value.
            Y2 (int, optional): Y2 value.
        """
        ...

    @property
    def X1(self) -> int:
        """
        X coordinate of upper left corner.
        """
        ...
    @X1.setter
    def X1(self, value: int) -> None:
        ...
    @property
    def Y1(self) -> int:
        """
        Y coordinate of upper left corner.
        """
        ...
    @Y1.setter
    def Y1(self, value: int) -> None:
        ...
    @property
    def X2(self) -> int:
        """
        X coordinate of lower right corner.
        
        Must be greater than X1 for non-empty rectangles.
        """
        ...
    @X2.setter
    def X2(self, value: int) -> None:
        ...
    @property
    def Y2(self) -> int:
        """
        Y coordinate of lower right corner.
        
        Must be greater than y1 for non-empty rectangles.
        """
        ...
    @Y2.setter
    def Y2(self, value: int) -> None:
        ...

