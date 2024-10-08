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
# Namespace: com.sun.star.util
# Libre Office Version: 2024.2
import typing
from .sort_field_type import SortFieldType as SortFieldType_bd500bf4


class SortField(object):
    """
    Struct Class

    describes a single field in a sort descriptor.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API SortField <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1SortField.html>`_
    """
    typeName: str = 'com.sun.star.util.SortField'

    def __init__(self, Field: typing.Optional[int] = ..., SortAscending: typing.Optional[bool] = ..., FieldType: typing.Optional[SortFieldType_bd500bf4] = ...) -> None:
        """
        Constructor

        Arguments:
            Field (int, optional): Field value.
            SortAscending (bool, optional): SortAscending value.
            FieldType (SortFieldType, optional): FieldType value.
        """
        ...

    @property
    def Field(self) -> int:
        """
        index of the field in the table; 0-based.
        """
        ...
    @Field.setter
    def Field(self, value: int) -> None:
        ...
    @property
    def SortAscending(self) -> bool:
        """
        TRUE if data are sorted in ascending order, FALSE if in descending order.
        """
        ...
    @SortAscending.setter
    def SortAscending(self, value: bool) -> None:
        ...
    @property
    def FieldType(self) -> SortFieldType_bd500bf4:
        """
        type of contents in the field.
        """
        ...
    @FieldType.setter
    def FieldType(self, value: SortFieldType_bd500bf4) -> None:
        ...

