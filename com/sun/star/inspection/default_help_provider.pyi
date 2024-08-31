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
# Namespace: com.sun.star.inspection
from __future__ import annotations
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_object_inspector_ui import XObjectInspectorUI as XObjectInspectorUI_5ccd1048

class DefaultHelpProvider(XInterface_8f010a43):
    """
    Service Class

    implements a component which can default-fill the help section of an ObjectInspector.
    
    The component registers a XPropertyControlObserver at an XObjectInspectoryUI interface. Whenever it then is notified of a XPropertyControl getting the focus, it will try to deduce the extended help text of this control's window, and set this help text at the object inspector's help section.

    See Also:
        `API DefaultHelpProvider <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1inspection_1_1DefaultHelpProvider.html>`_
    """
    def create(self, InspectorUI: XObjectInspectorUI_5ccd1048) -> None:
        """
        creates a help provider instance

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

