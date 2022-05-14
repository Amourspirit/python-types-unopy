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


class AnimationRepeat(object):
    """
    Const

    This are the possible repeat modes for animations.
    
    These constants determine how the [0,1] parameter range of the animation is driven through, thus defining the possible repeat modes.
    
    **since**
    
        OOo 2.0

    See Also:
        `API AnimationRepeat <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1rendering_1_1AnimationRepeat.html>`_
    """
    ONE_SHOT: Literal[0]
    """
    The [0,1] parameter range is swept through exactly once.
    
    The [0,1] parameter range is swept through exactly once, starting with 0 and ending with 1.
    """
    ONE_SHOT_PINGPONG: Literal[1]
    """
    The [0,1] parameter range is swept through exactly twice.
    
    The [0,1] parameter range is swept through exactly twice, starting with 0, going to 1, and going back to 0. When plotting the value over time, this yields a triangle curve.
    """
    PINGPONG: Literal[2]
    """
    The [0,1] parameter range is swept through infinitely.
    
    The [0,1] parameter range is swept through infinitely, starting with 0, going to 1, and going back to 0, and then starting again. When plotting the value over time, this yields a repeated triangle curve.
    """
    REPEAT: Literal[3]
    """
    The [0,1] parameter range is swept through infinitely.
    
    The [0,1] parameter range is swept through infinitely, starting with 0, going to 1, and starting with 0 again. When plotting the value over time, this yields a repeated saw-tooth curve.
    """

