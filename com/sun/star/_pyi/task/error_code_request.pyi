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
# Namespace: com.sun.star.task
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing
from ..uno.exception import Exception as Exception_85530a09
from ..uno.x_interface import XInterface as XInterface_8f010a43

class ErrorCodeRequest(Exception_85530a09):
    """
    Exception Class

    represents a general error exception.
    
    It can be used to transport the error code information. E.g. that can be useful for interactions.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API ErrorCodeRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1task_1_1ErrorCodeRequest.html>`_
    """

    typeName: Literal['com.sun.star.task.ErrorCodeRequest']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., ErrCode: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            ErrCode (int, optional): ErrCode value.
        """
        ...
    @property
    def ErrCode(self) -> int:
        """
        specifies the error code.
        """
        ...


__all__ = ['ErrorCodeRequest']

