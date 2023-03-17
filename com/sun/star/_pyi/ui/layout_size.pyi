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
# Namespace: com.sun.star.ui
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class LayoutSize(object):
    """
    Struct Class

    Size used for layouting windows.
    
    It specifies a range of valid values and a preferred value. The values must not violate the relation 0 â¤ Minimum â¤ Preferred â¤ Maximum.

    See Also:
        `API LayoutSize <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1ui_1_1LayoutSize.html>`_
    """
    typeName: Literal['com.sun.star.ui.LayoutSize']

    def __init__(self, Minimum: typing.Optional[int] = ..., Maximum: typing.Optional[int] = ..., Preferred: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Minimum (int, optional): Minimum value.
            Maximum (int, optional): Maximum value.
            Preferred (int, optional): Preferred value.
        """
        ...


    @property
    def Minimum(self) -> int:
        ...


    @property
    def Maximum(self) -> int:
        ...


    @property
    def Preferred(self) -> int:
        ...


