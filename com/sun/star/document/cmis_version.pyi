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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.document
# Libre Office Version: 2024.2
import typing


class CmisVersion(object):
    """
    Struct Class

    specifies a CMIS document version.

    See Also:
        `API CmisVersion <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1document_1_1CmisVersion.html>`_
    """
    typeName: str = 'com.sun.star.document.CmisVersion'

    def __init__(self, Id: typing.Optional[str] = ..., TimeStamp: typing.Optional[object] = ..., Author: typing.Optional[str] = ..., Comment: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Id (str, optional): Id value.
            TimeStamp (object, optional): TimeStamp value.
            Author (str, optional): Author value.
            Comment (str, optional): Comment value.
        """
        ...

    @property
    def Id(self) -> str:
        """
        unique ID of the Cmis version
        """
        ...
    @Id.setter
    def Id(self, value: str) -> None:
        ...
    @property
    def TimeStamp(self) -> object:
        """
        specifies the time when the revision was created.
        """
        ...
    @TimeStamp.setter
    def TimeStamp(self, value: object) -> None:
        ...
    @property
    def Author(self) -> str:
        """
        contains the author that created the version.
        """
        ...
    @Author.setter
    def Author(self, value: str) -> None:
        ...
    @property
    def Comment(self) -> str:
        """
        contains the comment the author has left.
        """
        ...
    @Comment.setter
    def Comment(self, value: str) -> None:
        ...

