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
# Namespace: com.sun.star.sdbc
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class SQLException(Exception_85530a09):
    """
    Exception Class

    is an exception that provides information on a database access error.
    
    Each com.sun.star.sdbc.SQLException provides several kinds of information:

    See Also:
        `API SQLException <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1sdbc_1_1SQLException.html>`_
    """

    typeName: Literal['com.sun.star.sdbc.SQLException']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., SQLState: typing.Optional[str] = ..., ErrorCode: typing.Optional[int] = ..., NextException: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            SQLState (str, optional): SQLState value.
            ErrorCode (int, optional): ErrorCode value.
            NextException (object, optional): NextException value.
        """
        ...
    @property
    def SQLState(self) -> str:
        """
        returns a string, which uses the XOPEN SQLState conventions.
        
        The values of the SQLState string are described in the XOPEN SQL spec.
        """
        ...

    @property
    def ErrorCode(self) -> int:
        """
        returns an integer error code that is specific to each vendor.
        
        Normally this will be the actual error code returned by the underlying database.
        """
        ...

    @property
    def NextException(self) -> object:
        """
        returns a chain to the next Exception.
        
        This can be used to provide additional error information.
        """
        ...


__all__ = ['SQLException']

