# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Namespace: com.sun.star.task
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing
from .user_record import UserRecord as UserRecord_9a2e0ab9


class UrlRecord(object):
    """
    Struct Class


    See Also:
        `API UrlRecord <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1task_1_1UrlRecord.html>`_
    """
    typeName: Literal['com.sun.star.task.UrlRecord']

    def __init__(self, UserList: typing.Optional[typing.Tuple[UserRecord_9a2e0ab9, ...]] = ..., Url: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            UserList (typing.Tuple[UserRecord, ...], optional): UserList value.
            Url (str, optional): Url value.
        """
        ...


    @property
    def UserList(self) -> typing.Tuple[UserRecord_9a2e0ab9, ...]:
        ...

    @UserList.setter
    def UserList(self, value: typing.Tuple[UserRecord_9a2e0ab9, ...]) -> None:
        ...

    @property
    def Url(self) -> str:
        """
        The URL for which these passwords where given.
        """
        ...

    @Url.setter
    def Url(self, value: str) -> None:
        ...

