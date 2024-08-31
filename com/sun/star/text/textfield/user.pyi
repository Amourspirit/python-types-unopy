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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.text.textfield
from __future__ import annotations
from ..dependent_text_field import DependentTextField as DependentTextField_fed90ded

class User(DependentTextField_fed90ded):
    """
    Service Class

    specifies service of a user defined field.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API User <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1User.html>`_
    """
    @property
    def IsFixedLanguage(self) -> bool:
        """
        determines whether changes in language attributes at the position the text field is located also change the number format as appropriate for this language.
        
        **since**
        
            OOo 1.1.2
        """
        ...
    @IsFixedLanguage.setter
    def IsFixedLanguage(self, value: bool) -> None:
        ...
    @property
    def IsShowFormula(self) -> bool:
        """
        determines if the content is shown as text rather than as value.
        """
        ...
    @IsShowFormula.setter
    def IsShowFormula(self, value: bool) -> None:
        ...
    @property
    def IsVisible(self) -> bool:
        """
        determines if the field is visible.
        """
        ...
    @IsVisible.setter
    def IsVisible(self, value: bool) -> None:
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

