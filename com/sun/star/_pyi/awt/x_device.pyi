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
# Namespace: com.sun.star.awt
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .device_info import DeviceInfo as DeviceInfo_8e370a30
    from .font_descriptor import FontDescriptor as FontDescriptor_bc110c0a
    from .x_bitmap import XBitmap as XBitmap_70cd0909
    from .x_display_bitmap import XDisplayBitmap as XDisplayBitmap_bb550bdf
    from .x_font import XFont as XFont_5f480843
    from .x_graphics import XGraphics as XGraphics_842309dd


class XDevice(XInterface_8f010a43):
    """
    provides information about a graphical output device and offers a factory for the graphics which provides write operations on the device.

    See Also:
        `API XDevice <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XDevice.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.awt.XDevice']

    def createBitmap(self, nX: int, nY: int, nWidth: int, nHeight: int) -> 'XBitmap_70cd0909':
        """
        creates a bitmap with the current device depth.
        
        If the specified area does not lie entirely in the device, the bits outside are not specified.
        """
        ...
    def createDevice(self, nWidth: int, nHeight: int) -> 'XDevice':
        """
        creates a new device which is compatible with this one.
        
        If the device does not support the GETBITS device capability, this method returns NULL.
        """
        ...
    def createDisplayBitmap(self, Bitmap: 'XBitmap_70cd0909') -> 'XDisplayBitmap_bb550bdf':
        """
        creates a device compatible bitmap.
        
        The data of the bitmap is in process memory instead of in the device, so that the output operation is fast.
        """
        ...
    def createGraphics(self) -> 'XGraphics_842309dd':
        """
        creates a new graphics whose output operation is directed to this device.
        """
        ...
    def getFont(self, aDescriptor: 'FontDescriptor_bc110c0a') -> 'XFont_5f480843':
        """
        returns information about a font offered by this device.
        """
        ...
    def getFontDescriptors(self) -> 'typing.Tuple[FontDescriptor_bc110c0a, ...]':
        """
        returns the list of available font descriptors.
        """
        ...
    def getInfo(self) -> 'DeviceInfo_8e370a30':
        """
        returns information about the device.
        """
        ...


