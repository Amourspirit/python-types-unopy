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
# Namespace: com.sun.star.presentation
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..awt.rectangle import Rectangle as Rectangle_84b109e9
    from ..awt.x_mouse_listener import XMouseListener as XMouseListener_bc1d0bfb
    from ..awt.x_mouse_motion_listener import XMouseMotionListener as XMouseMotionListener_c6a0e71
    from ..awt.x_paint_listener import XPaintListener as XPaintListener_bb6d0bee
    from ..geometry.affine_matrix2_d import AffineMatrix2D as AffineMatrix2D_ff040da8
    from ..geometry.integer_size2_d import IntegerSize2D as IntegerSize2D_f2690d53
    from ..rendering.x_sprite_canvas import XSpriteCanvas as XSpriteCanvas_ff8b0df1
    from ..util.x_modify_listener import XModifyListener as XModifyListener_d5c60ccc


class XSlideShowView(XInterface_8f010a43):
    """
    View interface to display slide show presentations on.
    
    This interface provides the necessary methods to enable an XSlideShow interface to display a presentation. The slide show can be displayed simultaneously on multiple views
    
    **since**
    
        OOo 2.4

    See Also:
        `API XSlideShowView <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1presentation_1_1XSlideShowView.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.presentation.XSlideShowView'

    def addMouseListener(self, xListener: XMouseListener_bc1d0bfb) -> None:
        """
        Add a mouse listener to the view.
        
        This method registers a listener with the view, which will get called every time the mouse is clicked on the view.
        """
        ...
    def addMouseMotionListener(self, xListener: XMouseMotionListener_c6a0e71) -> None:
        """
        Add a mouse motion listener to the view.
        
        This method registers a listener with the view, which will get called every time the mouse is moved on the view.
        """
        ...
    def addPaintListener(self, xListener: XPaintListener_bb6d0bee) -> None:
        """
        Add a listener to get notified when this view needs a repaint.
        
        This method registers a listener with the view, which will get called every time the view needs an update of their screen representation.
        """
        ...
    def addTransformationChangedListener(self, xListener: XModifyListener_d5c60ccc) -> None:
        """
        Add a listener to get notified when the transformation matrix changes.
        
        This method registers a listener with the view, which will get called every time the transformation matrix changes.
        """
        ...
    def clear(self) -> None:
        """
        This method clears the whole view area.
        
        The slide show uses this method to fully erase the view content. Since the slide show has no notion of view size, this is the only reliable way to wholly clear the view.
        """
        ...
    def getCanvas(self) -> XSpriteCanvas_ff8b0df1:
        """
        Get view canvas.
        
        This method gets the underlying XCanvas to display on this view.
        """
        ...
    def getCanvasArea(self) -> Rectangle_84b109e9:
        """
        Get rectangle defining area inside of canvas device which this slide show view uses.
        """
        ...
    def getTransformation(self) -> AffineMatrix2D_ff040da8:
        """
        Query the current transformation matrix for this view.
        
        This method returns the transformation matrix of the view. When notified via the transformation change listener, the show will be displayed using the new transformation.
        """
        ...
    def getTranslationOffset(self) -> IntegerSize2D_f2690d53:
        """
        Query the current translation offset used to fill the physical screen while keeping aspect ratio.
        
        This method returns the translation offset of the view of the view.
        """
        ...
    def removeMouseListener(self, xListener: XMouseListener_bc1d0bfb) -> None:
        """
        Revoke a previously registered mouse listener.
        """
        ...
    def removeMouseMotionListener(self, xListener: XMouseMotionListener_c6a0e71) -> None:
        """
        Revoke a previously registered mouse move listener.
        """
        ...
    def removePaintListener(self, xListener: XPaintListener_bb6d0bee) -> None:
        """
        Revoke a previously registered paint listener.
        """
        ...
    def removeTransformationChangedListener(self, xListener: XModifyListener_d5c60ccc) -> None:
        """
        Revoke a previously registered transformation matrix change listener.
        """
        ...
    def setMouseCursor(self, nPointerShape: int) -> None:
        """
        Change the mouse cursor currently in effect.
        
        This method changes the mouse cursor currently in effect, for this view.
        """
        ...


