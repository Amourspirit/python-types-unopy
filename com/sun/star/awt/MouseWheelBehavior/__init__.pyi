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
# Namespace: com.sun.star.awt
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
"""
Const

describes the scroll behavior of the mouse wheel for a control

**since**

    OOo 3.2

See Also:
    `API MouseWheelBehavior <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1awt_1_1MouseWheelBehavior.html>`_
"""
SCROLL_DISABLED: Literal[0]
"""
defines that the mouse wheel cannot be used to scroll through the control's content
"""
SCROLL_FOCUS_ONLY: Literal[1]
"""
defines that the mouse can only be used to scroll through the control's content if it currently has the focus.
"""
SCROLL_ALWAYS: Literal[2]
"""
defines that the mouse can be used to scroll through the control's content, no matter whether or not it has the focus, as long as the mouse pointer is over the control.
"""

