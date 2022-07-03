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
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class ExternalLinkInfo(object):
    """
    Struct Class

    describes an external link in a formula.
    
    **since**
    
        OOo 3.1

    See Also:
        `API ExternalLinkInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1ExternalLinkInfo.html>`_
    """
    typeName: Literal['com.sun.star.sheet.ExternalLinkInfo']

    def __init__(self, Type: typing.Optional[int] = ..., Data: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Type (int, optional): Type value.
            Data (object, optional): Data value.
        """
        ...


    @property
    def Type(self) -> int:
        """
        Link type, one of ExternalLinkType constants.
        """
        ...


    @property
    def Data(self) -> object:
        """
        Location of this link type.
        
        Modes used:
        """
        ...


