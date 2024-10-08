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
# Namespace: com.sun.star.embed
from __future__ import annotations
import typing

from .x_component_supplier import XComponentSupplier as XComponentSupplier_adb0e64


class XEmbeddedClient(XComponentSupplier_adb0e64):
    """
    represents common functionality for embedded clients.

    See Also:
        `API XEmbeddedClient <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1embed_1_1XEmbeddedClient.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.embed.XEmbeddedClient'

    def saveObject(self) -> None:
        """
        asks client to let the object store itself.

        Raises:
            com.sun.star.embed.ObjectSaveVetoException: ``ObjectSaveVetoException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    def visibilityChanged(self, bVisible: bool) -> None:
        """
        An object can use this method to notify the client when the object outplace window becomes visible or invisible.

        Raises:
            com.sun.star.embed.WrongStateException: ``WrongStateException``
        """
        ...


