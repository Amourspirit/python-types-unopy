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
# Namespace: com.sun.star.i18n
# Libre Office Version: 2024.2
import typing
from .calendar_item2 import CalendarItem2 as CalendarItem2_b38f0b23


class Calendar2(object):
    """
    Struct Class

    Calendar items as returned in a sequence by XLocaleData3.getAllCalendars2().
    
    Similar to com.sun.star.i18n.Calendar this provides additional members with a sequence of possessive (genitive case) and partitive case month names for locales that use them, for example Slavic locales. If a locale does not provide the possessive form in GenitiveMonths, the names are identical to the nominative case nouns in Calendar.Months. If a locale does not provide the partitive case in PartitiveMonths, the names are identical to GenitiveMonths.
    
    The sequences are of type com.sun.star.i18n.CalendarItem2 instead of com.sun.star.i18n.CalendarItem, with the additional NarrowName member.
    
    **since**
    
        LibreOffice 3.5

    See Also:
        `API Calendar2 <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1Calendar2.html>`_
    """
    typeName: str = 'com.sun.star.i18n.Calendar2'

    def __init__(self, Days: typing.Optional[typing.Tuple[CalendarItem2_b38f0b23, ...]] = ..., Months: typing.Optional[typing.Tuple[CalendarItem2_b38f0b23, ...]] = ..., GenitiveMonths: typing.Optional[typing.Tuple[CalendarItem2_b38f0b23, ...]] = ..., PartitiveMonths: typing.Optional[typing.Tuple[CalendarItem2_b38f0b23, ...]] = ..., Eras: typing.Optional[typing.Tuple[CalendarItem2_b38f0b23, ...]] = ..., StartOfWeek: typing.Optional[str] = ..., MinimumNumberOfDaysForFirstWeek: typing.Optional[int] = ..., Default: typing.Optional[bool] = ..., Name: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            Days (typing.Tuple[CalendarItem2, ...], optional): Days value.
            Months (typing.Tuple[CalendarItem2, ...], optional): Months value.
            GenitiveMonths (typing.Tuple[CalendarItem2, ...], optional): GenitiveMonths value.
            PartitiveMonths (typing.Tuple[CalendarItem2, ...], optional): PartitiveMonths value.
            Eras (typing.Tuple[CalendarItem2, ...], optional): Eras value.
            StartOfWeek (str, optional): StartOfWeek value.
            MinimumNumberOfDaysForFirstWeek (int, optional): MinimumNumberOfDaysForFirstWeek value.
            Default (bool, optional): Default value.
            Name (str, optional): Name value.
        """
        ...

    @property
    def Days(self) -> typing.Tuple[CalendarItem2_b38f0b23, ...]:
        """
        The days of the week.
        """
        ...
    @Days.setter
    def Days(self, value: typing.Tuple[CalendarItem2_b38f0b23, ...]) -> None:
        ...
    @property
    def Months(self) -> typing.Tuple[CalendarItem2_b38f0b23, ...]:
        """
        The months of the year.
        """
        ...
    @Months.setter
    def Months(self, value: typing.Tuple[CalendarItem2_b38f0b23, ...]) -> None:
        ...
    @property
    def GenitiveMonths(self) -> typing.Tuple[CalendarItem2_b38f0b23, ...]:
        """
        The months of the year in possessive genitive case.
        """
        ...
    @GenitiveMonths.setter
    def GenitiveMonths(self, value: typing.Tuple[CalendarItem2_b38f0b23, ...]) -> None:
        ...
    @property
    def PartitiveMonths(self) -> typing.Tuple[CalendarItem2_b38f0b23, ...]:
        """
        The months of the year in partitive case.
        """
        ...
    @PartitiveMonths.setter
    def PartitiveMonths(self, value: typing.Tuple[CalendarItem2_b38f0b23, ...]) -> None:
        ...
    @property
    def Eras(self) -> typing.Tuple[CalendarItem2_b38f0b23, ...]:
        """
        The possible eras.
        """
        ...
    @Eras.setter
    def Eras(self, value: typing.Tuple[CalendarItem2_b38f0b23, ...]) -> None:
        ...
    @property
    def StartOfWeek(self) -> str:
        """
        The ID of the day with which the week begins.
        """
        ...
    @StartOfWeek.setter
    def StartOfWeek(self, value: str) -> None:
        ...
    @property
    def MinimumNumberOfDaysForFirstWeek(self) -> int:
        """
        How many days must reside in the first week of a year.
        """
        ...
    @MinimumNumberOfDaysForFirstWeek.setter
    def MinimumNumberOfDaysForFirstWeek(self, value: int) -> None:
        ...
    @property
    def Default(self) -> bool:
        """
        If this is the default calendar for a given locale.
        """
        ...
    @Default.setter
    def Default(self, value: bool) -> None:
        ...
    @property
    def Name(self) -> str:
        """
        The name of the calendar, for example, Gregorian.
        """
        ...
    @Name.setter
    def Name(self, value: str) -> None:
        ...

