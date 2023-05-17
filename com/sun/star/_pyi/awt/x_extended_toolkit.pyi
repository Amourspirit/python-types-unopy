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
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_focus_listener import XFocusListener as XFocusListener_bb8e0bf2
    from .x_key_handler import XKeyHandler as XKeyHandler_98520a93
    from .x_top_window import XTopWindow as XTopWindow_8ebb0a57
    from .x_top_window_listener import XTopWindowListener as XTopWindowListener_efc20d9d


class XExtendedToolkit(XInterface_8f010a43):
    """
    The XExtendedToolkit is an extension of the com.sun.star.awt.XToolkit interface.
    
    It basically provides access to three event broadcasters which are used for instance in the context of accessibility. It is, however, not restricted to accessibility.
    
    The first event broadcaster lets you keep track of the open top-level windows (frames). To get the set of currently open top-level window use the XExtendedToolkit.getTopWindowCount() and XExtendedToolkit.getTopWindow() methods.
    
    The second event broadcaster informs its listeners of key events. Its listeners can, unlike with most other broadcasters/listeners, consume events, so that other listeners will not be called for consumed events.
    
    The last event broadcaster sends events on focus changes of all elements that can have the input focus.
    
    **since**
    
        OOo 1.1.2
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XExtendedToolkit <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XExtendedToolkit.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XExtendedToolkit']

    def addFocusListener(self, xListener: 'XFocusListener_bb8e0bf2') -> None:
        """
        Add a new listener that is called on com.sun.star.awt.FocusEvent.
        
        Use this focus broadcaster to keep track of the object that currently has the input focus.
        """
        ...
    def addKeyHandler(self, xHandler: 'XKeyHandler_98520a93') -> None:
        """
        Add a new listener that is called on com.sun.star.awt.KeyEvent.
        
        Every listener is given the opportunity to consume the event, i.e. prevent the not yet called listeners from being called.
        """
        ...
    def addTopWindowListener(self, xListener: 'XTopWindowListener_efc20d9d') -> None:
        """
        Add a new listener that is called for events that involve com.sun.star.awt.XTopWindow.
        
        After having obtained the current list of existing top-level windows you can keep this list up-to-date by listening to opened or closed top-level windows. Wait for activations or deactivations of top-level windows to keep track of the currently active frame.
        """
        ...
    def fireFocusGained(self, source: 'XInterface_8f010a43') -> None:
        """
        Broadcasts the a focusGained on all registered focus listeners.
        """
        ...
    def fireFocusLost(self, source: 'XInterface_8f010a43') -> None:
        """
        Broadcasts the a focusGained on all registered focus listeners.
        """
        ...
    def getActiveTopWindow(self) -> 'XTopWindow_8ebb0a57':
        """
        Return the currently active top-level window, i.e.
        
        which has currently the input focus.
        """
        ...
    def getTopWindow(self, nIndex: int) -> 'XTopWindow_8ebb0a57':
        """
        Return a reference to the specified top-level window.
        
        Note that the number of top-level windows may change between a call to getTopWindowCount() and successive calls to this function.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def getTopWindowCount(self) -> int:
        """
        This function returns the number of currently existing top-level windows.
        """
        ...
    def removeFocusListener(self, xListener: 'XFocusListener_bb8e0bf2') -> None:
        """
        Remove the specified listener from the list of listeners.
        """
        ...
    def removeKeyHandler(self, xHandler: 'XKeyHandler_98520a93') -> None:
        """
        Remove the specified listener from the list of listeners.
        """
        ...
    def removeTopWindowListener(self, xListener: 'XTopWindowListener_efc20d9d') -> None:
        """
        Remove the specified listener from the list of listeners.
        """
        ...


