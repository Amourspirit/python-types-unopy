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
# Libre Office Version: 7.4
# Namespace: com.sun.star.frame
from typing_extensions import Literal
import typing
from ..container.x_index_access import XIndexAccess as XIndexAccess_f0910d6d
if typing.TYPE_CHECKING:
    from .x_frame import XFrame as XFrame_7a570956

class XFrames(XIndexAccess_f0910d6d):
    """
    manages and creates frames.
    
    Frames may contain other frames (by implementing an XFrames interface) and may be contained in other frames.

    See Also:
        `API XFrames <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XFrames.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.frame.XFrames']

    def append(self, xFrame: 'XFrame_7a570956') -> None:
        """
        appends the specified Frame to the list of sub-frames.
        """
        ...
    def queryFrames(self, nSearchFlags: int) -> 'typing.Tuple[XFrame_7a570956, ...]':
        """
        provides access to the list of all currently existing frames inside this container and her sub frames
        """
        ...
    def remove(self, xFrame: 'XFrame_7a570956') -> None:
        """
        removes the frame from its container.
        
        Note:
        """
        ...


