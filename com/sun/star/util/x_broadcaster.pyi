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
# Namespace: com.sun.star.util
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XBroadcaster(XInterface_8f010a43):
    """
    allows to control notification behavior of a broadcaster.
    
    **since**
    
        OOo 3.0

    See Also:
        `API XBroadcaster <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1util_1_1XBroadcaster.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.util.XBroadcaster'

    def lockBroadcasts(self) -> None:
        """
        suspends broadcasts to the registered listeners.
        
        The calls to XBroadcaster.lockBroadcasts() and XBroadcaster.unlockBroadcasts() may be nested and even overlapping, but they must be in pairs. While there is at least one lock remaining, no broadcasts are sent to registered listeners.
        """
        ...
    def unlockBroadcasts(self) -> None:
        """
        resumes the broadcasts which were suspended by XBroadcaster.lockBroadcasts().
        
        The calls to XBroadcaster.lockBroadcasts() and XBroadcaster.unlockBroadcasts() may be nested and even overlapping, but they must be in pairs. While there is at least one lock remaining, no broadcasts are sent to registered listeners.
        
        Pending broadcasts will be sent immediately after the last call to XBroadcaster.lockBroadcasts() is matched by a call to XBroadcaster.unlockBroadcasts(). An implementation can decide to broadcast all pending notification in order or batch them in single broadcasts.
        """
        ...



