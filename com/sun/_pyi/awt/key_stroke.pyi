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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class KeyStroke(object):
    """
    Struct Class

    Describes a key stroke for hotkeys etc.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API KeyStroke <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1KeyStroke.html>`_
    """
    typeName: Literal['com.sun.star.awt.KeyStroke']

    def __init__(self, Modifiers: typing.Optional[int] = ..., KeyCode: typing.Optional[int] = ..., KeyChar: typing.Optional[str] = ..., KeyFunc: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Modifiers (int, optional): Modifiers value.
            KeyCode (int, optional): KeyCode value.
            KeyChar (str, optional): KeyChar value.
            KeyFunc (int, optional): KeyFunc value.
        """


    @property
    def Modifiers(self) -> int:
        """
        contains the modifier keys which were pressed while the event occurred.
        
        Zero or more constants from the group com.sun.star.awt.KeyModifier.
        """


    @property
    def KeyCode(self) -> int:
        """
        contains the integer code representing the key of the event.
        
        This is a constant from the constant group com.sun.star.awt.Key.
        """


    @property
    def KeyChar(self) -> str:
        """
        contains the Unicode character generated by this event or 0.
        """


    @property
    def KeyFunc(self) -> int:
        """
        contains the function type of the key event.
        
        This is a constant from the constant group com.sun.star.awt.KeyFunction.
        """



__all__ = ['KeyStroke']
