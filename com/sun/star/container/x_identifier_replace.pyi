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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.container
from __future__ import annotations
import typing

from .x_identifier_access import XIdentifierAccess as XIdentifierAccess_3a5a0f78


class XIdentifierReplace(XIdentifierAccess_3a5a0f78):
    """
    This is the generic interface for supporting the replacement of elements with unique identifiers.

    See Also:
        `API XIdentifierReplace <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1container_1_1XIdentifierReplace.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.container.XIdentifierReplace'

    def replaceByIdentifer(self, Identifier: int, aElement: typing.Any) -> None:
        """
        replaces the element with the specified identifier.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...


