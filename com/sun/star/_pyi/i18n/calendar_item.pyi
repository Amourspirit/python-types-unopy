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
# Namespace: com.sun.star.i18n
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing


class CalendarItem(object):
    """
    Struct Class

    One entry in a calendar, for example, a day of week or a month or an era.
    
    A sequence of CalendarItems is contained in Calendar.Days, Calendar.Months, Calendar.Eras

    See Also:
        `API CalendarItem <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1i18n_1_1CalendarItem.html>`_
    """
    typeName: Literal['com.sun.star.i18n.CalendarItem']

    def __init__(self, ID: typing.Optional[str] = ..., AbbrevName: typing.Optional[str] = ..., FullName: typing.Optional[str] = ...) -> None:
        """
        Constructor

        Arguments:
            ID (str, optional): ID value.
            AbbrevName (str, optional): AbbrevName value.
            FullName (str, optional): FullName value.
        """
        ...


    @property
    def ID(self) -> str:
        """
        A unique ID for an entry of this type, usually the lower case abbreviated English name, for example, \"sun\" for Sunday.
        """
        ...

    @ID.setter
    def ID(self, value: str) -> None:
        ...

    @property
    def AbbrevName(self) -> str:
        """
        The abbreviated name, for example, \"Sun\".
        """
        ...

    @AbbrevName.setter
    def AbbrevName(self, value: str) -> None:
        ...

    @property
    def FullName(self) -> str:
        """
        The full name, for example, \"Sunday\".
        """
        ...

    @FullName.setter
    def FullName(self, value: str) -> None:
        ...

