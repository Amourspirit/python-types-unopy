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
# Namespace: com.sun.star.bridge.oleautomation
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class Decimal(object):
    """
    Struct Class

    is the UNO representation of the Automation type DECIMAL.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API Decimal <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1bridge_1_1oleautomation_1_1Decimal.html>`_
    """
    typeName: Literal['com.sun.star.bridge.oleautomation.Decimal']

    def __init__(self, Scale: typing.Optional[int] = ..., Sign: typing.Optional[int] = ..., LowValue: typing.Optional[int] = ..., MiddleValue: typing.Optional[int] = ..., HighValue: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Scale (int, optional): Scale value.
            Sign (int, optional): Sign value.
            LowValue (int, optional): LowValue value.
            MiddleValue (int, optional): MiddleValue value.
            HighValue (int, optional): HighValue value.
        """
        ...


    @property
    def Scale(self) -> int:
        """
        corresponds to DECIMAL.scale.
        """
        ...

    @Scale.setter
    def Scale(self, value: int) -> None:
        ...

    @property
    def Sign(self) -> int:
        """
        corresponds to DECIMAL.sign.
        """
        ...

    @Sign.setter
    def Sign(self, value: int) -> None:
        ...

    @property
    def LowValue(self) -> int:
        """
        corresponds to DECIMAL.Lo32.
        """
        ...

    @LowValue.setter
    def LowValue(self, value: int) -> None:
        ...

    @property
    def MiddleValue(self) -> int:
        """
        corresponds to DECIMAL.Mid32.
        """
        ...

    @MiddleValue.setter
    def MiddleValue(self, value: int) -> None:
        ...

    @property
    def HighValue(self) -> int:
        """
        corresponds to DECIMAL.Hi32.
        """
        ...

    @HighValue.setter
    def HighValue(self, value: int) -> None:
        ...

