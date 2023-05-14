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
# Namespace: com.sun.star.text.textfield
import typing
from ..text_field import TextField as TextField_90260a56
if typing.TYPE_CHECKING:
    from ..page_number_type import PageNumberType as PageNumberType_c8ed0c55

class PageNumber(TextField_90260a56):
    """
    Service Class

    specifies service of a page number text field.

    See Also:
        `API PageNumber <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1PageNumber.html>`_
    """
    @property
    def NumberingType(self) -> int:
        """
        determines the type of the numbering.
        """
        ...
    @NumberingType.setter
    def NumberingType(self, value: int) -> None:
        ...
    @property
    def Offset(self) -> int:
        """
        determines an offset value to show a different page number.
        """
        ...
    @Offset.setter
    def Offset(self, value: int) -> None:
        ...
    @property
    def SubType(self) -> 'PageNumberType_c8ed0c55':
        """
        determines which page the field refers to.
        """
        ...
    @SubType.setter
    def SubType(self, value: 'PageNumberType_c8ed0c55') -> None:
        ...
    @property
    def UserText(self) -> str:
        """
        if the user text string is set then it is displayed when the value of NumberingType is set to com.sun.star.style.NumberingType.CHAR_SPECIAL
        """
        ...
    @UserText.setter
    def UserText(self, value: str) -> None:
        ...

