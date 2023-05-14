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
# Namespace: com.sun.star.document
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class CmisProperty(object):
    """
    Struct Class

    specifies a CMIS property.

    See Also:
        `API CmisProperty <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1document_1_1CmisProperty.html>`_
    """
    typeName: Literal['com.sun.star.document.CmisProperty']

    def __init__(self, Id: typing.Optional[str] = ..., Name: typing.Optional[str] = ..., Type: typing.Optional[str] = ..., Updatable: typing.Optional[bool] = ..., Required: typing.Optional[bool] = ..., MultiValued: typing.Optional[bool] = ..., OpenChoice: typing.Optional[bool] = ..., Choices: typing.Optional[object] = ..., Value: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            Id (str, optional): Id value.
            Name (str, optional): Name value.
            Type (str, optional): Type value.
            Updatable (bool, optional): Updatable value.
            Required (bool, optional): Required value.
            MultiValued (bool, optional): MultiValued value.
            OpenChoice (bool, optional): OpenChoice value.
            Choices (object, optional): Choices value.
            Value (object, optional): Value value.
        """
        ...


    @property
    def Id(self) -> str:
        """
        unique ID of the Cmis property
        """
        ...

    @Id.setter
    def Id(self, value: str) -> None:
        ...

    @property
    def Name(self) -> str:
        """
        specifies the display name of the CMIS property.
        """
        ...

    @Name.setter
    def Name(self, value: str) -> None:
        ...

    @property
    def Type(self) -> str:
        """
        type of the property
        """
        ...

    @Type.setter
    def Type(self, value: str) -> None:
        ...

    @property
    def Updatable(self) -> bool:
        """
        specifies if the property is updatable.
        """
        ...

    @Updatable.setter
    def Updatable(self, value: bool) -> None:
        ...

    @property
    def Required(self) -> bool:
        """
        specifies if the property is required and can not be empty.
        """
        ...

    @Required.setter
    def Required(self, value: bool) -> None:
        ...

    @property
    def MultiValued(self) -> bool:
        """
        specifies if the property has multiple value
        """
        ...

    @MultiValued.setter
    def MultiValued(self, value: bool) -> None:
        ...

    @property
    def OpenChoice(self) -> bool:
        """
        specifies if the property value can be freely set or is restricted from a list of choices.
        """
        ...

    @OpenChoice.setter
    def OpenChoice(self, value: bool) -> None:
        ...

    @property
    def Choices(self) -> object:
        """
        specifies the possible choices of the values.
        """
        ...

    @Choices.setter
    def Choices(self, value: object) -> None:
        ...

    @property
    def Value(self) -> object:
        """
        specifies value of the property
        """
        ...

    @Value.setter
    def Value(self, value: object) -> None:
        ...

