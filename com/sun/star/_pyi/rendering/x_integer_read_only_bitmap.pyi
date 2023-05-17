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
# Namespace: com.sun.star.rendering
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

import uno
from .x_bitmap import XBitmap as XBitmap_b1b70b7b
if typing.TYPE_CHECKING:
    from ..geometry.integer_point2_d import IntegerPoint2D as IntegerPoint2D_8f0dc2
    from ..geometry.integer_rectangle2_d import IntegerRectangle2D as IntegerRectangle2D_3c5c0f4d
    from .integer_bitmap_layout import IntegerBitmapLayout as IntegerBitmapLayout_5b94106f


class XIntegerReadOnlyBitmap(XBitmap_b1b70b7b):
    """
    This is a specialized interface for bitmaps having integer color channels.
    
    In contrast to XIntegerBitmap, this interface only permits read-only access.
    
    Use this interface for e.g. bitmaps that are calculated on-the-fly, or that are pure functional, and thus cannot be modified.
    
    If you get passed an instance of XIntegerReadOnlyBitmap that also supports the XVolatileBitmap interface, things become a bit more complicated. When reading data, one has to check for both VolatileContentDestroyedException and mismatching IntegerBitmapLayout return values. If either of them occurs, the whole bitmap read operation should be repeated, if you need consistent information.

    See Also:
        `API XIntegerReadOnlyBitmap <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XIntegerReadOnlyBitmap.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.rendering.XIntegerReadOnlyBitmap']

    def getData(self, bitmapLayout: 'IntegerBitmapLayout_5b94106f', rect: 'IntegerRectangle2D_3c5c0f4d') -> uno.ByteSequence:
        """
        Query the raw data of this bitmap.
        
        Query the raw data of this bitmap, in the format as defined by getMemoryLayout(). With the given rectangle, a subset of the whole bitmap can be queried. If the internal data format's pixel are not integer multiples of bytes (i.e. if one pixel occupies less than a byte), the leftover content of the bytes at the right of each scanline is filled with zeros. The details of the scanline padding are to be retrieved from the passed bitmap layout.
        
        Note that the bitmap memory layout might change over time for volatile bitmaps.

        * ``bitmapLayout`` is an out direction argument.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
            VolatileContentDestroyedException: ``VolatileContentDestroyedException``
        """
        ...
    def getMemoryLayout(self) -> 'IntegerBitmapLayout_5b94106f':
        """
        Query the memory layout for this bitmap.
        
        Please note that for volatile bitmaps, the memory layout might change between subsequent calls.
        """
        ...
    def getPixel(self, bitmapLayout: 'IntegerBitmapLayout_5b94106f', pos: 'IntegerPoint2D_8f0dc2') -> uno.ByteSequence:
        """
        Get a single pixel of the bitmap, returning its color value.
        
        If the internal data format's pixel are not integer multiples of bytes (i.e. if one pixel occupies less than a byte - the case of more than one byte per pixel is not specified), the color value is returned in the least significant bits of the single byte returned as the color. The details of the returned pixel data are to be retrieved from the passed bitmap layout.
        
        Note that the bitmap memory layout might change for volatile bitmaps.

        * ``bitmapLayout`` is an out direction argument.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
            VolatileContentDestroyedException: ``VolatileContentDestroyedException``
        """
        ...


