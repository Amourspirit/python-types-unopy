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
# Namespace: com.sun.star.reflection
from __future__ import annotations
import typing

from .x_compound_type_description import XCompoundTypeDescription as XCompoundTypeDescription_c7be12f6
if typing.TYPE_CHECKING:
    from .x_type_description import XTypeDescription as XTypeDescription_3c210fb1


class XStructTypeDescription(XCompoundTypeDescription_c7be12f6):
    """
    Reflects a struct type, supporting polymorphic struct types.
    
    This type supersedes XCompoundTypeDescription, which only supports plain struct types.
    
    This type is used to reflect all of the following:
    
    **since**
    
        OOo 2.0

    See Also:
        `API XStructTypeDescription <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XStructTypeDescription.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.reflection.XStructTypeDescription'

    def getTypeArguments(self) -> typing.Tuple[XTypeDescription_3c210fb1, ...]:
        """
        Returns the type arguments of an instantiated polymorphic struct type.
        """
        ...
    def getTypeParameters(self) -> typing.Tuple[str, ...]:
        """
        Returns the type parameters of a polymorphic struct type template.
        """
        ...


