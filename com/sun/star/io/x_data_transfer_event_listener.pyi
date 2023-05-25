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
# Namespace: com.sun.star.io
from __future__ import annotations
import typing

from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .data_transfer_event import DataTransferEvent as DataTransferEvent_d2a00ca1


class XDataTransferEventListener(XEventListener_c7230c4a):
    """
    is used to receive callbacks from an importer or exporter.

    See Also:
        `API XDataTransferEventListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XDataTransferEventListener.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.io.XDataTransferEventListener'

    def cancelled(self, aEvent: DataTransferEvent_d2a00ca1) -> None:
        """
        is called when an import or export process has been cancelled.
        """
        ...
    def finished(self, aEvent: DataTransferEvent_d2a00ca1) -> None:
        """
        is called when an import or export process has finished.
        """
        ...



