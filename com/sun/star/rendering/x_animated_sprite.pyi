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
# Namespace: com.sun.star.rendering
from __future__ import annotations
import typing

from .x_sprite import XSprite as XSprite_b2470b95
if typing.TYPE_CHECKING:
    from ..geometry.real_point2_d import RealPoint2D as RealPoint2D_d6e70c78
    from .render_state import RenderState as RenderState_e4490d27
    from .view_state import ViewState as ViewState_cab30c62


class XAnimatedSprite(XSprite_b2470b95):
    """
    This interface can be used to control an animated sprite object.
    
    This interface can be used to control an animated sprite object on an XSpriteCanvas. Sprites are moving, animated objects.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XAnimatedSprite <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XAnimatedSprite.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.rendering.XAnimatedSprite'

    def resetAnimation(self) -> None:
        """
        Reset the animation sequence to start with the first frame.
        
        If the animation is currently running, the next frame that is drawn after this method has finished, will be the first one. Please note that if an animation is not started, the associated XSpriteCanvas does not update changed sprites automatically.
        """
        ...
    def setAll(self, aNewPos: RealPoint2D_d6e70c78, aViewState: ViewState_cab30c62, aRenderState: RenderState_e4490d27, nAlpha: float, bUpdateAnimation: bool) -> None:
        """
        Changes all of the sprite's attributes at one atomic instance.
        
        This is useful at times where one does not want multiple redraws for every state change.
        
        Please note that if an animation is not started, the associated XSpriteCanvas does not update changed sprites automatically, but has to be told to do so via XSpriteCanvas.updateScreen().

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def setViewState(self, aViewState: ViewState_cab30c62) -> None:
        """
        Changes the view state in place for this sprite's animation.
        
        The state given here is used when calling the XAnimation.render() method, or when drawing the sprite's bitmaps, respectively. There's no need to call XSpriteCanvas.updateAnimation() after this method, as it automatically rerenders, if necessary. Please note that if an animation is not started, the associated XSpriteCanvas does not update changed sprites automatically, but has to be told to do so via XSpriteCanvas.updateScreen().

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def startAnimation(self, nSpeed: float) -> None:
        """
        Start animation sequence of this sprite.
        
        The speed of the animation is given in cycles per second (where a cycle is defined as one full animation run, i.e. the full [0,1] range of the XAnimation.render()'s t parameter, or a full sequence of sprite bitmaps drawn). Once an animation is running, the associated XSpriteCanvas handles screen updates automatically. That means, changes to position or alpha are reflected on screen automatically. Please note further that sprite visibility and animation are unrelated, i.e. a hidden sprite can have a running animation, which then displays in the middle of the animation sequence, when a show() is called later on.
        """
        ...
    def stopAnimation(self) -> None:
        """
        Stop the animation sequence.
        
        A subsequent XAnimatedSprite.startAnimation() will commence the sequence at the point where it was stopped with here. Once an animation is stopped, the associated XSpriteCanvas does not update changed sprites anymore.
        """
        ...
    def updateAnimation(self) -> None:
        """
        Issue an additional render call to this sprite's animation.
        
        This method has no effect when called for a bitmap-sequence sprite. Please note that if an animation is not started, the associated XSpriteCanvas does not update changed sprites automatically, but has to be told to do so via XSpriteCanvas.updateScreen().
        """
        ...


