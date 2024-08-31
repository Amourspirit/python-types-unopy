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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.text
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XNumberingTypeInfo(XInterface_8f010a43):
    """
    provides access to the numbering types that are supported by a component.
    
    To be able to store unknown numbering types in a file format the numbering types correspond to an identifier.

    See Also:
        `API XNumberingTypeInfo <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XNumberingTypeInfo.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.text.XNumberingTypeInfo'

    def getNumberingIdentifier(self, NumberingType: int) -> str:
        """
        returns the corresponding identifier to a numbering type.
        """
        ...
    def getNumberingType(self, NumberingIdentifier: str) -> int:
        """
        returns the corresponding numbering type to an identifier.
        """
        ...
    def getSupportedNumberingTypes(self) -> typing.Tuple[int, ...]:
        """
        returns the numbering type values that are supported by the component.
        """
        ...
    def hasNumberingType(self, NumberingIdentifier: str) -> bool:
        """
        determines whether an identifier is supported.
        """
        ...


