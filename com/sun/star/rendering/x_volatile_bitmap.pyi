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
# Namespace: com.sun.star.rendering
from __future__ import annotations
import typing

from .x_bitmap import XBitmap as XBitmap_b1b70b7b


class XVolatileBitmap(XBitmap_b1b70b7b):
    """
    This is a specialized interface to a volatile bitmap (which can become invalid at any point in time).

    See Also:
        `API XVolatileBitmap <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XVolatileBitmap.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.rendering.XVolatileBitmap'

    def isValid(self) -> bool:
        """
        Query whether this volatile bitmap still has valid content.
        
        As the video RAM allocated to this bitmap can be reclaimed at any time, a return value of true here does not imply that the next draw operation with this bitmap will succeed. Instead, the exception VolatileContentDestroyed might then be thrown, if lost bitmap data is accessed.
        """
        ...


