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
# Namespace: com.sun.star.datatransfer.clipboard
from __future__ import annotations
import typing

from .x_clipboard_ex import XClipboardEx as XClipboardEx_c626128a
from .x_clipboard_notifier import XClipboardNotifier as XClipboardNotifier_3e4e150d
from .x_flushable_clipboard import XFlushableClipboard as XFlushableClipboard_53ae1563
from ...lang.x_component import XComponent as XComponent_98dc0ab5


class XSystemClipboard(XClipboardEx_c626128a, XClipboardNotifier_3e4e150d, XFlushableClipboard_53ae1563, XComponent_98dc0ab5):
    """
    Provides a unified interface for new-style service SystemClipboard.
    
    **since**
    
        LibreOffice 4.2

    See Also:
        `API XSystemClipboard <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1clipboard_1_1XSystemClipboard.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.datatransfer.clipboard.XSystemClipboard'


