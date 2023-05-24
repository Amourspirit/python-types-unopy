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
# Namespace: com.sun.star.datatransfer
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .data_flavor import DataFlavor as DataFlavor_ffd30deb


class XDataFormatTranslator(XInterface_8f010a43):
    """
    Interface to be implemented by objects used to translate a DataFlavor to a system dependent data transfer type and vice versa.
    
    Different platforms use different types to describe data formats available during data exchange operations like clipboard or drag&drop. Windows for instance uses integer values to describe an available clipboard or drag&drop format, Unix X11 uses so called Atoms etc.

    See Also:
        `API XDataFormatTranslator <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1datatransfer_1_1XDataFormatTranslator.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.datatransfer.XDataFormatTranslator'

    def getDataFlavorFromSystemDataType(self, aSysDataType: typing.Any) -> DataFlavor_ffd30deb:
        """
        Converts a system dependent data type to a DataFlavor.
        
        If there is no appropriate mapping for a system dependent data type, the returned DataFlavor will be empty.
        """
        ...
    def getSystemDataTypeFromDataFlavor(self, aDataFlavor: DataFlavor_ffd30deb) -> typing.Any:
        """
        Converts a DataFlavor to system dependent data type.
        
        If the is no system dependent data type for a given DataFlavor the returned any is empty.
        """
        ...


