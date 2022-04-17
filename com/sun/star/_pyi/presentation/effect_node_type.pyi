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
# Namespace: com.sun.star.presentation
from typing_extensions import Literal
"""
Const

This constants defines a type for an animation effect node.

This is stored with the name node-type inside the com.sun.star.animations.XAnimationNode.UserData sequence.
This does not manipulate the timing or synchronization. It can be used to quickly identify semantic blocks inside an animation hierarchy.

See Also:
    `API EffectNodeType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1presentation_1_1EffectNodeType.html>`_
"""
DEFAULT: Literal[0]
"""
This node has no special meaning.
"""
ON_CLICK: Literal[1]
"""
This node contains an effect that starts on click.
"""
WITH_PREVIOUS: Literal[2]
"""
This node contains an effect that starts with a previous effect.
"""
AFTER_PREVIOUS: Literal[3]
"""
This node contains an effect that starts after a previous effect has finished.
"""
MAIN_SEQUENCE: Literal[4]
"""
This is the main sequence for effects that is automatically started.
"""
TIMING_ROOT: Literal[5]
"""
This is the root sequence.
"""
INTERACTIVE_SEQUENCE: Literal[6]
"""
This is a sequence with effects that starts due to user interaction.
"""

