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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.i18n
import typing


class CalendarDisplayCode:
    """
    Const

    Constants to use with XExtendedCalendar.getDisplayString().
    
    The examples given are for an English Gregorian calendar, note that other calendars or locales may return completely different strings, for example not a four digit year but a CJK name instead.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API CalendarDisplayCode <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1i18n_1_1CalendarDisplayCode.html>`_
    """
    SHORT_DAY: int = ...
    """
    Day of month, one or two digits, no leading zero.
    """
    LONG_DAY: int = ...
    """
    Day of month, two digits, with leading zero.
    """
    SHORT_DAY_NAME: int = ...
    """
    Day of week, abbreviated name.
    """
    LONG_DAY_NAME: int = ...
    """
    Day of week, full name.
    """
    SHORT_MONTH: int = ...
    """
    Month of year, one or two digits, no leading zero.
    """
    LONG_MONTH: int = ...
    """
    Month of year, with leading zero.
    """
    SHORT_MONTH_NAME: int = ...
    """
    Abbreviated month name.
    """
    LONG_MONTH_NAME: int = ...
    """
    Full month name.
    """
    SHORT_YEAR: int = ...
    """
    Year, two digits.
    """
    LONG_YEAR: int = ...
    """
    Year, four digits.
    """
    SHORT_ERA: int = ...
    """
    Abbreviated era name, for example, BC or AD.
    """
    LONG_ERA: int = ...
    """
    Full era name, for example, \"Before Christ\" or \"Anno Dominus\".
    """
    SHORT_YEAR_AND_ERA: int = ...
    """
    Combined short year and era, order depends on locale/calendar.
    """
    LONG_YEAR_AND_ERA: int = ...
    """
    Combined full year and era, order depends on locale/calendar.
    """
    SHORT_QUARTER: int = ...
    """
    Short quarter, for example, \"Q1\".
    """
    LONG_QUARTER: int = ...
    """
    Long quarter, for example, \"1st quarter\".
    """
    SHORT_GENITIVE_MONTH_NAME: int = ...
    """
    Abbreviated possessive genitive case month name.
    
    **since**
    
        LibreOffice 3.5
    """
    LONG_GENITIVE_MONTH_NAME: int = ...
    """
    Full possessive genitive case month name.
    
    **since**
    
        LibreOffice 3.5
    """
    NARROW_GENITIVE_MONTH_NAME: int = ...
    """
    Narrow possessive genitive case month name.
    
    **since**
    
        LibreOffice 3.5
    """
    SHORT_PARTITIVE_MONTH_NAME: int = ...
    """
    Abbreviated partitive case month name.
    
    **since**
    
        LibreOffice 3.5
    """
    LONG_PARTITIVE_MONTH_NAME: int = ...
    """
    Full partitive case month name.
    
    **since**
    
        LibreOffice 3.5
    """
    NARROW_PARTITIVE_MONTH_NAME: int = ...
    """
    Narrow partitive case month name.
    
    **since**
    
        LibreOffice 3.5
    """
    NARROW_DAY_NAME: int = ...
    """
    Day of week, narrow name.
    
    **since**
    
        LibreOffice 3.5
    """
    NARROW_MONTH_NAME: int = ...
    """
    Narrow month name.
    
    **since**
    
        LibreOffice 3.5
    """

