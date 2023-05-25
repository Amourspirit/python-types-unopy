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
# Namespace: com.sun.star.presentation
from __future__ import annotations
import typing

from abc import ABC
if typing.TYPE_CHECKING:
    from ..drawing.x_draw_page import XDrawPage as XDrawPage_b07a0b57
    from .x_slide_show import XSlideShow as XSlideShow_2a80e0e
    from .x_slide_show_listener import XSlideShowListener as XSlideShowListener_81671154


class XSlideShowController(ABC):
    """
    interface to control a running slide show.
    
    **since**
    
        OOo 3.0

    See Also:
        `API XSlideShowController <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1presentation_1_1XSlideShowController.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.presentation.XSlideShowController'

    def activate(self) -> None:
        """
        activates the user interface of this slide show.
        """
        ...
    def addSlideShowListener(self, Listener: XSlideShowListener_81671154) -> None:
        """
        adds a listener that receives events while the slide show is running.
        """
        ...
    def blankScreen(self, Color: int) -> None:
        """
        pauses the slide show and blanks the screen in the given color.
        
        Change attribute Pause to false to unpause the slide show.
        """
        ...
    def deactivate(self) -> None:
        """
        can be called to deactivate the user interface of this slide show.
        
        A deactivated
        """
        ...
    def getCurrentSlide(self) -> XDrawPage_b07a0b57:
        """
        returns slide that is currently displayed
        """
        ...
    def getCurrentSlideIndex(self) -> int:
        """
        returns the index of the current slide.
        """
        ...
    def getNextSlideIndex(self) -> int:
        """
        the index for the slide that is displayed next.
        """
        ...
    def getSlideByIndex(self, Index: int) -> XDrawPage_b07a0b57:
        """
        gives access to the slides that will be shown in this slide show.
        
        Slides are returned in the order they will be displayed in the presentation which can be different than the orders of slides in the document. Not all slides must be present and each slide can be used more than once.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def getSlideCount(self) -> int:
        """
        """
        ...
    def getSlideShow(self) -> XSlideShow_2a80e0e:
        """
        returns the actual XSlideShow instance that runs the slide show.
        
        Normally all navigation should be done using this controller and not the XSlideShow itself.
        """
        ...
    def gotoBookmark(self, Bookmark: str) -> None:
        """
        goto the given textual bookmark
        """
        ...
    def gotoFirstSlide(self) -> None:
        """
        goto and display first slide
        """
        ...
    def gotoLastSlide(self) -> None:
        """
        goto and display last slide.
        
        Remaining effects on the current slide will be skipped.
        """
        ...
    def gotoNextEffect(self) -> None:
        """
        start next effects that wait on a generic trigger.
        
        If no generic triggers are waiting the next slide will be displayed.
        """
        ...
    def gotoNextSlide(self) -> None:
        """
        goto and display next slide.
        
        Remaining effects on the current slide will be skipped.
        """
        ...
    def gotoPreviousEffect(self) -> None:
        """
        undo the last effects that were triggered by a generic trigger.
        
        If there is no previous effect that can be undone then the previous slide will be displayed.
        """
        ...
    def gotoPreviousSlide(self) -> None:
        """
        goto and display previous slide.
        
        Remaining effects on the current slide will be skipped.
        """
        ...
    def gotoSlide(self, Page: XDrawPage_b07a0b57) -> None:
        """
        jumps to the given slide.
        
        The slide can also be a slide that would normally not be shown during the current slide show.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def gotoSlideIndex(self, Index: int) -> None:
        """
        jumps to the slide at the given index.
        """
        ...
    def isActive(self) -> bool:
        """
        determines if the slide show is active.
        """
        ...
    def isEndless(self) -> bool:
        """
        returns TRUE if the slide show was started to run endlessly.
        """
        ...
    def isFullScreen(self) -> bool:
        """
        Returns TRUE if the slide show was started in full-screen mode.
        """
        ...
    def isPaused(self) -> bool:
        """
        returns TRUE if the slide show is currently paused.
        """
        ...
    def isRunning(self) -> bool:
        """
        returns true if the slide show is still running.
        
        If this returns false, this component is already disposed. You can start a new slide show and get a new instance of XSlideShowController from XPresentation2
        """
        ...
    def pause(self) -> None:
        """
        pauses the slide show.
        
        All effects are paused.
        
        The slide show continues on next user input or if resume() is called.
        """
        ...
    def removeSlideShowListener(self, Listener: XSlideShowListener_81671154) -> None:
        """
        removes a listener.
        """
        ...
    def resume(self) -> None:
        """
        resumes a paused slide show.
        """
        ...
    def setEraseAllInk(self, EraseAllInk: bool) -> None:
        """
        This method clears ink drawing from the slideshow being played.
        
        **since**
        
            LibreOffice 7.2
        """
        ...
    def stopSound(self) -> None:
        """
        stop all currently played sounds
        """
        ...

    @property
    def AlwaysOnTop(self) -> bool:
        """
        If this attribute is set to TRUE, the window of the slide show is always on top of all other windows.
        """
        ...
    @AlwaysOnTop.setter
    def AlwaysOnTop(self, value: bool) -> None:
        ...
    @property
    def MouseVisible(self) -> bool:
        """
        If this attribute is TRUE, the mouse is visible during the slide show.
        """
        ...
    @MouseVisible.setter
    def MouseVisible(self, value: bool) -> None:
        ...
    @property
    def PenColor(self) -> int:
        """
        This attribute changes the color of the pen.
        """
        ...
    @PenColor.setter
    def PenColor(self, value: int) -> None:
        ...
    @property
    def PenWidth(self) -> float:
        """
        This attribute changes the width of the pen.
        
        **since**
        
            LibreOffice 4.2
        """
        ...
    @PenWidth.setter
    def PenWidth(self, value: float) -> None:
        ...
    @property
    def UsePen(self) -> bool:
        """
        If this is TRUE, a pen is shown during presentation.
        
        You can draw on the presentation with this pen.
        """
        ...
    @UsePen.setter
    def UsePen(self, value: bool) -> None:
        ...


