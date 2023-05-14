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


class Date(object):
    """
    Struct Class

    is the UNO representation of the Automation type DATE.
    
    A DATE could actually be represented as double in UNO and therefore a typedef from double to a date type would do. But a typedef cannot be expressed in all language bindings. In the case where no typedefs are supported the actual type is used. That is, a typedef'd date type would be represented as double in Java. The information that the double is a date type is lost.
    
    When calling Automation objects from UNO the distinction between double and date type is important. Therefore Date is declared as struct.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API Date <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1bridge_1_1oleautomation_1_1Date.html>`_
    """
    typeName: Literal['com.sun.star.bridge.oleautomation.Date']

    def __init__(self, Value: typing.Optional[float] = ...) -> None:
        """
        Constructor

        Arguments:
            Value (float, optional): Value value.
        """
        ...


    @property
    def Value(self) -> float:
        """
        corresponds to the Automation type DATE.
        """
        ...

    @Value.setter
    def Value(self, value: float) -> None:
        ...

