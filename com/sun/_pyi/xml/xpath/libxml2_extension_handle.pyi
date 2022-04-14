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
# Namespace: com.sun.star.xml.xpath
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class Libxml2ExtensionHandle(object):
    """
    Struct Class


    See Also:
        `API Libxml2ExtensionHandle <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1xml_1_1xpath_1_1Libxml2ExtensionHandle.html>`_
    """
    typeName: Literal['com.sun.star.xml.xpath.Libxml2ExtensionHandle']

    def __init__(self, functionLookupFunction: typing.Optional[int] = ..., functionData: typing.Optional[int] = ..., variableLookupFunction: typing.Optional[int] = ..., variableData: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            functionLookupFunction (int, optional): functionLookupFunction value.
            functionData (int, optional): functionData value.
            variableLookupFunction (int, optional): variableLookupFunction value.
            variableData (int, optional): variableData value.
        """


    @property
    def functionLookupFunction(self) -> int:
        ...


    @property
    def functionData(self) -> int:
        ...


    @property
    def variableLookupFunction(self) -> int:
        ...


    @property
    def variableData(self) -> int:
        ...



__all__ = ['Libxml2ExtensionHandle']
