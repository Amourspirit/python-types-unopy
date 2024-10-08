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
# Namespace: com.sun.star.beans
# Libre Office Version: 2024.2
import typing


class Optional(object):
    """
    Struct Class

    An optional value of a given type.
    
    This structure is used as the type of interface attributes corresponding to instances of com.sun.star.beans.Property that have the com.sun.star.beans.PropertyAttribute.MAYBEVOID. It might also be useful in other situations, for example as the return type of an interface method.

    See Also:
        `API Optional <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1beans_1_1Optional_3_01T_01_4.html>`_
    """
    typeName: str = 'com.sun.star.beans.Optional'

    def __init__(self, IsPresent: typing.Optional[bool] = ..., Value: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            IsPresent (bool, optional): IsPresent value.
            Value (object, optional): Value value.
        """
        ...

    @property
    def IsPresent(self) -> bool:
        """
        Marks this structure instance as having an actual value.
        """
        ...
    @IsPresent.setter
    def IsPresent(self, value: bool) -> None:
        ...
    @property
    def Value(self) -> object:
        """
        The actual value of this structure instance.
        
        If no actual value is present, a producer of such a structure instance should leave this member defaulted, and a consumer of such a structure instance should ignore the specific value stored in this member.
        """
        ...
    @Value.setter
    def Value(self, value: object) -> None:
        ...

