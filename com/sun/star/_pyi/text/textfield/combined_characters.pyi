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
from ..text_field import TextField as TextField_90260a56

class CombinedCharacters(TextField_90260a56):
    """
    Service Class

    specifies service of a text field to combine 1 to 6 characters that are treated as one normal character.

    See Also:
        `API CombinedCharacters <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1text_1_1textfield_1_1CombinedCharacters.html>`_
    """
    @property
    def Content(self) -> str:
        """
        contains the characters to be combined.
        """
        ...
    @Content.setter
    def Content(self, value: str) -> None:
        ...

