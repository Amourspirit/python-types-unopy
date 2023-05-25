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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.text
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_text_range import XTextRange as XTextRange_9a910ab7


class XTextRangeCompare(XInterface_8f010a43):
    """
    compares the positions of two TextRanges within a Text.
    
    Only TextRange instances within the same Text can be compared.

    See Also:
        `API XTextRangeCompare <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1text_1_1XTextRangeCompare.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.text.XTextRangeCompare'

    def compareRegionEnds(self, xR1: XTextRange_9a910ab7, xR2: XTextRange_9a910ab7) -> int:
        """

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def compareRegionStarts(self, xR1: XTextRange_9a910ab7, xR2: XTextRange_9a910ab7) -> int:
        """

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...


