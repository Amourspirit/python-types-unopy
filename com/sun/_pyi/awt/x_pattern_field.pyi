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
# Libre Office Version: 7.2
# Namespace: com.sun.star.awt
from typing_extensions import Literal
from ..uno.x_interface import XInterface as XInterface_8f010a43

class XPatternField(XInterface_8f010a43):
    """
    gives access to the value and formatting of a pattern field.

    See Also:
        `API XPatternField <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XPatternField.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XPatternField']

    def getMasks(self, EditMask: str, LiteralMask: str) -> None:
        """
        returns the currently set pattern mask.

        * ``EditMask`` is an out direction argument.
        * ``LiteralMask`` is an out direction argument.
        """
    def getString(self) -> str:
        """
        returns the currently set string value of the pattern field.
        """
    def isStrictFormat(self) -> bool:
        """
        returns whether the format is currently checked during user input.
        """
    def setMasks(self, EditMask: str, LiteralMask: str) -> None:
        """
        sets the pattern mask.
        """
    def setStrictFormat(self, bStrict: bool) -> None:
        """
        determines if the format is checked during user input.
        """
    def setString(self, Str: str) -> None:
        """
        sets the string value of the pattern field.
        """

__all__ = ['XPatternField']

