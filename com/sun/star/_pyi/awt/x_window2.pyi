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
from .x_window import XWindow as XWindow_713b0924
if typing.TYPE_CHECKING:
    from .size import Size as Size_576707ef

class XWindow2(XWindow_713b0924):
    """
    specifies some extended operations for a window component.
    
    A window is a rectangular region on an output device with its own position, size, and internal coordinate system. A window is used for displaying data. In addition, the window receives events from the user.

    See Also:
        `API XWindow2 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XWindow2.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XWindow2']

    def getOutputSize(self) -> 'Size_576707ef':
        """
        returns the inner bounds of the window, also known as the client size.
        """
        ...
    def hasFocus(self) -> bool:
        """
        returns the focus state of the window
        """
        ...
    def isActive(self) -> bool:
        """
        returns the activation state of the window
        """
        ...
    def isEnabled(self) -> bool:
        """
        returns the enabled state of the window
        """
        ...
    def isVisible(self) -> bool:
        """
        returns the visibility state of the window
        """
        ...
    def setOutputSize(self, Size: 'Size_576707ef') -> None:
        """
        sets the inner bounds of the window, also known as the client size
        """
        ...


