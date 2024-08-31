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
# Namespace: com.sun.star.frame
from __future__ import annotations
import typing

from ..container.x_set import XSet as XSet_90c40a4f
from ..document.x_document_event_broadcaster import XDocumentEventBroadcaster as XDocumentEventBroadcaster_b2f1126a
from ..document.x_document_event_listener import XDocumentEventListener as XDocumentEventListener_7db01146
from ..document.x_events_supplier import XEventsSupplier as XEventsSupplier_ecd0e88


class XGlobalEventBroadcaster(XSet_90c40a4f, XDocumentEventBroadcaster_b2f1126a, XDocumentEventListener_7db01146, XEventsSupplier_ecd0e88):
    """
    Provides the unified interface of theGlobalEventBroadcaster singleton.
    
    **since**
    
        LibreOffice 4.0

    See Also:
        `API XGlobalEventBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XGlobalEventBroadcaster.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.frame.XGlobalEventBroadcaster'


