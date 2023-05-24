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
# Namespace: com.sun.star.script.provider
from __future__ import annotations
import typing

from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ...document.x_script_invocation_context import XScriptInvocationContext as XScriptInvocationContext_a29f1233
    from ...frame.x_desktop import XDesktop as XDesktop_8e740a45
    from ...frame.x_model import XModel as XModel_7a6e095c
    from ...uno.x_component_context import XComponentContext as XComponentContext_e2e10d4a


class XScriptContext(XInterface_8f010a43):
    """
    This interface is provided to scripts, and provides a means of access to the various interfaces which they might need to perform some action on a document.
    
    It is required to be passed as the first argument for any Java scripts.
    
    **since**
    
        OOo 3.0

    See Also:
        `API XScriptContext <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1provider_1_1XScriptContext.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.script.provider.XScriptContext'

    def getComponentContext(self) -> XComponentContext_e2e10d4a:
        """
        Obtain the component context which the script can use to create other uno components.
        """
        ...
    def getDesktop(self) -> XDesktop_8e740a45:
        """
        Obtain the desktop reference on which the script can operate.
        """
        ...
    def getDocument(self) -> XModel_7a6e095c:
        """
        Obtain the document reference on which the script can operate.
        """
        ...
    def getInvocationContext(self) -> XScriptInvocationContext_a29f1233:
        """
        provides access to the context where the script was invoked
        
        In some cases, it is possible that scripts, embedded in a document, are executed from within a context which is not the document itself. In this case, the getInvocationContext member allows to access this context.
        
        Note that the returned context is allowed to be NULL, in this case, the document as returned by getDocument is the invocation context.
        
        If the returned context is not NULL, its ScriptContainer attribute equals the document as returned by XScriptContext.getDocument.
        
        **since**
        
            OOo 3.0
        """
        ...


