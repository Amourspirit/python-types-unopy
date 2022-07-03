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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.sheet
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing
from ..container.x_name_access import XNameAccess as XNameAccess_e2ab0cf6
from .x_data_pilot_field import XDataPilotField as XDataPilotField_e0350cdf


class DataPilotFieldGroupInfo(object):
    """
    Struct Class

    contains the grouping information of a DataPilotField.

    See Also:
        `API DataPilotFieldGroupInfo <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1sheet_1_1DataPilotFieldGroupInfo.html>`_
    """
    typeName: Literal['com.sun.star.sheet.DataPilotFieldGroupInfo']

    def __init__(self, HasAutoStart: typing.Optional[bool] = ..., HasAutoEnd: typing.Optional[bool] = ..., HasDateValues: typing.Optional[bool] = ..., Start: typing.Optional[float] = ..., End: typing.Optional[float] = ..., Step: typing.Optional[float] = ..., GroupBy: typing.Optional[int] = ..., SourceField: typing.Optional[XDataPilotField_e0350cdf] = ..., Groups: typing.Optional[XNameAccess_e2ab0cf6] = ...) -> None:
        """
        Constructor

        Arguments:
            HasAutoStart (bool, optional): HasAutoStart value.
            HasAutoEnd (bool, optional): HasAutoEnd value.
            HasDateValues (bool, optional): HasDateValues value.
            Start (float, optional): Start value.
            End (float, optional): End value.
            Step (float, optional): Step value.
            GroupBy (int, optional): GroupBy value.
            SourceField (XDataPilotField, optional): SourceField value.
            Groups (XNameAccess, optional): Groups value.
        """
        ...


    @property
    def HasAutoStart(self) -> bool:
        """
        specifies whether the start value for the grouping is taken automatically from the minimum of the item values.
        """
        ...


    @property
    def HasAutoEnd(self) -> bool:
        """
        specifies whether the end value for the grouping is taken automatically from the maximum of the item values.
        """
        ...


    @property
    def HasDateValues(self) -> bool:
        """
        specifies whether date values are grouped by ranges of days.
        """
        ...


    @property
    def Start(self) -> float:
        """
        specifies the start value for the grouping if HasAutoStart is set to FALSE.
        """
        ...


    @property
    def End(self) -> float:
        """
        specifies the end value for the grouping if HasAutoEnd is set to FALSE.
        """
        ...


    @property
    def Step(self) -> float:
        """
        specifies the size of the ranges for numeric or day grouping.
        
        Example: With HasAutoStart set to FALSE, Start set to 2, and Step set to 3, the first group will contain all values greater than or equal to 2 and less than 5. The second group will contain all values greater than or equal to 5 and less than 8, and so on.
        """
        ...


    @property
    def GroupBy(self) -> int:
        """
        specifies the grouping of the date values.
        """
        ...


    @property
    def SourceField(self) -> XDataPilotField_e0350cdf:
        """
        contains the source DataPilot field grouping is based on.
        
        Will be NULL if this field is not grouped or contains numeric grouping.
        """
        ...


    @property
    def Groups(self) -> XNameAccess_e2ab0cf6:
        """
        specifies the named groups in this field if there are some.
        
        The returned object is an instance of DataPilotFieldGroups . The collection of groups can be modified by inserting, removing, replacing, or renaming single groups or item names in the groups. When writing back this struct containing such a changed collection of groups to the DataPilotField.GroupInfo property, the modified grouping settings are applied at the DataPilot field.
        """
        ...


