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
# Namespace: com.sun.star.ucb
# Libre Office Version: 2024.2
from typing_extensions import Literal
import typing
from .authentication_request import AuthenticationRequest as AuthenticationRequest_1b520eeb
from ..uno.x_interface import XInterface as XInterface_8f010a43
from ..task.interaction_classification import InteractionClassification as InteractionClassification_6c4d10e7

class URLAuthenticationRequest(AuthenticationRequest_1b520eeb):
    """
    Exception Class

    An error specifying lack of correct authentication data (e.g., to log into an account).
    
    **since**
    
        OOo 3.2

    See Also:
        `API URLAuthenticationRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1URLAuthenticationRequest.html>`_
    """

    typeName: Literal['com.sun.star.ucb.URLAuthenticationRequest']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., Classification: typing.Optional[InteractionClassification_6c4d10e7] = ..., ServerName: typing.Optional[str] = ..., Diagnostic: typing.Optional[str] = ..., HasRealm: typing.Optional[bool] = ..., Realm: typing.Optional[str] = ..., HasUserName: typing.Optional[bool] = ..., UserName: typing.Optional[str] = ..., HasPassword: typing.Optional[bool] = ..., Password: typing.Optional[str] = ..., HasAccount: typing.Optional[bool] = ..., Account: typing.Optional[str] = ..., URL: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Classification (InteractionClassification, optional): Classification value.
            ServerName (str, optional): ServerName value.
            Diagnostic (str, optional): Diagnostic value.
            HasRealm (bool, optional): HasRealm value.
            Realm (str, optional): Realm value.
            HasUserName (bool, optional): HasUserName value.
            UserName (str, optional): UserName value.
            HasPassword (bool, optional): HasPassword value.
            Password (str, optional): Password value.
            HasAccount (bool, optional): HasAccount value.
            Account (str, optional): Account value.
            URL (str, optional): URL value.
        """
        ...
    @property
    def URL(self) -> str:
        """
        The URL for which authentication is requested.
        """
        ...
    @URL.setter
    def URL(self, value: str) -> None:
        ...

__all__ = ['URLAuthenticationRequest']

