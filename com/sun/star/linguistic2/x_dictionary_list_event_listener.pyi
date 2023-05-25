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
# Namespace: com.sun.star.linguistic2
from __future__ import annotations
import typing

from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .dictionary_list_event import DictionaryListEvent as DictionaryListEvent_7cdd1129


class XDictionaryListEventListener(XEventListener_c7230c4a):
    """
    This interfaces allows the object to act according to dictionary-list events.
    
    This interface is the base class for all dictionary-list event listeners. Its single function will be called by the broadcasting dictionary-list in order to notify its registered listeners.

    See Also:
        `API XDictionaryListEventListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1linguistic2_1_1XDictionaryListEventListener.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.linguistic2.XDictionaryListEventListener'

    def processDictionaryListEvent(self, aDicListEvent: DictionaryListEvent_7cdd1129) -> None:
        """
        is used to notify the object about dictionary-list events.
        """
        ...


