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
# Namespace: com.sun.star.rendering
from typing_extensions import Literal
import typing
import uno
from .x_half_float_read_only_bitmap import XHalfFloatReadOnlyBitmap as XHalfFloatReadOnlyBitmap_ad83120a
if typing.TYPE_CHECKING:
    from ..geometry.integer_point2_d import IntegerPoint2D as IntegerPoint2D_8f0dc2
    from ..geometry.integer_rectangle2_d import IntegerRectangle2D as IntegerRectangle2D_3c5c0f4d
    from .floating_point_bitmap_layout import FloatingPointBitmapLayout as FloatingPointBitmapLayout_c66812df

class XHalfFloatBitmap(XHalfFloatReadOnlyBitmap_ad83120a):
    """
    Specialized interface for bitmaps containing half floats as their color components.
    
    Half floats are 16 bit wide, and newer GPUs already have them as supported frame buffer format.

    See Also:
        `API XHalfFloatBitmap <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XHalfFloatBitmap.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.rendering.XHalfFloatBitmap']

    def setData(self, data: uno.ByteSequence, bitmapLayout: 'FloatingPointBitmapLayout_c66812df', rect: 'IntegerRectangle2D_3c5c0f4d') -> None:
        """
        Set raw data of a bitmap.
        
        Set raw data of a bitmap, in the format as defined by getMemoryLayout(). With the given rectangle, a subset of the bitmap can be changed. When setting subsets of the bitmap, the same scanline padding takes place as when the whole bitmap is changed.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def setPixel(self, color: uno.ByteSequence, bitmapLayout: 'FloatingPointBitmapLayout_c66812df', pos: 'IntegerPoint2D_8f0dc2') -> None:
        """
        Set a single pixel of the bitmap with the given color value.
        
        When setting data on volatile bitmaps, always call isValid() before, and retrieve a new memory layout via getMemoryLayout(). At least under Windows, the memory layout can change for the same bitmap, if the user e.g. switches the screen resolution. Thus, this method will throw an IllegalArgumentException, if the memory layout changed between a call to getMemoryLayout() and setData().

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...


