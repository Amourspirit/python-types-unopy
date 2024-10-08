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
# Namespace: com.sun.star.lang
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XTypeProvider(XInterface_8f010a43):
    """
    interface to get information about the types (usually interface types) supported by an object.

    See Also:
        `API XTypeProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1lang_1_1XTypeProvider.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.lang.XTypeProvider'

    def getImplementationId(self) -> typing.Tuple[int, ...]:
        """
        Obsolete unique identifier.
        
        Originally returned a sequence of bytes which, when non-empty, was used as an ID to distinguish unambiguously between two sets of types, for example to realise hashing functionality when the object is introspected. Two objects that returned the same non-empty ID had to return the same set of types in getTypes(). (If a unique ID could not be provided, this method was always allowed to return an empty sequence, though).
        """
        ...
    def getTypes(self) -> typing.Tuple[object, ...]:
        """
        returns a sequence of all types (usually interface types) provided by the object.
        """
        ...


