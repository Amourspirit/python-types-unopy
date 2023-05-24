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
# Namespace: com.sun.star.xml.crypto.sax
from __future__ import annotations
import typing

from ....uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_reference_resolved_listener import XReferenceResolvedListener as XReferenceResolvedListener_3a2d1513


class XReferenceResolvedBroadcaster(XInterface_8f010a43):
    """
    Interface of Reference Resolved Broadcaster.
    
    This interface is used to manipulate reference resolved listener.

    See Also:
        `API XReferenceResolvedBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1sax_1_1XReferenceResolvedBroadcaster.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.xml.crypto.sax.XReferenceResolvedBroadcaster'

    def addReferenceResolvedListener(self, referenceId: int, listener: XReferenceResolvedListener_3a2d1513) -> None:
        """
        Adds a new reference resolved listener for an element collector.
        
        When the element collector has completely collected that element, this listener will receive a notification.
        """
        ...
    def removeReferenceResolvedListener(self, referenceId: int, listener: XReferenceResolvedListener_3a2d1513) -> None:
        """
        Removes a listener from an element collector.
        
        When a listener is removed, it will not receive notification when collection completes.
        """
        ...


