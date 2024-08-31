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
from ..accessibility.x_accessible_image import XAccessibleImage as XAccessibleImage_6bc11099
from .accessible_shape import AccessibleShape as AccessibleShape_fdd20dd3

class AccessibleGraphicShape(AccessibleShape_fdd20dd3, XAccessibleImage_6bc11099):
    """
    Service Class

    The AccessibleGraphicShape service is implemented by the graphic object shapes shapes com.sun.star.drawing.GraphicObjectShape and com.sun.star.presentation.GraphicObjectShape.
    
    It differs from the included AccessibleShape \"base\" service by the additional support of the com.sun.star.accessibility.XAccessibleImage interface.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API AccessibleGraphicShape <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1drawing_1_1AccessibleGraphicShape.html>`_
    """
    ...

