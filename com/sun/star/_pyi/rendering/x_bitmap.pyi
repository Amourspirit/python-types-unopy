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
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..geometry.integer_size2_d import IntegerSize2D as IntegerSize2D_f2690d53
    from ..geometry.real_size2_d import RealSize2D as RealSize2D_ca1a0c09

class XBitmap(XInterface_8f010a43):
    """
    This is a generic interface to a bitmap.
    
    This interface contains the generic functionality to be used on every XCanvas bitmap object. More format-specific methods can be found at the XIntegerBitmap, XIeeeDoubleBitmap, XIeeeFloatBitmap and XHalfFloatBitmap interfaces.
    
    **since**
    
        OOo 2.0

    See Also:
        `API XBitmap <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XBitmap.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.rendering.XBitmap']

    def getScaledBitmap(self, newSize: 'RealSize2D_ca1a0c09', beFast: bool) -> 'XBitmap':
        """
        Query a scaled copy of the original bitmap.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            VolatileContentDestroyedException: ``VolatileContentDestroyedException``
        """
        ...
    def getSize(self) -> 'IntegerSize2D_f2690d53':
        """
        Query the size of the bitmap.
        
        This method queries the bitmap size in pixel.
        """
        ...
    def hasAlpha(self) -> bool:
        """
        Query transparency status of the bitmap.
        
        The method checks, whether the bitmap contains any alpha information. The same information is also available at the XColorSpace associated with this bitmap, though much easier to access here (the color space then has a component flagged ColorComponentTag.ALPHA).
        """
        ...


