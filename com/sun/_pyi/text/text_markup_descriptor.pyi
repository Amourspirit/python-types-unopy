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
# Namespace: com.sun.star.text
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing
from ..container.x_string_key_map import XStringKeyMap as XStringKeyMap_ffc60de1


class TextMarkupDescriptor(object):
    """
    Struct Class

    A descriptor for a single text markup.
    
    **since**
    
        OOo 3.0.1

    See Also:
        `API TextMarkupDescriptor <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1text_1_1TextMarkupDescriptor.html>`_
    """
    typeName: Literal['com.sun.star.text.TextMarkupDescriptor']

    def __init__(self, nType: typing.Optional[int] = ..., aIdentifier: typing.Optional[str] = ..., nOffset: typing.Optional[int] = ..., nLength: typing.Optional[int] = ..., xMarkupInfoContainer: typing.Optional[XStringKeyMap_ffc60de1] = ...) -> None:
        """
        Constructor

        Arguments:
            nType (int, optional): nType value.
            aIdentifier (str, optional): aIdentifier value.
            nOffset (int, optional): nOffset value.
            nLength (int, optional): nLength value.
            xMarkupInfoContainer (XStringKeyMap, optional): xMarkupInfoContainer value.
        """


    @property
    def nType(self) -> int:
        """
        Type of text markup see TextMarkupType.
        """


    @property
    def aIdentifier(self) -> str:
        """
        A string used to identify the caller.
        """


    @property
    def nOffset(self) -> int:
        """
        Start of the markup range.
        """


    @property
    def nLength(self) -> int:
        """
        Length of the markup range.
        """


    @property
    def xMarkupInfoContainer(self) -> XStringKeyMap_ffc60de1:
        """
        contains additional information about the markup
        
        Supported properties:
        
        |
        
        **since**
        
            6.3: BOLDWAVE, BOLD | See: com::sun::star::awt::FontUnderline
        """



__all__ = ['TextMarkupDescriptor']
