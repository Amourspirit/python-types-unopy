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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.awt
# Libre Office Version: 2024.2
import typing


class SystemDependentXWindow(object):
    """
    Struct Class

    specifies a system dependent XWindow.
    
    This is the structure returned in the XSystemDependentWindowPeer.getWindowHandle() call, if the system type is com.sun.star.lang.SystemDependent.XWINDOW.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API SystemDependentXWindow <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1awt_1_1SystemDependentXWindow.html>`_
    """
    typeName: str = 'com.sun.star.awt.SystemDependentXWindow'

    def __init__(self, WindowHandle: typing.Optional[int] = ..., DisplayPointer: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            WindowHandle (int, optional): WindowHandle value.
            DisplayPointer (int, optional): DisplayPointer value.
        """
        ...

    @property
    def WindowHandle(self) -> int:
        """
        The XWindow handle if possible, otherwise 0.
        """
        ...
    @WindowHandle.setter
    def WindowHandle(self, value: int) -> None:
        ...
    @property
    def DisplayPointer(self) -> int:
        """
        The display pointer.
        """
        ...
    @DisplayPointer.setter
    def DisplayPointer(self, value: int) -> None:
        ...

