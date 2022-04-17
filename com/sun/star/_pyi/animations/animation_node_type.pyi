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
# Namespace: com.sun.star.animations
from typing_extensions import Literal
"""
Const

This constants defines a type for an animation node.

It can be used to quickly identify semantic blocks inside an animation hierarchy.

**since**

    LibreOffice 7.1

See Also:
    `API AnimationNodeType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1animations_1_1AnimationNodeType.html>`_
"""
CUSTOM: Literal[0]
"""
Defines a custom time node.
"""
PAR: Literal[1]
"""
Defines a parallel time container.
"""
SEQ: Literal[2]
"""
Defines a sequence time container.
"""
ITERATE: Literal[3]
"""
Defines an iterate time container.
"""
ANIMATE: Literal[4]
"""
Defines a generic attribute animation.
"""
SET: Literal[5]
"""
Defines a simple mean of just setting the value of an attribute for a specified duration.
"""
ANIMATEMOTION: Literal[6]
"""
Defines a move animation along a path.
"""
ANIMATECOLOR: Literal[7]
"""
Defines an animation of a color attribute.
"""
ANIMATETRANSFORM: Literal[8]
"""
Defines an animation of a transformation attribute.
"""
TRANSITIONFILTER: Literal[9]
"""
Defines an animation of a filter behavior.
"""
AUDIO: Literal[10]
"""
Defines an audio effect.
"""
COMMAND: Literal[11]
"""
Defines a command effect.
"""
ANIMATEPHYSICS: Literal[12]
"""
Defines a physics animation.

**since**

    LibreOffice 7.1
"""

