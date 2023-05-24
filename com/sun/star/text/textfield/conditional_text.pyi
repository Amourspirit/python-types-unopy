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
from __future__ import annotations
from ..text_field import TextField as TextField_90260a56

class ConditionalText(TextField_90260a56):
    """
    Service Class

    specifies service of a conditional text field.

    See Also:
        `API ConditionalText <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1ConditionalText.html>`_
    """
    @property
    def Condition(self) -> str:
        """
        contains the condition.
        """
        ...
    @Condition.setter
    def Condition(self, value: str) -> None:
        ...
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
    def FalseContent(self) -> str:
        """
        contains the text that is displayed if the condition evaluates to FALSE.
        """
        ...
    @FalseContent.setter
    def FalseContent(self, value: str) -> None:
        ...
    @property
    def IsConditionTrue(self) -> bool:
        """
        contains the result of the last evaluation of the condition.
        
        This property has to be read/written in file export/import to save and restore the result without initiation of a new evaluation.
        """
        ...
    @IsConditionTrue.setter
    def IsConditionTrue(self, value: bool) -> None:
        ...
    @property
    def TrueContent(self) -> str:
        """
        contains the text that is displayed if the condition evaluates to TRUE.
        """
        ...
    @TrueContent.setter
    def TrueContent(self, value: str) -> None:
        ...

