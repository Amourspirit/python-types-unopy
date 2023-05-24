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
# Namespace: com.sun.star.awt
from __future__ import annotations
import typing

import uno
from ..uno.x_interface import XInterface as XInterface_8f010a43


class XSystemDependentWindowPeer(XInterface_8f010a43):
    """
    provides access to the system dependent implementation of the window.

    See Also:
        `API XSystemDependentWindowPeer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XSystemDependentWindowPeer.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.awt.XSystemDependentWindowPeer'

    def getWindowHandle(self, ProcessId: uno.ByteSequence, SystemType: int) -> typing.Any:
        """
        returns a system-specific window handle.
        
        You must check the machine ID and the process ID.WIN32: Returns an HWND if possible, otherwise 0.WIN16: Returns an HWND if possible, otherwise 0.
        
        JAVA: Returns a global reference to a java.awt.Component object provided from the JNI-API.
        
        MAC: Returns a ptr to the NSView implementing the window.
        
        XWINDOW: Returns a structure SystemDependentXWindow or void if it is not reachable.
        """
        ...


