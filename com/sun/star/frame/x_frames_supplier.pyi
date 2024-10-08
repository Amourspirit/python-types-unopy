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
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing

from .x_frame import XFrame as XFrame_7a570956
if typing.TYPE_CHECKING:
    from .x_frames import XFrames as XFrames_842009c9


class XFramesSupplier(XFrame_7a570956):
    """
    provides access to sub frames of current one

    See Also:
        `API XFramesSupplier <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XFramesSupplier.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.frame.XFramesSupplier'

    def getActiveFrame(self) -> XFrame_7a570956:
        """
        gets the current active frame of this container (not of any other available supplier)
        
        This may be the frame itself. The active frame is defined as the frame which contains (recursively) the window with the focus. If no window within the frame contains the focus, this method returns the last frame which had the focus. If no containing window ever had the focus, the first frame within this frame is returned.
        """
        ...
    def getFrames(self) -> XFrames_842009c9:
        """
        provides access to this container and to all other XFramesSupplier which are available from this node of frame tree
        """
        ...
    def setActiveFrame(self, Frame: XFrame_7a570956) -> None:
        """
        is called on activation of a direct sub-frame.
        
        This method is only allowed to be called by a sub-frame according to XFrame.activate() or XFramesSupplier.setActiveFrame(). After this call XFramesSupplier.getActiveFrame() will return the frame specified by Frame.
        
        In general this method first calls the method XFramesSupplier.setActiveFrame() at the creator frame with this as the current argument. Then it broadcasts the FrameActionEvent FrameAction.FRAME_ACTIVATED.
        
        Note: Given parameter Frame must already exist inside the container (e.g., inserted by using XFrames.append())
        """
        ...


