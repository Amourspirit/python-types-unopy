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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.mozilla
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class MenuMultipleChange(object):
    """
    Struct Class

    Explains properties of a menu item.

    See Also:
        `API MenuMultipleChange <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1mozilla_1_1MenuMultipleChange.html>`_
    """
    typeName: Literal['com.sun.star.mozilla.MenuMultipleChange']

    def __init__(self, Image: typing.Optional[typing.Tuple[int, ...]] = ..., ID: typing.Optional[int] = ..., GroupID: typing.Optional[int] = ..., PreItemID: typing.Optional[int] = ..., ItemText: typing.Optional[str] = ..., IsVisible: typing.Optional[bool] = ..., IsActive: typing.Optional[bool] = ..., IsCheckable: typing.Optional[bool] = ..., IsChecked: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            Image (typing.Tuple[int, ...], optional): Image value.
            ID (int, optional): ID value.
            GroupID (int, optional): GroupID value.
            PreItemID (int, optional): PreItemID value.
            ItemText (str, optional): ItemText value.
            IsVisible (bool, optional): IsVisible value.
            IsActive (bool, optional): IsActive value.
            IsCheckable (bool, optional): IsCheckable value.
            IsChecked (bool, optional): IsChecked value.
        """


    @property
    def Image(self) -> typing.Tuple[int, ...]:
        """
        sequence of bytes representing a possible image
        """


    @property
    def ID(self) -> int:
        """
        unique ID of this menu item
        """


    @property
    def GroupID(self) -> int:
        """
        unique ID of the group this menu item belongs to
        """


    @property
    def PreItemID(self) -> int:
        """
        unique ID of the item directly above this menu item, used for fuzzy placement
        """


    @property
    def ItemText(self) -> str:
        """
        text of the menu item
        """


    @property
    def IsVisible(self) -> bool:
        """
        true if visible
        """


    @property
    def IsActive(self) -> bool:
        """
        true if active, so clickable
        """


    @property
    def IsCheckable(self) -> bool:
        """
        true if checkable, so there can be a checkmark
        """


    @property
    def IsChecked(self) -> bool:
        """
        true if there is a checkmark
        """



__all__ = ['MenuMultipleChange']
