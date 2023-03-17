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
# Namespace: com.sun.star.chart2.data
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class HighlightedRange(object):
    """
    Struct Class


    See Also:
        `API HighlightedRange <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1chart2_1_1data_1_1HighlightedRange.html>`_
    """
    typeName: Literal['com.sun.star.chart2.data.HighlightedRange']

    def __init__(self, RangeRepresentation: typing.Optional[str] = ..., Index: typing.Optional[int] = ..., PreferredColor: typing.Optional[int] = ..., AllowMerginigWithOtherRanges: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            RangeRepresentation (str, optional): RangeRepresentation value.
            Index (int, optional): Index value.
            PreferredColor (int, optional): PreferredColor value.
            AllowMerginigWithOtherRanges (bool, optional): AllowMerginigWithOtherRanges value.
        """
        ...


    @property
    def RangeRepresentation(self) -> str:
        """
        The range representation string of the highlighted range.
        """
        ...


    @property
    def Index(self) -> int:
        """
        Only take the cell at position Index out of the given Range.
        
        If this value is -1 take the whole sequence.
        """
        ...


    @property
    def PreferredColor(self) -> int:
        """
        Use this color for marking the range.
        
        This color may be ignored and replaced by a better fitting color, if it would be otherwise not well visible.
        """
        ...


    @property
    def AllowMerginigWithOtherRanges(self) -> bool:
        """
        If the highlighted range is visually highlighted and this member is TRUE, the range given in RangeRepresentation may be included in a merged range rectangle spanning a bigger range.
        """
        ...


