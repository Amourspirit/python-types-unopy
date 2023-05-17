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
# Namespace: com.sun.star.datatransfer.clipboard
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..x_transferable import XTransferable as XTransferable_2d800f38
    from .x_clipboard_owner import XClipboardOwner as XClipboardOwner_8713d8


class XClipboard(XInterface_8f010a43):
    """

    See Also:
        `API XClipboard <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1clipboard_1_1XClipboard.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.datatransfer.clipboard.XClipboard']

    def getContents(self) -> 'XTransferable_2d800f38':
        """
        To get the current content of the clipboard.
        """
        ...
    def getName(self) -> str:
        """
        To get the name of the clipboard instance.
        
        If the returned string is empty the clipboard instance is the system clipboard.
        """
        ...
    def setContents(self, xTrans: 'XTransferable_2d800f38', xClipboardOwner: 'XClipboardOwner_8713d8') -> None:
        """
        Sets the current contents of the clipboard to the specified transferable object and registers the specified clipboard owner as the owner of the new contents.
        
        If the given com.sun.star.datatransfer.XTransferable has no com.sun.star.datatransfer.DataFlavor the clipboard will be deleted.
        
        A NULL value is not allowed.
        
        NULL is an acceptable value and means that the caller is not interested in lost ownership notifications.
        """
        ...


