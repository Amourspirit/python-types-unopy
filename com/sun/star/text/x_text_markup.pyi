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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 2024.2
# Namespace: com.sun.star.text
from __future__ import annotations
import typing

from abc import ABC
if typing.TYPE_CHECKING:
    from ..container.x_string_key_map import XStringKeyMap as XStringKeyMap_ffc60de1
    from .x_text_range import XTextRange as XTextRange_9a910ab7


class XTextMarkup(ABC):
    """
    provides functionality to markup text.
    
    **since**
    
        OOo 2.3

    See Also:
        `API XTextMarkup <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XTextMarkup.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.text.XTextMarkup'

    def commitStringMarkup(self, nType: int, aIdentifier: str, nStart: int, nLength: int, xMarkupInfoContainer: XStringKeyMap_ffc60de1) -> None:
        """
        submits a new markup range.
        """
        ...
    def commitTextRangeMarkup(self, nType: int, aIdentifier: str, xRange: XTextRange_9a910ab7, xMarkupInfoContainer: XStringKeyMap_ffc60de1) -> None:
        """
        """
        ...
    def getMarkupInfoContainer(self) -> XStringKeyMap_ffc60de1:
        """
        obtains a container to store additional user defined text markup information.
        """
        ...


