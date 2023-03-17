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
# Namespace: com.sun.star.awt
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..util.color import Color as Color_68e908c5

class XProgressBar(XInterface_8f010a43):
    """
    gives access to the value and settings of a progress bar.

    See Also:
        `API XProgressBar <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XProgressBar.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XProgressBar']

    def getValue(self) -> int:
        """
        returns the current progress value of the progress bar.
        """
        ...
    def setBackgroundColor(self, Color: 'Color_68e908c5') -> None:
        """
        sets the background color (RGB) of the control.
        """
        ...
    def setForegroundColor(self, Color: 'Color_68e908c5') -> None:
        """
        sets the foreground color (RGB) of the control.
        """
        ...
    def setRange(self, Min: int, Max: int) -> None:
        """
        sets the minimum and the maximum progress value of the progress bar.
        
        If the minimum value is greater than the maximum value, the method exchanges the values automatically.
        """
        ...
    def setValue(self, Value: int) -> None:
        """
        sets the progress value of the progress bar.
        """
        ...


