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
# Enum
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.text
# Libre Office Version: 7.4
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import uno
from enum import Enum

class PageNumberType(Enum):
    """
    Enum

    

    See Also:
        `API PageNumberType <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1text.html#aeffd73e249af906f303724f66f1f01c5>`_
    """
    typeName: str = 'com.sun.star.text.PageNumberType'

    CURRENT: 'uno.Enum'
    """
    The number of the current page is displayed.
    """
    NEXT: 'uno.Enum'
    """
    The number of the next page is displayed if there is any, otherwise the field is empty.
    """
    PREV: 'uno.Enum'
    """
    The number of the previous page is displayed if there is any, otherwise the field is empty.
    """

