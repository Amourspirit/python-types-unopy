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
# Namespace: com.sun.star.geometry
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class RealRectangle2D(object):
    """
    Struct Class

    This structure contains the necessary information for a two-dimensional rectangle.
    
    **since**
    
        OOo 2.0

    See Also:
        `API RealRectangle2D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1geometry_1_1RealRectangle2D.html>`_
    """
    typeName: Literal['com.sun.star.geometry.RealRectangle2D']

    def __init__(self, X1: typing.Optional[float] = ..., Y1: typing.Optional[float] = ..., X2: typing.Optional[float] = ..., Y2: typing.Optional[float] = ...) -> None:
        """
        Constructor

        Arguments:
            X1 (float, optional): X1 value.
            Y1 (float, optional): Y1 value.
            X2 (float, optional): X2 value.
            Y2 (float, optional): Y2 value.
        """
        ...


    @property
    def X1(self) -> float:
        """
        X coordinate of upper left corner .
        """
        ...

    @X1.setter
    def X1(self, value: float) -> None:
        ...

    @property
    def Y1(self) -> float:
        """
        Y coordinate of upper left corner.
        """
        ...

    @Y1.setter
    def Y1(self, value: float) -> None:
        ...

    @property
    def X2(self) -> float:
        """
        X coordinate of lower right corner.
        
        Must be greater than x1 for non-empty rectangles.
        
        .
        """
        ...

    @X2.setter
    def X2(self, value: float) -> None:
        ...

    @property
    def Y2(self) -> float:
        """
        Y coordinate of lower right corner.
        
        Must be greater than y1 for non-empty rectangles.
        """
        ...

    @Y2.setter
    def Y2(self, value: float) -> None:
        ...

