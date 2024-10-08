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
# Namespace: com.sun.star.awt
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43


class XNumericField(XInterface_8f010a43):
    """
    gives access to the value and formatting of a numeric field.

    See Also:
        `API XNumericField <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XNumericField.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.awt.XNumericField'

    def getDecimalDigits(self) -> int:
        """
        returns the currently set number of decimals.
        """
        ...
    def getFirst(self) -> float:
        """
        returns the currently set first value which is set on POS1 key.
        """
        ...
    def getLast(self) -> float:
        """
        returns the currently set last value which is set on END key.
        """
        ...
    def getMax(self) -> float:
        """
        returns the currently set maximum value that can be entered by the user.
        """
        ...
    def getMin(self) -> float:
        """
        returns the currently set minimum value that can be entered by the user.
        """
        ...
    def getSpinSize(self) -> float:
        """
        returns the currently set increment value for the spin button.
        """
        ...
    def getValue(self) -> float:
        """
        returns the value which is currently displayed in the numeric field.
        """
        ...
    def isStrictFormat(self) -> bool:
        """
        returns whether the format is currently checked during user input.
        """
        ...
    def setDecimalDigits(self, nDigits: int) -> None:
        """
        sets the number of decimals.
        """
        ...
    def setFirst(self, Value: float) -> None:
        """
        sets the first value to be set on POS1 key.
        """
        ...
    def setLast(self, Value: float) -> None:
        """
        sets the last value to be set on END key.
        """
        ...
    def setMax(self, Value: float) -> None:
        """
        sets the maximum value that can be entered by the user.
        """
        ...
    def setMin(self, Value: float) -> None:
        """
        sets the minimum value that can be entered by the user.
        """
        ...
    def setSpinSize(self, Value: float) -> None:
        """
        sets the increment value for the spin button.
        """
        ...
    def setStrictFormat(self, bStrict: bool) -> None:
        """
        determines if the format is checked during user input.
        """
        ...
    def setValue(self, Value: float) -> None:
        """
        sets the value which is displayed in the numeric field.
        """
        ...


