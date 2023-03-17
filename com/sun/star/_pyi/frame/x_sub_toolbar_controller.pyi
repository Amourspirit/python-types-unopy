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
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XSubToolbarController(XInterface_8f010a43):
    """
    special interface to support sub-toolbars in a controller implementation.
    
    This interface is normally used to implement the toolbar button/sub- toolbar function feature. It exchanges the function of the toolbar button, that opened the sub-toolbar, with the one that has been selected on the sub-toolbar.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XSubToolbarController <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XSubToolbarController.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.frame.XSubToolbarController']

    def functionSelected(self, aCommand: str) -> None:
        """
        gets called to notify a controller that a sub-toolbar function has been selected.
        """
        ...
    def getSubToolbarName(self) -> str:
        """
        provides the resource URL of the sub-toolbar this controller opens.
        """
        ...
    def opensSubToolbar(self) -> bool:
        """
        if the controller features a sub-toolbar.
        
        Enables implementations to dynamically decide to support sub-toolbars or not.
        """
        ...
    def updateImage(self) -> None:
        """
        gets called to notify a controller that it should set an image which represents the current selected function.
        
        Only the controller instance is able to set the correct image for the current function. A toolbar implementation will ask sub-toolbar controllers to update their image whenever it has to update the images of all its buttons.
        """
        ...


