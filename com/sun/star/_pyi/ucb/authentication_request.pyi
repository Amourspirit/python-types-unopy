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
# Namespace: com.sun.star.ucb
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing
from ..task.classified_interaction_request import ClassifiedInteractionRequest as ClassifiedInteractionRequest_9f72121b
from ..uno.x_interface import XInterface as XInterface_8f010a43
from ..task.interaction_classification import InteractionClassification as InteractionClassification_6c4d10e7

class AuthenticationRequest(ClassifiedInteractionRequest_9f72121b):
    """
    Exception Class

    An error specifying lack of correct authentication data (e.g., to log into an account).

    See Also:
        `API AuthenticationRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1ucb_1_1AuthenticationRequest.html>`_
    """

    typeName: Literal['com.sun.star.ucb.AuthenticationRequest']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., Classification: typing.Optional[InteractionClassification_6c4d10e7] = ..., ServerName: typing.Optional[str] = ..., Diagnostic: typing.Optional[str] = ..., HasRealm: typing.Optional[bool] = ..., Realm: typing.Optional[str] = ..., HasUserName: typing.Optional[bool] = ..., UserName: typing.Optional[str] = ..., HasPassword: typing.Optional[bool] = ..., Password: typing.Optional[str] = ..., HasAccount: typing.Optional[bool] = ..., Account: typing.Optional[str] = ...) -> None:
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
        """
        ...
    @property
    def ServerName(self) -> str:
        """
        The name of the server (if applicable).
        """
        ...

    @property
    def Diagnostic(self) -> str:
        """
        Any diagnostic message about the failure to log in (if applicable; it will typically be an English phrase or sentence).
        """
        ...

    @property
    def HasRealm(self) -> bool:
        """
        Specifies if the authentication involves a \"realm\" (as can be the case for HTTP).
        """
        ...

    @property
    def Realm(self) -> str:
        """
        Any already specified realm.
        
        If HasRealm is false, this member should be ignored.
        """
        ...

    @property
    def HasUserName(self) -> bool:
        """
        Specifies if the authentication involves a \"user name\" (as is almost always the case).
        """
        ...

    @property
    def UserName(self) -> str:
        """
        Any already specified user name.
        
        If HasUserName is false, this member should be ignored.
        """
        ...

    @property
    def HasPassword(self) -> bool:
        """
        Specifies if the authentication involves a \"password\" (as is almost always the case).
        """
        ...

    @property
    def Password(self) -> str:
        """
        Any already specified password.
        
        If HasPassword is false, this member should be ignored.
        """
        ...

    @property
    def HasAccount(self) -> bool:
        """
        Specifies if the authentication involves an \"account\" (as can be the case for FTP).
        """
        ...

    @property
    def Account(self) -> str:
        """
        Any already specified account.
        
        If HasAccount is false, this member should be ignored.
        """
        ...


__all__ = ['AuthenticationRequest']

