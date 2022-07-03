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
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from .direction3_d import Direction3D as Direction3D_c9370c0c
from .position3_d import Position3D as Position3D_bddc0bc0


class CameraGeometry(object):
    """
    Struct Class

    specifies a three-dimensional camera.

    See Also:
        `API CameraGeometry <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1drawing_1_1CameraGeometry.html>`_
    """
    typeName: Literal['com.sun.star.drawing.CameraGeometry']

    def __init__(self, vrp: typing.Optional[Position3D_bddc0bc0] = ..., vpn: typing.Optional[Direction3D_c9370c0c] = ..., vup: typing.Optional[Direction3D_c9370c0c] = ...) -> None:
        """
        Constructor

        Arguments:
            vrp (Position3D, optional): vrp value.
            vpn (Direction3D, optional): vpn value.
            vup (Direction3D, optional): vup value.
        """
        ...


    @property
    def vrp(self) -> Position3D_bddc0bc0:
        """
        is the camera position
        """
        ...


    @property
    def vpn(self) -> Direction3D_c9370c0c:
        """
        is the camera view direction
        """
        ...


    @property
    def vup(self) -> Direction3D_c9370c0c:
        """
        is the camera up direction
        """
        ...


