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
# Const Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.drawing
from typing_extensions import Literal


class EnhancedCustomShapeGluePointType:
    """
    Const Class

    defines which glue points are being offered by the EnhancedCustomShape

    See Also:
        `API EnhancedCustomShapeGluePointType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing_1_1EnhancedCustomShapeGluePointType.html>`_
    """
    NONE: Literal[0]
    """
    no glue points are offered
    """
    SEGMENTS: Literal[1]
    """
    glue points are offered for each segment
    """
    CUSTOM: Literal[2]
    """
    only glue points of the GluePoints property from the com.sun:star.drawing.EnhancedCustomShapePath are offered
    """
    RECT: Literal[3]
    """
    standard top, left, right, bottom glue points are offered
    """

__all__ = ['EnhancedCustomShapeGluePointType']
