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

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_session_manager_listener import XSessionManagerListener as XSessionManagerListener_582d1050


class XSessionManagerClient(XInterface_8f010a43):
    """
    Connect to a session manager to get information about pending desktop shutdown.

    See Also:
        `API XSessionManagerClient <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1frame_1_1XSessionManagerClient.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.frame.XSessionManagerClient'

    def addSessionManagerListener(self, xListener: XSessionManagerListener_582d1050) -> None:
        """
        addSessionManagerListener registers a listener for session management events
        """
        ...
    def cancelShutdown(self) -> bool:
        """
        Call cancelShutdown to try to cancel a desktop shutdown in progress.
        """
        ...
    def interactionDone(self, xListener: XSessionManagerListener_582d1050) -> None:
        """
        interactionDone is called when a listener has finished user interaction
        """
        ...
    def queryInteraction(self, xListener: XSessionManagerListener_582d1050) -> None:
        """
        queryInteraction issues a request for a user interaction slot from the session manager
        """
        ...
    def removeSessionManagerListener(self, xListener: XSessionManagerListener_582d1050) -> None:
        """
        removeSessionManagerListener deregisters a listener for session events
        """
        ...
    def saveDone(self, xListener: XSessionManagerListener_582d1050) -> None:
        """
        saveDone signals that a listener has processed a save request
        """
        ...


