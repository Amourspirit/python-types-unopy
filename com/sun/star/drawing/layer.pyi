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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.drawing
from __future__ import annotations
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class Layer(XPropertySet_bc180bfa):
    """
    Service Class

    A layer is an entity inside a document which contains shapes.
    
    There could be zero or more Shapes attached to such a layer.
    
    The properties of a Layer instance affect all Shapes attached to the Layer.

    See Also:
        `API Layer <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1Layer.html>`_
    """
    @property
    def IsLocked(self) -> bool:
        """
        If a Layer is locked, the objects in this Layer cannot be edited in the user interface.
        """
        ...
    @IsLocked.setter
    def IsLocked(self, value: bool) -> None:
        ...
    @property
    def IsPrintable(self) -> bool:
        """
        If a Layer is not printable, the objects in this Layer are not printed.
        """
        ...
    @IsPrintable.setter
    def IsPrintable(self, value: bool) -> None:
        ...
    @property
    def IsVisible(self) -> bool:
        """
        If a Layer is not visible, the objects in this Layer are not shown in the user interface.
        """
        ...
    @IsVisible.setter
    def IsVisible(self, value: bool) -> None:
        ...
    @property
    def Name(self) -> str:
        """
        The name of a Layer is used to identify the Layer in the user interface.
        """
        ...
    @Name.setter
    def Name(self, value: str) -> None:
        ...

