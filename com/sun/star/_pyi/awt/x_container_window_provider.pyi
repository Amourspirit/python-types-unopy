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
# Namespace: com.sun.star.awt
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_window import XWindow as XWindow_713b0924
    from .x_window_peer import XWindowPeer as XWindowPeer_99760ab0

class XContainerWindowProvider(XInterface_8f010a43):
    """
    provides container windows implementing the com.sun.star.awt.XWindow interface.

    See Also:
        `API XContainerWindowProvider <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XContainerWindowProvider.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XContainerWindowProvider']

    def createContainerWindow(self, URL: str, WindowType: str, xParent: 'XWindowPeer_99760ab0', xHandler: 'XInterface_8f010a43') -> 'XWindow_713b0924':
        """
        creates a window for the given URL
        
        xHandler can handle events in two different ways:
        
        If XContainerWindowEventHandler is supported XContainerWindowEventHandler.callHandlerMethod() is always called first to handle the event. Only if the event cannot be handled by XContainerWindowEventHandler (callHandlerMethod() then has to return false) or if XContainerWindowEventHandler is not supported at all the Introspection based access will be used.
        
        The Introspection based access tries to call a method named according to the HandlerMethodName specified by a vnd.sun.star.UNO:HandlerMethodName URL. First a method
        
        void HandlerMethodName( [in] com.sun.star.awt.XWindow xWindow, [in] any aEvent )
        
        will be searched. The signature is similar to XContainerWindowEventHandler. callHandlerMethod except for MethodName itself that isn't needed here. For more information about these parameters, see com.sun.star.awt.XContainerWindowEventHandler.
        
        If this method is found, it will be called, otherwise a method
        
        void HandlerMethodName( void )
        
        will be searched and called.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...


