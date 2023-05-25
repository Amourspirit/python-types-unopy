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
from __future__ import annotations
import typing

from .x_window_peer import XWindowPeer as XWindowPeer_99760ab0
if typing.TYPE_CHECKING:
    from .font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from ..util.color import Color as Color_68e908c5


class XVclWindowPeer(XWindowPeer_99760ab0):
    """
    gives access to the VCL window implementation.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XVclWindowPeer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XVclWindowPeer.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.awt.XVclWindowPeer'

    def enableClipSiblings(self, bClip: bool) -> None:
        """
        enables clipping of sibling windows.
        """
        ...
    def getProperty(self, PropertyName: str) -> typing.Any:
        """
        returns the value of the property with the specified name.
        """
        ...
    def getStyles(self, nType: int, Font: FontDescriptor_bc110c0a, ForegroundColor: Color_68e908c5, BackgroundColor: Color_68e908c5) -> None:
        """
        returns the font, foreground and background color for the specified type.

        * ``Font`` is an out direction argument.
        * ``ForegroundColor`` is an out direction argument.
        * ``BackgroundColor`` is an out direction argument.
        """
        ...
    def isChild(self, Peer: XWindowPeer_99760ab0) -> bool:
        """
        returns TRUE if the window peer is a child, FALSE otherwise.
        """
        ...
    def isDesignMode(self) -> bool:
        """
        returns TRUE if the window peer is in design mode, FALSE otherwise.
        """
        ...
    def setControlFont(self, aFont: FontDescriptor_bc110c0a) -> None:
        """
        sets the control font.
        """
        ...
    def setDesignMode(self, bOn: bool) -> None:
        """
        sets the design mode for use in a design editor.
        """
        ...
    def setForeground(self, Color: Color_68e908c5) -> None:
        """
        sets the foreground color.
        """
        ...
    def setProperty(self, PropertyName: str, Value: typing.Any) -> None:
        """
        sets the value of the property with the specified name.
        """
        ...



