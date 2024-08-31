# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.awt
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .size import Size as Size_576707ef
    from .x_graphics import XGraphics as XGraphics_842309dd


class XView(XInterface_8f010a43):
    """
    makes it possible to attach an output device to the object.
    
    This kind of object is called view-object.

    See Also:
        `API XView <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XView.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.awt.XView'

    def draw(self, nX: int, nY: int) -> None:
        """
        draws the object at the specified position.
        
        If the output should be clipped, the caller has to set the clipping region.
        """
        ...
    def getGraphics(self) -> XGraphics_842309dd:
        """
        returns the output device which was set using the method XView.setGraphics().
        """
        ...
    def getSize(self) -> Size_576707ef:
        """
        returns the size of the object in device units.
        
        A device must be set before.
        """
        ...
    def setGraphics(self, aDevice: XGraphics_842309dd) -> bool:
        """
        sets the output device.
        """
        ...
    def setZoom(self, fZoomX: float, fZoomY: float) -> None:
        """
        sets the zoom factor.
        
        The zoom factor only affects the content of the view, not the size.
        """
        ...


