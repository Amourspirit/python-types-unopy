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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.awt
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..lang.x_component import XComponent as XComponent_98dc0ab5
if typing.TYPE_CHECKING:
    from .rectangle import Rectangle as Rectangle_84b109e9
    from .x_pointer import XPointer as XPointer_7abe098d
    from .x_toolkit import XToolkit as XToolkit_7adf0992
    from ..util.color import Color as Color_68e908c5


class XWindowPeer(XComponent_98dc0ab5):
    """
    gives access to the actual window implementation on the device.

    See Also:
        `API XWindowPeer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XWindowPeer.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XWindowPeer']

    def getToolkit(self) -> 'XToolkit_7adf0992':
        """
        returns the toolkit which created this object.
        """
        ...
    def invalidate(self, Flags: int) -> None:
        """
        invalidates the whole window with the specified InvalidateStyle.
        """
        ...
    def invalidateRect(self, Rect: 'Rectangle_84b109e9', Flags: int) -> None:
        """
        invalidates a rectangular area of the window with the specified InvalidateStyle.
        """
        ...
    def setBackground(self, Color: 'Color_68e908c5') -> None:
        """
        sets the background color.
        """
        ...
    def setPointer(self, Pointer: 'XPointer_7abe098d') -> None:
        """
        sets the mouse pointer.
        """
        ...


