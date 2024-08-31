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
# Namespace: com.sun.star.form
from __future__ import annotations
import typing

from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from ..lang.event_object import EventObject as EventObject_a3d70b03


class XDeleteListener(XEventListener_c7230c4a):
    """
    This is the listener interface for receiving \"approveDelete\" and \"deleted\" events posted by a database form.
    
    \"approveDelete\" may be used to abort a deletion of the current data record.
    
    Please do not use anymore, this interface is superseded by com.sun.star.form.XConfirmDeleteListener.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API XDeleteListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1XDeleteListener.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.form.XDeleteListener'

    def approveDelete(self, aEvent: EventObject_a3d70b03) -> bool:
        """
        is invoked when the current record of the database form will be deleted.
        """
        ...
    def deleted(self, aEvent: EventObject_a3d70b03) -> None:
        """
        is invoked when a database form has finished the delete processing and the data has been successfully deleted from the datasource.
        """
        ...


