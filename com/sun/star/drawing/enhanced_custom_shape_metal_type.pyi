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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.drawing
import typing


class EnhancedCustomShapeMetalType:
    """
    Const

    These constants define the way the attribute Metal of service EnhancedCustomShapeExtrusion is interpreted for rendering the shape.
    
    **since**
    
        LibreOffice 7.4

    See Also:
        `API EnhancedCustomShapeMetalType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing_1_1EnhancedCustomShapeMetalType.html>`_
    """
    MetalODF: int = ...
    """
    The rendering of the shape is modified as specified in the ODF standard.
    """
    MetalMSCompatible: int = ...
    """
    The rendering of the shape is modified to get a similar rendering as in Microsoft Office for objects, which have the fc3DMetallic flag in Rich Text Format or binary MS Office format set.
    """

