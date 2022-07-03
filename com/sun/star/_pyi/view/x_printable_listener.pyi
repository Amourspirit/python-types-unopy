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
# Libre Office Version: 7.2
# Namespace: com.sun.star.view
from typing_extensions import Literal
import typing
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .printable_state_event import PrintableStateEvent as PrintableStateEvent_db30e67

class XPrintableListener(XEventListener_c7230c4a):
    """
    receives events about print job progress.
    
    XPrintableListener can be registered to XPrintableBroadcaster. Then, the client object will receive events about print progress.

    See Also:
        `API XPrintableListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1view_1_1XPrintableListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.view.XPrintableListener']

    def stateChanged(self, Event: 'PrintableStateEvent_db30e67') -> None:
        """
        informs the user of the new state in print progress.
        """
        ...


