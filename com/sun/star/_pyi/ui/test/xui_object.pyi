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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.ui.test
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ...beans.property_values import PropertyValues as PropertyValues_d6470ce6

class XUIObject(ABC):
    """

    See Also:
        `API XUIObject <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ui_1_1test_1_1XUIObject.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ui.test.XUIObject']

    def executeAction(self, action: str, propValues: 'PropertyValues_d6470ce6') -> None:
        """
        """
    def getChild(self, id: str) -> 'XUIObject':
        """
        """
    def getChildren(self) -> 'typing.Tuple[str, ...]':
        """
        """
    def getHierarchy(self) -> str:
        """
        """
    def getState(self) -> 'PropertyValues_d6470ce6':
        """
        """
    def getType(self) -> str:
        """
        """
