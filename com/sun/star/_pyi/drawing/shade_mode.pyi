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
# Libre Office Version: 7.3
"""
Enum



See Also:
    `API ShadeMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1drawing.html#af49ab4b65513d2c0077f76b2227326e9>`_
"""

DRAFT: object
"""
DRAFT is a special mode which uses a BSP tree and triangle subdivision for displaying.
"""
FLAT: object
"""
forces one normal per flat part.

With FLAT shading, the faces of the object are rendered in a solid color.
"""
PHONG: object
"""
With PHONG shading, the normal itself is interpolated to get more realistic colors and light reflections.
"""
SMOOTH: object
"""
the point is smooth, the first derivation from the curve discussion view.

With SMOOTH shading, the colors of the lit vertices is interpolated.
"""
