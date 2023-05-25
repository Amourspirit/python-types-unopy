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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.text.textfield.docinfo
from __future__ import annotations
from ...text_field import TextField as TextField_90260a56

class CreateDateTime(TextField_90260a56):
    """
    Service Class

    specifies service of a text field that provides information about the date and time of the document creation.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API CreateDateTime <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1docinfo_1_1CreateDateTime.html>`_
    """
    @property
    def CurrentPresentation(self) -> str:
        """
        contains the current content of the text field.
        
        This property is especially useful for import/export purposes.
        """
        ...
    @CurrentPresentation.setter
    def CurrentPresentation(self, value: str) -> None:
        ...
    @property
    def DateTimeValue(self) -> float:
        """
        contains the date and time as double value.
        """
        ...
    @DateTimeValue.setter
    def DateTimeValue(self, value: float) -> None:
        ...
    @property
    def IsDate(self) -> bool:
        """
        If this flag is set to TRUE this field represents, a date with an optional time.
        
        If it is set to FALSE only the time is used here.
        """
        ...
    @IsDate.setter
    def IsDate(self, value: bool) -> None:
        ...
    @property
    def IsFixed(self) -> bool:
        """
        If this flag is set to false the author will be overridden by the current author each time the document is saved.
        
        If this flag is set to FALSE the date or time is always displayed as the current date or time.
        
        **since**
        
            OOo 1.1.2
        """
        ...
    @IsFixed.setter
    def IsFixed(self, value: bool) -> None:
        ...
    @property
    def IsFixedLanguage(self) -> bool:
        """
        determines whether changes in language attributes at the position the text field is located also change the number format as appropriate for this language.
        """
        ...
    @IsFixedLanguage.setter
    def IsFixedLanguage(self, value: bool) -> None:
        ...
    @property
    def NumberFormat(self) -> int:
        """
        this is the number format for this field.
        """
        ...
    @NumberFormat.setter
    def NumberFormat(self, value: int) -> None:
        ...
