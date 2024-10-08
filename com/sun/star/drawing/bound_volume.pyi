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
# Namespace: com.sun.star.drawing
# Libre Office Version: 2024.2
import typing
from .position3_d import Position3D as Position3D_bddc0bc0


class BoundVolume(object):
    """
    Struct Class

    specifies a three-dimensional boundary volume with two positions.

    See Also:
        `API BoundVolume <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1BoundVolume.html>`_
    """
    typeName: str = 'com.sun.star.drawing.BoundVolume'

    def __init__(self, min: typing.Optional[Position3D_bddc0bc0] = ..., max: typing.Optional[Position3D_bddc0bc0] = ...) -> None:
        """
        Constructor

        Arguments:
            min (Position3D, optional): min value.
            max (Position3D, optional): max value.
        """
        ...

    @property
    def min(self) -> Position3D_bddc0bc0:
        """
        this is the minimum position inside the boundary volume.
        """
        ...
    @min.setter
    def min(self, value: Position3D_bddc0bc0) -> None:
        ...
    @property
    def max(self) -> Position3D_bddc0bc0:
        """
        this is the maximum position inside the boundary volume.
        """
        ...
    @max.setter
    def max(self, value: Position3D_bddc0bc0) -> None:
        ...

