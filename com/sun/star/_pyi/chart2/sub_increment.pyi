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
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class SubIncrement(object):
    """
    Struct Class


    See Also:
        `API SubIncrement <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1SubIncrement.html>`_
    """
    typeName: Literal['com.sun.star.chart2.SubIncrement']

    def __init__(self, IntervalCount: typing.Optional[object] = ..., PostEquidistant: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            IntervalCount (object, optional): IntervalCount value.
            PostEquidistant (object, optional): PostEquidistant value.
        """
        ...


    @property
    def IntervalCount(self) -> object:
        """
        should contain nothing for auto, or an integer value for an explicit interval count.
        """
        ...


    @property
    def PostEquidistant(self) -> object:
        """
        should contain nothing for auto, or a boolean value for an explicit setting.
        """
        ...


