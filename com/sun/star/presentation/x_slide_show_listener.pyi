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

from ..animations.x_animation_listener import XAnimationListener as XAnimationListener_5c5a1079


class XSlideShowListener(XAnimationListener_5c5a1079):
    """
    Listener interface to receive global slide show events.
    
    **since**
    
        OOo 3.0

    See Also:
        `API XSlideShowListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1presentation_1_1XSlideShowListener.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.presentation.XSlideShowListener'

    def hyperLinkClicked(self, hyperLink: str) -> None:
        """
        Notifies that a hyperlink has been clicked.
        """
        ...
    def paused(self) -> None:
        """
        Notify that the slide show is paused.
        """
        ...
    def resumed(self) -> None:
        """
        Notify that the slide show is resumed from a paused state.
        """
        ...
    def slideAnimationsEnded(self) -> None:
        """
        Notify that the last animation from the main sequence of the current slide has ended.
        """
        ...
    def slideEnded(self, reverse: bool) -> None:
        """
        Notify that the current slide has ended, e.g.
        
        the user has clicked on the slide. Calling displaySlide() twice will not issue this event.
        """
        ...
    def slideTransitionEnded(self) -> None:
        """
        Notify that the slide transition of the current slide ended.
        """
        ...
    def slideTransitionStarted(self) -> None:
        """
        Notify that a new slide starts to become visible.
        """
        ...


