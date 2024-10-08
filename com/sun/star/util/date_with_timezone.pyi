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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.util
# Libre Office Version: 2024.2
import typing
from .date import Date as Date_60040844


class DateWithTimezone(object):
    """
    Struct Class

    represents a date value with time zone.
    
    **since**
    
        LibreOffice 4.1

    See Also:
        `API DateWithTimezone <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1util_1_1DateWithTimezone.html>`_
    """
    typeName: str = 'com.sun.star.util.DateWithTimezone'

    def __init__(self, DateInTZ: typing.Optional[Date_60040844] = ..., Timezone: typing.Optional[int] = ...) -> None:
        """
        Constructor

        Arguments:
            DateInTZ (Date, optional): DateInTZ value.
            Timezone (int, optional): Timezone value.
        """
        ...

    @property
    def DateInTZ(self) -> Date_60040844:
        """
        the date.
        """
        ...
    @DateInTZ.setter
    def DateInTZ(self, value: Date_60040844) -> None:
        ...
    @property
    def Timezone(self) -> int:
        """
        contains the time zone, as signed offset in minutes from UTC, that is east of UTC, that is the amount of minutes that should be added to UTC time to obtain time in that timezone.
        """
        ...
    @Timezone.setter
    def Timezone(self, value: int) -> None:
        ...

