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

from .x_enumeration_access import XEnumerationAccess as XEnumerationAccess_4bac0ffc
if typing.TYPE_CHECKING:
    from .x_component_enumeration import XComponentEnumeration as XComponentEnumeration_7ee3115d


class XComponentEnumerationAccess(XEnumerationAccess_4bac0ffc):
    """
    provides a factory for a typified enumeration through a collection of components.

    See Also:
        `API XComponentEnumerationAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1container_1_1XComponentEnumerationAccess.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.container.XComponentEnumerationAccess'

    def createComponentEnumeration(self) -> XComponentEnumeration_7ee3115d:
        """
        creates a new instance of enumeration through components.
        """
        ...


