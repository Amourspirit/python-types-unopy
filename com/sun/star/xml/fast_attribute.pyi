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
# Namespace: com.sun.star.xml
# Libre Office Version: 2024.2
import typing


class FastAttribute(object):
    """
    Struct Class

    A struct to keep information of an element's attribute.

    See Also:
        `API FastAttribute <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1xml_1_1FastAttribute.html>`_
    """
    typeName: str = 'com.sun.star.xml.FastAttribute'

    def __init__(self, Token: typing.Optional[int] = ..., Value: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Token (int, optional): Token value.
            Value (str, optional): Value value.
        """
        ...

    @property
    def Token(self) -> int:
        """
        the token corresponding to the attribute
        """
        ...
    @Token.setter
    def Token(self, value: int) -> None:
        ...
    @property
    def Value(self) -> str:
        """
        the attribute value
        """
        ...
    @Value.setter
    def Value(self, value: str) -> None:
        ...

