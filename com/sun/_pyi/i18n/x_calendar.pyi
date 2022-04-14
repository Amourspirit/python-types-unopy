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
# Namespace: com.sun.star.i18n
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .calendar import Calendar as Calendar_7f2d0962
    from .calendar_item import CalendarItem as CalendarItem_a86c0af1
    from ..lang.locale import Locale as Locale_70d308fa

class XCalendar(XInterface_8f010a43):
    """
    Access to locale specific calendar systems.
    
    **since**
    
        LibreOffice 3.5

    See Also:
        `API XCalendar <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1i18n_1_1XCalendar.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.i18n.XCalendar']

    def addValue(self, nCalendarFieldIndex: int, nAmount: int) -> None:
        """
        Add an amount to a field.
        """
    def getAllCalendars(self, rLocale: 'Locale_70d308fa') -> 'typing.Tuple[str, ...]':
        """
        Returns all available calendars for the given locale.
        """
    def getDateTime(self) -> float:
        """
        Get the UTC date/time as an offset to the start of the calendar at 1-Jan-1970 00:00.
        
        The integer part represents the number of days passed since start date. The fractional part represents fractions of a day, thus 0.5 means 12 hours.
        """
    def getDays(self) -> 'typing.Tuple[CalendarItem_a86c0af1, ...]':
        """
        returns a sequence of CalendarItem describing the day names.
        """
    def getDisplayName(self, nCalendarDisplayIndex: int, nIdx: int, nNameType: int) -> str:
        """
        Returns a string (name to display) matching the given parameters.
        
        The value should be obtained by a previous call to XCalendar.getValue() with an appropriate CalendarFieldIndex argument.
        
        This parameter is not used if the nCalendarDisplayIndex argument equals CalendarDisplayIndex.AM_PM
        
        **since**
        
            LibreOffice 3.5
        """
    def getFirstDayOfWeek(self) -> int:
        """
        returns the first day of a week, one of Weekdays values.
        """
    def getLoadedCalendar(self) -> 'Calendar_7f2d0962':
        """
        Get the currently loaded Calendar.
        """
    def getMinimumNumberOfDaysForFirstWeek(self) -> int:
        """
        returns how many days of a week must reside in the first week of a year.
        """
    def getMonths(self) -> 'typing.Tuple[CalendarItem_a86c0af1, ...]':
        """
        returns a sequence of CalendarItem describing the month names.
        """
    def getNumberOfDaysInWeek(self) -> int:
        """
        returns the number of days in a week, e.g. 7
        """
    def getNumberOfMonthsInYear(self) -> int:
        """
        returns the number of months in a year, e.g. 12
        """
    def getUniqueID(self) -> str:
        """
        Returns the ID string of the loaded calendar, for example, \"Gregorian\"
        """
    def getValue(self, nCalendarFieldIndex: int) -> int:
        """
        Get the value of a field.
        """
    def isValid(self) -> bool:
        """
        Verify if the date fields set by a combination of XCalendar.setValue() calls is valid.
        
        It has a side-effect because it will internally calculate the final value for the date fields
        """
    def loadCalendar(self, uniqueID: str, rLocale: 'Locale_70d308fa') -> None:
        """
        Load a specific calendar for the given locale.
        """
    def loadDefaultCalendar(self, rLocale: 'Locale_70d308fa') -> None:
        """
        Load the default calendar for the given locale.
        """
    def setDateTime(self, nTimeInDays: float) -> None:
        """
        Set the UTC date/time as an offset to the start of the calendar at 1-Jan-1970 00:00.
        
        The integer part represents the number of days passed since start date. The fractional part represents fractions of a day, thus 0.5 means 12 hours.
        """
    def setFirstDayOfWeek(self, nDay: int) -> None:
        """
        Set the first day of a week, one of Weekdays values.
        """
    def setMinimumNumberOfDaysForFirstWeek(self, nDays: int) -> None:
        """
        Set how many days of a week must reside in the first week of a year.
        """
    def setValue(self, nCalendarFieldIndex: int, nValue: int) -> None:
        """
        Set the value of a field.
        """

__all__ = ['XCalendar']

