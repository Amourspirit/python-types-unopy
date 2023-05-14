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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.util
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class DateTimeRange(object):
    """
    Struct Class

    represents a range of date+time values.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API DateTimeRange <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1DateTimeRange.html>`_
    """
    typeName: Literal['com.sun.star.util.DateTimeRange']

    def __init__(self, StartNanoSeconds: typing.Optional[int] = ..., StartSeconds: typing.Optional[int] = ..., StartMinutes: typing.Optional[int] = ..., StartHours: typing.Optional[int] = ..., StartDay: typing.Optional[int] = ..., StartMonth: typing.Optional[int] = ..., StartYear: typing.Optional[int] = ..., EndNanoSeconds: typing.Optional[int] = ..., EndSeconds: typing.Optional[int] = ..., EndMinutes: typing.Optional[int] = ..., EndHours: typing.Optional[int] = ..., EndDay: typing.Optional[int] = ..., EndMonth: typing.Optional[int] = ..., EndYear: typing.Optional[int] = ..., IsUTC: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            StartNanoSeconds (int, optional): StartNanoSeconds value.
            StartSeconds (int, optional): StartSeconds value.
            StartMinutes (int, optional): StartMinutes value.
            StartHours (int, optional): StartHours value.
            StartDay (int, optional): StartDay value.
            StartMonth (int, optional): StartMonth value.
            StartYear (int, optional): StartYear value.
            EndNanoSeconds (int, optional): EndNanoSeconds value.
            EndSeconds (int, optional): EndSeconds value.
            EndMinutes (int, optional): EndMinutes value.
            EndHours (int, optional): EndHours value.
            EndDay (int, optional): EndDay value.
            EndMonth (int, optional): EndMonth value.
            EndYear (int, optional): EndYear value.
            IsUTC (bool, optional): IsUTC value.
        """
        ...


    @property
    def StartNanoSeconds(self) -> int:
        """
        contains the start nanoseconds (0 - 999 999 999) for the range.
        """
        ...

    @StartNanoSeconds.setter
    def StartNanoSeconds(self, value: int) -> None:
        ...

    @property
    def StartSeconds(self) -> int:
        """
        contains the start seconds (0-59) for the range.
        """
        ...

    @StartSeconds.setter
    def StartSeconds(self, value: int) -> None:
        ...

    @property
    def StartMinutes(self) -> int:
        """
        contains the start minutes (0-59) for the range.
        """
        ...

    @StartMinutes.setter
    def StartMinutes(self, value: int) -> None:
        ...

    @property
    def StartHours(self) -> int:
        """
        contains the start hour (0-23) for the range.
        """
        ...

    @StartHours.setter
    def StartHours(self, value: int) -> None:
        ...

    @property
    def StartDay(self) -> int:
        """
        contains the start day of month (1-31 or 0 for a void date) for the range.
        """
        ...

    @StartDay.setter
    def StartDay(self, value: int) -> None:
        ...

    @property
    def StartMonth(self) -> int:
        """
        contains the start month of year (1-12 or 0 for a void date) for the range.
        """
        ...

    @StartMonth.setter
    def StartMonth(self, value: int) -> None:
        ...

    @property
    def StartYear(self) -> int:
        """
        contains the start year for the range.
        """
        ...

    @StartYear.setter
    def StartYear(self, value: int) -> None:
        ...

    @property
    def EndNanoSeconds(self) -> int:
        """
        contains the end nanoseconds (0 - 999 999 999) for the range.
        """
        ...

    @EndNanoSeconds.setter
    def EndNanoSeconds(self, value: int) -> None:
        ...

    @property
    def EndSeconds(self) -> int:
        """
        contains the end seconds (0-59) for the range.
        """
        ...

    @EndSeconds.setter
    def EndSeconds(self, value: int) -> None:
        ...

    @property
    def EndMinutes(self) -> int:
        """
        contains the end minutes (0-59) for the range.
        """
        ...

    @EndMinutes.setter
    def EndMinutes(self, value: int) -> None:
        ...

    @property
    def EndHours(self) -> int:
        """
        contains the end hour (0-23) for the range.
        """
        ...

    @EndHours.setter
    def EndHours(self, value: int) -> None:
        ...

    @property
    def EndDay(self) -> int:
        """
        contains the end day of month (1-31 or 0 for a void date) for the range.
        """
        ...

    @EndDay.setter
    def EndDay(self, value: int) -> None:
        ...

    @property
    def EndMonth(self) -> int:
        """
        contains the end month of year (1-12 or 0 for a void date) for the range.
        """
        ...

    @EndMonth.setter
    def EndMonth(self, value: int) -> None:
        ...

    @property
    def EndYear(self) -> int:
        """
        contains the end year for the range.
        """
        ...

    @EndYear.setter
    def EndYear(self, value: int) -> None:
        ...

    @property
    def IsUTC(self) -> bool:
        """
        true: time zone is UTC false: unknown time zone.
        
        **since**
        
            LibreOffice 4.1
        """
        ...

    @IsUTC.setter
    def IsUTC(self, value: bool) -> None:
        ...

