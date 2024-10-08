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
# Namespace: com.sun.star.mozilla
# Libre Office Version: 2024.2
import typing


class MenuSingleChange(object):
    """
    Struct Class

    Explains a change for a menu item.

    See Also:
        `API MenuSingleChange <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1mozilla_1_1MenuSingleChange.html>`_
    """
    typeName: str = 'com.sun.star.mozilla.MenuSingleChange'

    def __init__(self, ID: typing.Optional[int] = ..., ChangeID: typing.Optional[int] = ..., Change: typing.Optional[object] = ...) -> None:
        """
        Constructor

        Arguments:
            ID (int, optional): ID value.
            ChangeID (int, optional): ChangeID value.
            Change (object, optional): Change value.
        """
        ...

    @property
    def ID(self) -> int:
        """
        unique ID of this menu item
        """
        ...
    @ID.setter
    def ID(self, value: int) -> None:
        ...
    @property
    def ChangeID(self) -> int:
        """
        ID identifying the type of change in the any type change.
        """
        ...
    @ChangeID.setter
    def ChangeID(self, value: int) -> None:
        ...
    @property
    def Change(self) -> object:
        """
        value of change
        """
        ...
    @Change.setter
    def Change(self, value: object) -> None:
        ...

