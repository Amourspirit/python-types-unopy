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
# Namespace: com.sun.star.sdbc
from __future__ import annotations
import typing

from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from ..lang.event_object import EventObject as EventObject_a3d70b03


class XRowSetListener(XEventListener_c7230c4a):
    """
    is used for receiving \"cursorMoved\", \"rowChanged\", and \"rowSetChanged\" events posted by, for example, a row set.

    See Also:
        `API XRowSetListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdbc_1_1XRowSetListener.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sdbc.XRowSetListener'

    def cursorMoved(self, event: EventObject_a3d70b03) -> None:
        """
        is called when a row set's cursor is moved.
        """
        ...
    def rowChanged(self, event: EventObject_a3d70b03) -> None:
        """
        is called when a row is inserted, updated, or deleted.
        """
        ...
    def rowSetChanged(self, event: EventObject_a3d70b03) -> None:
        """
        is called when the row set has changed, or in other words, when the row set has been reexecuted.
        """
        ...



