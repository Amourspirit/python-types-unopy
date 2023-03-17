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
# Namespace: com.sun.star.chart2
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing
from ..drawing.direction3_d import Direction3D as Direction3D_c9370c0c


class LightSource(object):
    """
    Struct Class


    See Also:
        `API LightSource <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1LightSource.html>`_
    """
    typeName: Literal['com.sun.star.chart2.LightSource']

    def __init__(self, nDiffuseColor: typing.Optional[int] = ..., aDirection: typing.Optional[Direction3D_c9370c0c] = ..., bIsEnabled: typing.Optional[bool] = ..., bSpecular: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            nDiffuseColor (int, optional): nDiffuseColor value.
            aDirection (Direction3D, optional): aDirection value.
            bIsEnabled (bool, optional): bIsEnabled value.
            bSpecular (bool, optional): bSpecular value.
        """
        ...


    @property
    def nDiffuseColor(self) -> int:
        """
        the light source's color
        """
        ...


    @property
    def aDirection(self) -> Direction3D_c9370c0c:
        """
        the direction into which the light-source points
        """
        ...


    @property
    def bIsEnabled(self) -> bool:
        ...


    @property
    def bSpecular(self) -> bool:
        """
        When TRUE, the specularity of material is taken into account when lighting an object.
        """
        ...


