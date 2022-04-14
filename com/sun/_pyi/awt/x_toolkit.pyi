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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.awt
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .rectangle import Rectangle as Rectangle_84b109e9
    from .window_descriptor import WindowDescriptor as WindowDescriptor_d61e0ceb
    from .x_device import XDevice as XDevice_70ba08fc
    from .x_region import XRegion as XRegion_70f30910
    from .x_window_peer import XWindowPeer as XWindowPeer_99760ab0

class XToolkit(XInterface_8f010a43):
    """
    specifies a factory interface for the window toolkit.
    
    This is similar to the abstract window toolkit (AWT) in Java.

    See Also:
        `API XToolkit <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XToolkit.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XToolkit']

    def createRegion(self) -> 'XRegion_70f30910':
        """
        creates a region.
        """
    def createScreenCompatibleDevice(self, Width: int, Height: int) -> 'XDevice_70ba08fc':
        """
        creates a virtual device that is compatible with the screen.
        """
    def createWindow(self, Descriptor: 'WindowDescriptor_d61e0ceb') -> 'XWindowPeer_99760ab0':
        """
        creates a new window using the given descriptor.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def createWindows(self, Descriptors: 'typing.Tuple[WindowDescriptor_d61e0ceb, ...]') -> 'typing.Tuple[XWindowPeer_99760ab0, ...]':
        """
        returns a sequence of windows which are newly created using the given descriptors.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def getDesktopWindow(self) -> 'XWindowPeer_99760ab0':
        """
        returns the desktop window.
        """
    def getWorkArea(self) -> 'Rectangle_84b109e9':
        """
        For LibreOffice versions < 4.1, this method just returned an empty rectangle.
        
        After that, it started returning a valid value.
        """

__all__ = ['XToolkit']

