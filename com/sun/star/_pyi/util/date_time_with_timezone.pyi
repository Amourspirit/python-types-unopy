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
# Namespace: com.sun.star.util
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing
from .date_time import DateTime as DateTime_84de09d3


class DateTimeWithTimezone(object):
    """
    Struct Class

    represents a combined date+time value with time zone.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API DateTimeWithTimezone <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1DateTimeWithTimezone.html>`_
    """
    typeName: Literal['com.sun.star.util.DateTimeWithTimezone']

    def __init__(self, DateTimeInTZ: typing.Optional[DateTime_84de09d3] = ..., Timezone: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            DateTimeInTZ (DateTime, optional): DateTimeInTZ value.
            Timezone (int, optional): Timezone value.
        """
        ...


    @property
    def DateTimeInTZ(self) -> DateTime_84de09d3:
        """
        the date and time (in TimeZone)
        """
        ...


    @property
    def Timezone(self) -> int:
        """
        contains the time zone, as signed offset in minutes from UTC, that is east of UTC, that is the amount of minutes that should be added to UTC time to obtain the time in that timezone.
        
        To obtain UTC datetime from DateTimeInTZ, you need to subtract TimeZone minutes.
        """
        ...


