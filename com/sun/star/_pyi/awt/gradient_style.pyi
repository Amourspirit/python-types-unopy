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
# Namespace: com.sun.star.awt
# Libre Office Version: 7.3
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class GradientStyle(Enum):
    """
    Enum

    

    See Also:
        `API GradientStyle <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt.html#aa6b9d577a1700f29923f49f7b77d165f>`_
    """

    AXIAL: 'uno.Enum'
    """
    specifies an axial gradient.
    """
    ELLIPTICAL: 'uno.Enum'
    """
    specifies an elliptical gradient.
    """
    LINEAR: 'uno.Enum'
    """
    specifies a linear gradient.
    """
    RADIAL: 'uno.Enum'
    """
    specifies a radial gradient.
    """
    RECT: 'uno.Enum'
    """
    specifies a gradient in the shape of a rectangle.
    """
    SQUARE: 'uno.Enum'
    """
    specifies a gradient in the shape of a square.
    """

