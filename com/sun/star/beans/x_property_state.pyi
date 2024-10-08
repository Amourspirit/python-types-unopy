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
# Namespace: com.sun.star.beans
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from com.sun.star.beans.PropertyState import PropertyStateProto  # type: ignore


class XPropertyState(XInterface_8f010a43):
    """
    makes it possible to query information about the state of one or more properties.
    
    The state contains the information if:

    See Also:
        `API XPropertyState <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XPropertyState.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.beans.XPropertyState'

    def getPropertyDefault(self, aPropertyName: str) -> typing.Any:
        """
        If no default exists, is not known or is void, then the return type is void.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def getPropertyState(self, PropertyName: str) -> PropertyStateProto:
        """

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
        """
        ...
    def getPropertyStates(self, aPropertyName: typing.Tuple[str, ...]) -> typing.Tuple[PropertyStateProto, ...]:
        """
        The order of the states is correlating to the order of the given property names.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
        """
        ...
    def setPropertyToDefault(self, PropertyName: str) -> None:
        """
        Sets the property to default value.
        
        The value depends on the implementation of this interface. If it is a bound property, you must change the value before the change events are fired. If it is a constrained property, you must fire the vetoable event before you change the property value.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
        """
        ...
