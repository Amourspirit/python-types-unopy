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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.text.textfield
import typing
from ..text_field import TextField as TextField_90260a56
if typing.TYPE_CHECKING:
    from ...util.date_time import DateTime as DateTime_84de09d3

class DateTime(TextField_90260a56):
    """
    Service Class

    specifies service of a date or time text field.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API DateTime <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1DateTime.html>`_
    """
    @property
    def Adjust(self) -> int:
        """
        contains an offset to the date or time value in minutes.
        """
        ...
    @property
    def DateTimeFormat(self) -> int:
        """
        this is the display format for this field.
        
        Depending on IsDate, this is either a com.sun.star.text.DateDisplayFormat or com.sun.star.text.TimeDisplayFormat.
        
        This property is deprecated and is here only for components that do not support a com.sun.star.util.NumberFormatter.
        """
        ...
    @property
    def DateTimeValue(self) -> 'DateTime_84de09d3':
        """
        the is the content of this field.
        """
        ...
    @property
    def IsDate(self) -> bool:
        """
        If this flag is set to TRUE this field represents a date with an optional time.
        
        If it is set to FALSE only the time is used here.
        """
        ...
    @property
    def IsFixed(self) -> bool:
        """
        If this flag is set to FALSE the date or time is always displayed as the current date or time.
        
        **since**
        
            OOo 1.1.2
        """
        ...
    @property
    def IsFixedLanguage(self) -> bool:
        """
        determines whether changes in language attributes at the position the text field is located also change the number format as appropriate for this language.
        """
        ...
    @property
    def NumberFormat(self) -> int:
        """
        this is the number format for this field
        """
        ...

