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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.uno
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from .x_interface import XInterface as XInterface_8f010a43
from builtins import Exception as BException


class Exception(BException):
    """
    Exception Class

    the base of all UNO exceptions
    
    All exceptions defined in UNO idl should derive from this exception.

    See Also:
        `API Exception <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1uno_1_1Exception.html>`_
    """

    typeName: Literal['com.sun.star.uno.Exception']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
        """
        ...
    @property
    def Message(self) -> str:
        """
        gives a detailed description of the reason, why the exception was thrown.
        
        The description should be as detailed as possible.
        """
        ...

    @property
    def Context(self) -> XInterface_8f010a43:
        """
        should contain a reference to the original, which raised the exception.
        
        May be NULL.
        """
        ...


__all__ = ['Exception']

