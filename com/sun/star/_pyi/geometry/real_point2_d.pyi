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
# Namespace: com.sun.star.geometry
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class RealPoint2D(object):
    """
    Struct Class

    This structure defines a two-dimensional point.
    
    This structure contains x and y real-valued coordinates of a two-dimensional point.
    
    **since**
    
        OOo 2.0

    See Also:
        `API RealPoint2D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1geometry_1_1RealPoint2D.html>`_
    """
    typeName: Literal['com.sun.star.geometry.RealPoint2D']

    def __init__(self, X: typing.Optional[float] = ..., Y: typing.Optional[float] = ...) -> None:
        """
        Constructor

        Arguments:
            X (float, optional): X value.
            Y (float, optional): Y value.
        """
        ...


    @property
    def X(self) -> float:
        """
        The x coordinate of the point.
        """
        ...


    @property
    def Y(self) -> float:
        """
        The x coordinate of the point.
        """
        ...


