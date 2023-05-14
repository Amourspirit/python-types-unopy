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
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.rendering
# Libre Office Version: 7.4
from typing_extensions import Literal
import typing
from .x_bitmap_palette import XBitmapPalette as XBitmapPalette_cf20e4a
from .x_integer_bitmap_color_space import XIntegerBitmapColorSpace as XIntegerBitmapColorSpace_b1691234


class IntegerBitmapLayout(object):
    """
    Struct Class

    This structure describes the memory layout of a bitmap having integer color channels.
    
    This structure collects all necessary information to describe the memory layout of a bitmap having integer color channels
    
    **since**
    
        OOo 2.0

    See Also:
        `API IntegerBitmapLayout <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1rendering_1_1IntegerBitmapLayout.html>`_
    """
    typeName: Literal['com.sun.star.rendering.IntegerBitmapLayout']

    def __init__(self, ScanLines: typing.Optional[int] = ..., ScanLineBytes: typing.Optional[int] = ..., ScanLineStride: typing.Optional[int] = ..., PlaneStride: typing.Optional[int] = ..., ColorSpace: typing.Optional[XIntegerBitmapColorSpace_b1691234] = ..., Palette: typing.Optional[XBitmapPalette_cf20e4a] = ..., IsMsbFirst: typing.Optional[bool] = ...) -> None:
        """
        Constructor

        Arguments:
            ScanLines (int, optional): ScanLines value.
            ScanLineBytes (int, optional): ScanLineBytes value.
            ScanLineStride (int, optional): ScanLineStride value.
            PlaneStride (int, optional): PlaneStride value.
            ColorSpace (XIntegerBitmapColorSpace, optional): ColorSpace value.
            Palette (XBitmapPalette, optional): Palette value.
            IsMsbFirst (bool, optional): IsMsbFirst value.
        """
        ...


    @property
    def ScanLines(self) -> int:
        """
        Number of scanlines for this bitmap.
        
        This value must not be negative
        """
        ...

    @ScanLines.setter
    def ScanLines(self, value: int) -> None:
        ...

    @property
    def ScanLineBytes(self) -> int:
        """
        Number of data bytes per scanline.
        
        This value must not be negative
        """
        ...

    @ScanLineBytes.setter
    def ScanLineBytes(self, value: int) -> None:
        ...

    @property
    def ScanLineStride(self) -> int:
        """
        Byte offset between the start of two consecutive scanlines.
        
        This value is permitted to be negative, denoting a bitmap whose content is flipped at the x axis.
        """
        ...

    @ScanLineStride.setter
    def ScanLineStride(self, value: int) -> None:
        ...

    @property
    def PlaneStride(self) -> int:
        """
        Byte offset between the start of two consecutive planes.
        
        This value is permitted to be negative. If this value is zero, the bitmap is assumed to be in chunky format, otherwise it is assumed to be planar. The difference between chunky and planar layout lies in the way how color channels are interleaved. For a chunky format, all channel data for a single pixel lies consecutively in memory. For a planar layout, the first channel of all pixel is stored consecutive, followed by the second channel, and so forth.
        """
        ...

    @PlaneStride.setter
    def PlaneStride(self, value: int) -> None:
        ...

    @property
    def ColorSpace(self) -> XIntegerBitmapColorSpace_b1691234:
        """
        Color space the bitmap colors shall be interpreted within.
        
        Note that the actual pixel layout is specified at the color space. If this layout describes a palette bitmap format, this color space describes the index format (plus maybe an extra alpha channel). The palette itself references another color space, which describes the layout of the palette entries.
        """
        ...

    @ColorSpace.setter
    def ColorSpace(self, value: XIntegerBitmapColorSpace_b1691234) -> None:
        ...

    @property
    def Palette(self) -> XBitmapPalette_cf20e4a:
        """
        This member determines whether the bitmap data are actually indices into a color map.
        
        When set to the nil reference, the bitmap data is assumed to contain direct color values (to be interpreted according to the associated color space). If this member references a valid palette, one of the pixel components as returned by the color space referenced from the ColorSpace is required to be of type ColorComponentTag.INDEX. That component is then used to index the palette.
        """
        ...

    @Palette.setter
    def Palette(self, value: XBitmapPalette_cf20e4a) -> None:
        ...

    @property
    def IsMsbFirst(self) -> bool:
        """
        This member determines the bit order (only relevant if a pixel uses less than 8 bits, of course).
        
        When TRUE, this member denotes that the leftmost pixel from an 8 bit amount of pixel data consists of the bits starting with the most significant bit. When FALSE, it's starting with the least significant bit.
        
        Example: for a 1bpp bitmap, each pixel is represented by exactly one bit. If this member is TRUE, the first pixel is the MSB of the first byte, and the eighth pixel is the LSB of the first byte. If this member is FALSE, it's just the opposite.
        """
        ...

    @IsMsbFirst.setter
    def IsMsbFirst(self, value: bool) -> None:
        ...

