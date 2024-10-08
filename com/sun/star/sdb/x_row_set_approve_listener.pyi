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
# Namespace: com.sun.star.sdb
from __future__ import annotations
import typing

from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from ..lang.event_object import EventObject as EventObject_a3d70b03
    from .row_change_event import RowChangeEvent as RowChangeEvent_ba0c0bc1


class XRowSetApproveListener(XEventListener_c7230c4a):
    """
    is used for approving the moving and changing of row set actions.

    See Also:
        `API XRowSetApproveListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sdb_1_1XRowSetApproveListener.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sdb.XRowSetApproveListener'

    def approveCursorMove(self, event: EventObject_a3d70b03) -> bool:
        """
        is called before a row set's cursor is moved.
        """
        ...
    def approveRowChange(self, event: RowChangeEvent_ba0c0bc1) -> bool:
        """
        is called before a row is inserted, updated, or deleted.
        """
        ...
    def approveRowSetChange(self, event: EventObject_a3d70b03) -> bool:
        """
        is called before a row set is changed, or in other words before a row set is reexecuted.
        """
        ...


