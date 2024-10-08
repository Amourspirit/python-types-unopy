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
# Namespace: com.sun.star.task
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XStatusIndicator(XInterface_8f010a43):
    """
    controls a status indicator which displays progress of longer actions to the user
    
    Such objects are provided by a XStatusIndicatorFactory.

    See Also:
        `API XStatusIndicator <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1task_1_1XStatusIndicator.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.task.XStatusIndicator'

    def end(self) -> None:
        """
        stop the progress
        
        Further calls of XStatusIndicator.setText(), XStatusIndicator.setValue() or XStatusIndicator.reset() must be ignored. Only XStatusIndicator.start() can reactivate this indicator. It's not allowed to destruct the indicator inside this method. The instance must be gone by using ref count or disposing.
        """
        ...
    def reset(self) -> None:
        """
        clear progress value and description
        
        Calling of setValue(0) and setText(\"\") should do the same. Stopped indicators must ignore this call.
        """
        ...
    def setText(self, Text: str) -> None:
        """
        update progress description
        
        Initial value can be set during starting of the progress by calling XStatusIndicator.start(). Stopped indicators must ignore this call.
        """
        ...
    def setValue(self, Value: int) -> None:
        """
        update progress value
        
        Wrong values must be ignored and stopped indicators must ignore this call generally.
        """
        ...
    def start(self, Text: str, Range: int) -> None:
        """
        initialize and start the progress
        
        It activates a new created or reactivate an already used indicator (must be finished by calling XStatusIndicator.end() before!). By the way it's possible to set first progress description and the possible range of progress value. That means that a progress can runs from 0 to Range.
        """
        ...


