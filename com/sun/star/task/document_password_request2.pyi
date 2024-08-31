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
from .document_password_request import DocumentPasswordRequest as DocumentPasswordRequest_4bb71036
from ..uno.x_interface import XInterface as XInterface_8f010a43
from .interaction_classification import InteractionClassification as InteractionClassification_6c4d10e7
from .password_request_mode import PasswordRequestMode as PasswordRequestMode_ec10e7c

class DocumentPasswordRequest2(DocumentPasswordRequest_4bb71036):
    """
    Exception Class

    this request specifies if a password for opening or modifying a document is requested.
    
    It is supported by InteractionHandler service, and can be used to interact for a document password. Continuations for using with the mentioned service are Abort and Approve.
    
    **since**
    
        OOo 3.3

    See Also:
        `API DocumentPasswordRequest2 <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1task_1_1DocumentPasswordRequest2.html>`_
    """

    typeName: Literal['com.sun.star.task.DocumentPasswordRequest2']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., Classification: typing.Optional[InteractionClassification_6c4d10e7] = ..., Mode: typing.Optional[PasswordRequestMode_ec10e7c] = ..., Name: typing.Optional[str] = ..., IsRequestPasswordToModify: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Classification (InteractionClassification, optional): Classification value.
            Mode (PasswordRequestMode, optional): Mode value.
            Name (str, optional): Name value.
            IsRequestPasswordToModify (bool, optional): IsRequestPasswordToModify value.
        """
        ...
    @property
    def IsRequestPasswordToModify(self) -> bool:
        """
        specifies if the requested password is for opening a document or for modifying it.
        """
        ...
    @IsRequestPasswordToModify.setter
    def IsRequestPasswordToModify(self, value: bool) -> None:
        ...

__all__ = ['DocumentPasswordRequest2']

