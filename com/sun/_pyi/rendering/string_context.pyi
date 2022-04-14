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
# Namespace: com.sun.star.rendering
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class StringContext(object):
    """
    Struct Class

    Collection of string-related arguments used on all canvas text interfaces.
    
    A possibly much larger string than later rendered is necessary here, because in several languages, glyph selection is context dependent.
    
    **since**
    
        OOo 2.0

    See Also:
        `API StringContext <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1StringContext.html>`_
    """
    typeName: Literal['com.sun.star.rendering.StringContext']

    def __init__(self, Text: typing.Optional[str] = ..., StartPosition: typing.Optional[int] = ..., Length: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Text (str, optional): Text value.
            StartPosition (int, optional): StartPosition value.
            Length (int, optional): Length value.
        """


    @property
    def Text(self) -> str:
        """
        The complete text, from which a subset is selected by the parameters below.
        """


    @property
    def StartPosition(self) -> int:
        """
        Start position within the string.
        
        The first character has index 0.
        """


    @property
    def Length(self) -> int:
        """
        Length of the substring to actually use.
        
        Must be within the range [0,INTMAX].
        """



__all__ = ['StringContext']
