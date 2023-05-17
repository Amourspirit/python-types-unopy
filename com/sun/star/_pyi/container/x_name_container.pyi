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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.container
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from .x_name_replace import XNameReplace as XNameReplace_f0900d60


class XNameContainer(XNameReplace_f0900d60):
    """
    This is the generic interface for supporting the insertion and removal of named elements.

    See Also:
        `API XNameContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1container_1_1XNameContainer.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.container.XNameContainer']

    def insertByName(self, aName: str, aElement: typing.Any) -> None:
        """
        inserts the given element at the specified name.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def removeByName(self, Name: str) -> None:
        """
        removes the element with the specified name.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...


