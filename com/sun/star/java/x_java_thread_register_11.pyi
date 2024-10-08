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
# Namespace: com.sun.star.java
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XJavaThreadRegister_11(XInterface_8f010a43):
    """
    must be implemented by the user of the XJavaThreadRegister_11.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XJavaThreadRegister_11 <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1java_1_1XJavaThreadRegister__11.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.java.XJavaThreadRegister_11'

    def isThreadAttached(self) -> bool:
        """
        returns TRUE if the current thread is already attached to the VM otherwise FALSE.
        """
        ...
    def registerThread(self) -> None:
        """
        registers the current thread.
        
        This method should be called every time a JNI function is called from Java.
        """
        ...
    def revokeThread(self) -> None:
        """
        revokes the current thread from the list of registered threads.
        
        This method should be called at the end of every JNI call from Java.
        """
        ...


