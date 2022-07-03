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
# Libre Office Version: 7.3
# Namespace: com.sun.star.java
from typing_extensions import Literal
import uno
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XJavaVM(XInterface_8f010a43):
    """
    must be implemented by the user of the XJavaVM.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XJavaVM <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1java_1_1XJavaVM.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.java.XJavaVM']

    def getJavaVM(self, processID: uno.ByteSequence) -> object:
        """
        returns the address of the Java Virtual Machine.
        
        If the VM is not already instantiated, it will be now.
        
        If the processID is a normal 16-byte ID, the returned any contains a JNI JavaVM pointer as a long or hyper integer (depending on the platform). If the processID does not match the current process, or if the VM cannot be instantiated for whatever reason, a VOID any is returned.
        
        If the processID has an additional 17th byte of value 0, the returned any contains a non–reference-counted pointer to a (reference-counted) instance of the C++ jvmaccess.VirtualMachine class, always represented as a hyper integer. The pointer is guaranteed to be valid as long as the reference to this com.sun.star.java.XJavaVM is valid (but the pointer should be converted into a reference-counted reference as soon as possible). Again, if the first 16 bytes of the processID do not match the current process, or if the VM cannot be instantiated for whatever reason, a VOID any is returned.
        
        If the processID has an additional 17th byte of value 1, the returned any contains a non–reference-counted pointer to a (reference-counted) instance of the C++ jvmaccess.UnoVirtualMachine class, always represented as a hyper integer. The pointer is guaranteed to be valid as long as the reference to this com.sun.star.java.XJavaVM is valid. Again, if the first 16 bytes of the processID do not match the current process, or if the VM cannot be instantiated for whatever reason, a VOID any is returned.
        
        The first form (returning a JNI JavaVM pointer) is mainly for backwards compatibility, new code should use the second form (returning a pointer to a jvmaccess.VirtualMachine) if it does not want to use the Java UNO environment, and it should use the third form (returning a pointer to a jvmaccess.UnoVirtualMachine) if it wants to use the Java UNO environment. For example, one advantage of using jvmaccess.VirtualMachine instead of the raw JavaVM pointer is that whenever you attach a native thread to the Java virtual machine, that thread's context ClassLoader (see java.lang.Thread.getContextClassLoader) will automatically be set to a meaningful value.
        """
        ...
    def isVMEnabled(self) -> bool:
        """
        Returns TRUE if the VM is enabled.
        
        It is only possible to get the VM, if this method return 0.
        """
        ...
    def isVMStarted(self) -> bool:
        """
        returns TRUE if the VM is started successfully, otherwise FALSE.
        """
        ...


