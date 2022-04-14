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
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.2
from typing_extensions import Literal
import typing


class LocaleDataItem(object):
    """
    Struct Class

    Locale specific data, for example, separators, quotation marks.

    See Also:
        `API LocaleDataItem <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1LocaleDataItem.html>`_
    """
    typeName: Literal['com.sun.star.i18n.LocaleDataItem']

    def __init__(self, unoID: typing.Optional[str] = ..., dateSeparator: typing.Optional[str] = ..., thousandSeparator: typing.Optional[str] = ..., decimalSeparator: typing.Optional[str] = ..., timeSeparator: typing.Optional[str] = ..., time100SecSeparator: typing.Optional[str] = ..., listSeparator: typing.Optional[str] = ..., quotationStart: typing.Optional[str] = ..., quotationEnd: typing.Optional[str] = ..., doubleQuotationStart: typing.Optional[str] = ..., doubleQuotationEnd: typing.Optional[str] = ..., timeAM: typing.Optional[str] = ..., timePM: typing.Optional[str] = ..., measurementSystem: typing.Optional[str] = ..., LongDateDayOfWeekSeparator: typing.Optional[str] = ..., LongDateDaySeparator: typing.Optional[str] = ..., LongDateMonthSeparator: typing.Optional[str] = ..., LongDateYearSeparator: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            unoID (str, optional): unoID value.
            dateSeparator (str, optional): dateSeparator value.
            thousandSeparator (str, optional): thousandSeparator value.
            decimalSeparator (str, optional): decimalSeparator value.
            timeSeparator (str, optional): timeSeparator value.
            time100SecSeparator (str, optional): time100SecSeparator value.
            listSeparator (str, optional): listSeparator value.
            quotationStart (str, optional): quotationStart value.
            quotationEnd (str, optional): quotationEnd value.
            doubleQuotationStart (str, optional): doubleQuotationStart value.
            doubleQuotationEnd (str, optional): doubleQuotationEnd value.
            timeAM (str, optional): timeAM value.
            timePM (str, optional): timePM value.
            measurementSystem (str, optional): measurementSystem value.
            LongDateDayOfWeekSeparator (str, optional): LongDateDayOfWeekSeparator value.
            LongDateDaySeparator (str, optional): LongDateDaySeparator value.
            LongDateMonthSeparator (str, optional): LongDateMonthSeparator value.
            LongDateYearSeparator (str, optional): LongDateYearSeparator value.
        """


    @property
    def unoID(self) -> str:
        """
        internal ID string, not unique, not meaningful to the outer world
        """


    @property
    def dateSeparator(self) -> str:
        """
        date separator, for example, \"/\" or \".\" or \"-\"
        """


    @property
    def thousandSeparator(self) -> str:
        """
        group and thousand separator, for example, \",\" or \".\"
        """


    @property
    def decimalSeparator(self) -> str:
        """
        decimal separator, for example, \".\" or \",\"
        """


    @property
    def timeSeparator(self) -> str:
        """
        time separator, for example, \":\"
        """


    @property
    def time100SecSeparator(self) -> str:
        """
        time 100th seconds separator, for example, \",\"
        """


    @property
    def listSeparator(self) -> str:
        """
        list separator, for example, \";\"
        """


    @property
    def quotationStart(self) -> str:
        """
        single quotation mark start
        """


    @property
    def quotationEnd(self) -> str:
        """
        single quotation mark end
        """


    @property
    def doubleQuotationStart(self) -> str:
        """
        double quotation mark start
        """


    @property
    def doubleQuotationEnd(self) -> str:
        """
        double quotation mark end
        """


    @property
    def timeAM(self) -> str:
        """
        time AM symbol, for example, \"AM\" or \"am\"
        """


    @property
    def timePM(self) -> str:
        """
        time PM symbol, for example, \"PM\" or \"pm\"
        """


    @property
    def measurementSystem(self) -> str:
        """
        measurement system, \"metric\" or \"us\"
        """


    @property
    def LongDateDayOfWeekSeparator(self) -> str:
        """
        long date day of week separator, for example, \", \"
        """


    @property
    def LongDateDaySeparator(self) -> str:
        """
        long date day separator, for example, \", \"
        """


    @property
    def LongDateMonthSeparator(self) -> str:
        """
        long date month separator, for example, \" \"
        """


    @property
    def LongDateYearSeparator(self) -> str:
        """
        long date year separator, for example, \" \"
        """



__all__ = ['LocaleDataItem']
