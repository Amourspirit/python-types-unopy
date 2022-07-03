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
# Namespace: com.sun.star.form.binding
from typing_extensions import Literal
import typing
from ...lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .list_entry_event import ListEntryEvent as ListEntryEvent_37f10f75
    from ...lang.event_object import EventObject as EventObject_a3d70b03

class XListEntryListener(XEventListener_c7230c4a):
    """
    specifies a listener for changes in a string entry list

    See Also:
        `API XListEntryListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1form_1_1binding_1_1XListEntryListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.form.binding.XListEntryListener']

    def allEntriesChanged(self, Source: 'EventObject_a3d70b03') -> None:
        """
        notifies the listener that all entries of the list have changed.
        
        The listener should retrieve the complete new list by calling the XListEntrySource.getAllListEntries() method of the event source (which is denoted by com.sun.star.lang.EventObject.Source).
        """
        ...
    def entryChanged(self, Source: 'ListEntryEvent_37f10f75') -> None:
        """
        notifies the listener that a single entry in the list has change
        """
        ...
    def entryRangeInserted(self, Source: 'ListEntryEvent_37f10f75') -> None:
        """
        notifies the listener that a range of entries has been inserted into the list
        """
        ...
    def entryRangeRemoved(self, Source: 'ListEntryEvent_37f10f75') -> None:
        """
        notifies the listener that a range of entries has been removed from the list
        """
        ...


