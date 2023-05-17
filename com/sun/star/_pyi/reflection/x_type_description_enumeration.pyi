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
# Namespace: com.sun.star.reflection
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..container.x_enumeration import XEnumeration as XEnumeration_f2180daa
if typing.TYPE_CHECKING:
    from .x_type_description import XTypeDescription as XTypeDescription_3c210fb1


class XTypeDescriptionEnumeration(XEnumeration_f2180daa):
    """
    Defines an enumeration for type descriptions.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XTypeDescriptionEnumeration <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XTypeDescriptionEnumeration.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.reflection.XTypeDescriptionEnumeration']

    def nextTypeDescription(self) -> 'XTypeDescription_3c210fb1':
        """
        Returns the next element of the enumeration.

        Raises:
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...


