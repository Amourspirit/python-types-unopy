# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
"""
Const


See Also:
    `API AnimationEndSync <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1animations_1_1AnimationEndSync.html>`_
"""
FIRST: Literal[0]
"""
The par, excl, or media element's implicit duration ends with the earliest active end of all the child elements.

This does not refer to the lexical first child, or to the first child to start, but rather refers to the first child to end its (first) active duration.
"""
LAST: Literal[1]
"""
The par, excl, or media element's implicit duration ends with the last active end of the child elements.

This does not refer to the lexical last child, or to the last child to start, but rather refers to the last active end of all children that have a resolved, definite begin time. If the time container has no children with a resolved begin time, the time container ends immediately. If child elements have multiple begin times, or otherwise restart, the child elements must complete all instances of active durations for resolved begin times. This is the default value for par and excl elements.
"""
ALL: Literal[2]
"""
The par, excl, or media element's implicit duration ends when all of the child elements have ended their respective active durations.

Elements with indefinite or unresolved begin times will keep the simple duration of the time container from ending. When all elements have completed the active duration one or more times, the parent time container can end.
"""
MEDIA: Literal[3]
"""
The time container element's implicit duration ends when the intrinsic media duration of the element ends.

This must be defined by a host language. If the time container element does not define an intrinsic media duration, the host language must define the simple duration for the element. This is the default value for media time container elements.
"""

