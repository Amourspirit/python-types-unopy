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
# Namespace: com.sun.star.frame
from typing_extensions import Literal
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XToolbarControllerListener(XInterface_8f010a43):
    """
    is used to notify a toolbar controller about events
    
    **since**
    
        OOo 2.0

    See Also:
        `API XToolbarControllerListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XToolbarControllerListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.frame.XToolbarControllerListener']

    def functionSelected(self, aToolbarRes: str, aCommand: str) -> None:
        """
        gets called to notify a controller that a toolbar function has been selected.
        
        This notification is normally used to implement the toolbar button/sub-toolbar function feature. It exchanges the function of the toolbar button, that opened the sub-toolbar, with the one that has been selected on the sub-toolbar.
        """

__all__ = ['XToolbarControllerListener']

