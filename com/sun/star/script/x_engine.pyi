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
# Namespace: com.sun.star.script
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_engine_listener import XEngineListener as XEngineListener_f0b70d91
    from .x_library_access import XLibraryAccess as XLibraryAccess_e32a0d1c


class XEngine(XInterface_8f010a43):
    """
    makes it possible to control a scripting engine.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XEngine <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XEngine.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.script.XEngine'

    def addEngineListener(self, Listener: XEngineListener_f0b70d91) -> None:
        """
        adds an engine listener.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.
        """
        ...
    def cancel(self) -> None:
        """
        terminates the execution of the running script.
        
        The waiting queue is cleared too.
        """
        ...
    def compile(self, ModuleName: str, Script: str, CreateDebugInfo: bool) -> bool:
        """
        compiles a script module in the scope of the root object.
        """
        ...
    def getRoot(self) -> XInterface_8f010a43:
        """
        gets an interface to the object which is the scripting root.
        """
        ...
    def removeEngineListener(self, Listener: XEngineListener_f0b70d91) -> None:
        """
        removes an engine listener.
        
        It is suggested to allow multiple registration of the same listener, thus for each time a listener is added, it has to be removed.
        """
        ...
    def run(self, aScript: str, xThis: XInterface_8f010a43, aArgs: typing.Tuple[object, ...]) -> typing.Any:
        """
        runs a script specified by a string.
        
        The arguments given in aArgs can be ignored by the engine. The Script is executed synchronously.
        """
        ...
    def runAsync(self, acript: str, xThis: XInterface_8f010a43, args: typing.Tuple[object, ...], xCallback: XEngineListener_f0b70d91) -> None:
        """
        runs the script specified by a string and makes callbacks.
        
        The arguments given in aArgs can be ignored by the engine. The script is executed asynchronously.
        """
        ...
    def setLibraryAccess(self, Library: XLibraryAccess_e32a0d1c) -> None:
        """
        sets an access object to get external functions.
        """
        ...
    def setRoot(self, xRoot: XInterface_8f010a43) -> None:
        """
        sets an interface to an object as a scripting root.
        
        If the root object implements the XInvocation interface, then the engine uses this interface to set/get properties and call methods.
        """
        ...



