# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.drawing
# Libre Office Version: 7.2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class NormalsKind(Enum):
    """
    Enum

    

    See Also:
        `API NormalsKind <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#a2f040e92a1488875fb14c6ecc377630b>`_
    """
    typeName: str = 'com.sun.star.drawing.NormalsKind'

    FLAT: 'uno.Enum'
    """
    forces one normal per flat part.
    
    With FLAT shading, the faces of the object are rendered in a solid color.
    """
    SPECIFIC: 'uno.Enum'
    """
    does not produce standard normals, but leaves the object-specific ones untouched.
    """
    SPHERE: 'uno.Enum'
    """
    forces normals to think that the object is a sphere.
    
    This value forces projection to wrapping in X and/or Y.
    """

