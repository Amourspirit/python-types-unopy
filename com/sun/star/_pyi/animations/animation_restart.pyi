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
# Libre Office Version: 7.4
# Namespace: com.sun.star.animations
from typing_extensions import Literal


class AnimationRestart(object):
    """
    Const

    defines the restart behavior

    See Also:
        `API AnimationRestart <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1animations_1_1AnimationRestart.html>`_
    """
    DEFAULT: Literal[0]
    """
    The restart behavior for the element is determined by the value of the XTiming.RestartDefault attribute.
    
    This is the default value for the XTiming.Restart attribute.
    """
    INHERIT: Literal[0]
    """
    Specifies that the value of this attribute (and of the restart behavior) are inherited from the XTiming.RestartDefault value of the parent element.
    
    If there is no parent element, the value is AnimationRestart.ALWAYS. This is the default value for the XTiming.RestartDefault attribute.
    """
    ALWAYS: Literal[1]
    """
    The element can be restarted at any time.
    """
    WHEN_NOT_ACTIVE: Literal[2]
    """
    The element can only be restarted when it is not active (i.e.
    
    it can be restarted after the active end). Attempts to restart the element during its active duration are ignored.
    """
    NEVER: Literal[3]
    """
    The element cannot be restarted for the remainder of the current simple duration of the parent time container.
    """

