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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.frame
from __future__ import annotations
from .x_status_listener import XStatusListener as XStatusListener_e2740d35
from .x_sub_toolbar_controller import XSubToolbarController as XSubToolbarController_37b30f8c
from .x_toolbar_controller import XToolbarController as XToolbarController_b630e62
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca
from ..util.x_updatable import XUpdatable as XUpdatable_9a420ab0

class ToolbarController(XStatusListener_e2740d35, XSubToolbarController_37b30f8c, XToolbarController_b630e62, XInitialization_d46c0cca, XUpdatable_9a420ab0):
    """
    Service Class

    is an abstract service for a component which offers a more complex user interface to users within a toolbar.
    
    A generic toolbar function is represented as a button which has a state (enabled,disabled and selected, not selected). A toolbar controller can be added to a toolbar and provide information or functions within a more sophisticated user interface.A typical example for toolbar controller is the font chooser within the toolbar. It provides all available fonts in a dropdown box and shows the current chosen font.
    
    **since**
    
        OOo 2.0

    See Also:
        `API ToolbarController <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1frame_1_1ToolbarController.html>`_
    """
    ...

