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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.task
# Libre Office Version: 2024.2
from typing_extensions import Literal
import typing
from .error_code_request import ErrorCodeRequest as ErrorCodeRequest_e22d0d29
from ..uno.x_interface import XInterface as XInterface_8f010a43

class ErrorCodeRequest2(ErrorCodeRequest_e22d0d29):
    """
    Exception Class

    represents a general error exception.
    
    It can be used to transport the error code information. E.g. that can be useful for interactions.
    
    This is designed to mesh with tools.ErrCodeMsg
    
    **since**
    
        LibreOffice 24.2

    See Also:
        `API ErrorCodeRequest2 <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1task_1_1ErrorCodeRequest2.html>`_
    """

    typeName: Literal['com.sun.star.task.ErrorCodeRequest2']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., ErrCode: typing.Optional[int] = ..., Arg1: typing.Optional[str] = ..., Arg2: typing.Optional[str] = ..., DialogMask: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            ErrCode (int, optional): ErrCode value.
            Arg1 (str, optional): Arg1 value.
            Arg2 (str, optional): Arg2 value.
            DialogMask (int, optional): DialogMask value.
        """
        ...
    @property
    def Arg1(self) -> str:
        """
        """
        ...
    @Arg1.setter
    def Arg1(self, value: str) -> None:
        ...
    @property
    def Arg2(self) -> str:
        """
        """
        ...
    @Arg2.setter
    def Arg2(self, value: str) -> None:
        ...
    @property
    def DialogMask(self) -> int:
        """
        """
        ...
    @DialogMask.setter
    def DialogMask(self, value: int) -> None:
        ...

__all__ = ['ErrorCodeRequest2']

