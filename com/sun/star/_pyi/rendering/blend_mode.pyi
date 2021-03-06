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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.rendering
from typing_extensions import Literal


class BlendMode(object):
    """
    Const

    These constants determine some extra ways how the primitive color is combined with the background.
    
    Please refer to the PDF specification for explanations of this constants.

    See Also:
        `API BlendMode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1rendering_1_1BlendMode.html>`_
    """
    NORMAL: Literal[0]
    MULTIPLY: Literal[1]
    SCREEN: Literal[2]
    OVERLAY: Literal[3]
    DARKEN: Literal[4]
    LIGHTEN: Literal[5]
    COLOR_DODGE: Literal[6]
    COLOR_BURN: Literal[7]
    HARD_LIGHT: Literal[8]
    SOFT_LIGHT: Literal[9]
    DIFFERENCE: Literal[10]
    EXCLUSION: Literal[11]
    HUE: Literal[12]
    SATURATION: Literal[13]
    COLOR: Literal[14]
    LUMINOSITY: Literal[15]

