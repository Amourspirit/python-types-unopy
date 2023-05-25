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
from __future__ import annotations
import typing

from .x_type_description import XTypeDescription as XTypeDescription_3c210fb1
if typing.TYPE_CHECKING:
    from .x_constant_type_description import XConstantTypeDescription as XConstantTypeDescription_c80612fb


class XConstantsTypeDescription(XTypeDescription_3c210fb1):
    """
    Reflects a constants group.
    
    The type class of this type is com.sun.star.uno.TypeClass.CONSTANTS.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XConstantsTypeDescription <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1reflection_1_1XConstantsTypeDescription.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.reflection.XConstantsTypeDescription'

    def getConstants(self) -> typing.Tuple[XConstantTypeDescription_c80612fb, ...]:
        """
        Returns the constants defined for this constants group.
        """
        ...


