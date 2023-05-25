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
# Namespace: com.sun.star.sheet
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .data_pilot_field_group_info import DataPilotFieldGroupInfo as DataPilotFieldGroupInfo_56691020
    from .x_data_pilot_field import XDataPilotField as XDataPilotField_e0350cdf


class XDataPilotFieldGrouping(XInterface_8f010a43):
    """
    Provides methods to create new DataPilot fields where some or all items of this DataPilot field are grouped in some way.

    See Also:
        `API XDataPilotFieldGrouping <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1sheet_1_1XDataPilotFieldGrouping.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.sheet.XDataPilotFieldGrouping'

    def createDateGroup(self, aInfo: DataPilotFieldGroupInfo_56691020) -> XDataPilotField_e0350cdf:
        """
        Groups the members of this field by dates, according to the passed settings.
        
        If this field is already grouped by dates, a new DataPilot field will be created and returned. If this field is not grouped at all, the date grouping is performed inside of this field (no new field will be created). There must not be any other grouping (by member names or by numeric ranges), otherwise an exception is thrown.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def createNameGroup(self, aItems: typing.Tuple[str, ...]) -> XDataPilotField_e0350cdf:
        """
        Creates a new DataPilot field which contains a group containing the given DataPilot field items (members).
        
        It is possible to create multiple groups by calling this method several times at the same DataPilot field. On subsequent calls, the DataPilot field created at the first call is used to insert the new groups.
        
        The collection of groups can be accessed via the DataPilotField.GroupInfo property. The returned struct contains the sequence of groups in its member DataPilotFieldGroupInfo.Groups.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...



