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
# Namespace: com.sun.star.xml
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class AttributeData(object):
    """
    Struct Class

    store the type and value of an XML attribute inside a XNameContainer

    See Also:
        `API AttributeData <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1xml_1_1AttributeData.html>`_
    """
    typeName: Literal['com.sun.star.xml.AttributeData']

    def __init__(self, Namespace: typing.Optional[str] = ..., Type: typing.Optional[str] = ..., Value: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Namespace (str, optional): Namespace value.
            Type (str, optional): Type value.
            Value (str, optional): Value value.
        """
        ...


    @property
    def Namespace(self) -> str:
        """
        the namespace of this XML attribute.
        
        This string can be empty if you are not using namespaces.
        """
        ...


    @property
    def Type(self) -> str:
        """
        the type of this XML attribute.
        
        For non validating parsers this must be CDATA.
        """
        ...


    @property
    def Value(self) -> str:
        """
        the string value of this XML attribute.
        """
        ...


