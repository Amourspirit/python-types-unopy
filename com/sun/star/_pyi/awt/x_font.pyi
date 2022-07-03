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
import typing
import uno
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from .simple_font_metric import SimpleFontMetric as SimpleFontMetric_d53c0cb9

class XFont(XInterface_8f010a43):
    """
    describes a font on a specific device.
    
    All values are in pixels within this device.

    See Also:
        `API XFont <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XFont.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XFont']

    def getCharWidth(self, c: str) -> int:
        """
        returns the width of the specified character.
        """
        ...
    def getCharWidths(self, nFirst: str, nLast: str) -> uno.ByteSequence:
        """
        returns the widths of the specified characters.
        """
        ...
    def getFontDescriptor(self) -> 'FontDescriptor_bc110c0a':
        """
        returns the description of the font.
        
        The unit of measurement is pixels for the device.
        """
        ...
    def getFontMetric(self) -> 'SimpleFontMetric_d53c0cb9':
        """
        returns additional information about the font.
        """
        ...
    def getKernPairs(self, Chars1: 'typing.Tuple[str, ...]', Chars2: 'typing.Tuple[str, ...]', Kerns: uno.ByteSequence) -> None:
        """
        queries the kerning pair table.

        * ``Chars1`` is an out direction argument.
        * ``Chars2`` is an out direction argument.
        * ``Kerns`` is an out direction argument.
        """
        ...
    def getStringWidth(self, str: str) -> int:
        """
        returns the string width.
        """
        ...
    def getStringWidthArray(self, str: str, aDXArray: uno.ByteSequence) -> int:
        """
        returns the string and the character widths.

        * ``aDXArray`` is an out direction argument.
        """
        ...


