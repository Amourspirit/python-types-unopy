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
# Namespace: com.sun.star.document
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73


class XFilter(XInterface_8f010a43):
    """
    interface to filter documents
    
    This interface will be used by service ImportFilter or ExportFilter to support loading/saving of documents in different formats. The target/source of such filter operations must be known before filtering will be started. (see XImporter and XExporter too) Otherwise this interface can't work right.

    See Also:
        `API XFilter <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XFilter.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.document.XFilter'

    def cancel(self) -> None:
        """
        cancel the process.
        """
        ...
    def filter(self, aDescriptor: typing.Tuple[PropertyValue_c9610c73, ...]) -> bool:
        """
        filter the document.
        
        The given MediaDescriptor holds all necessary information about the document.
        
        Don't hold hard references to the descriptor items. You must copy needed information! Otherwise we couldn't destroy (for example) an existing input stream!
        """
        ...


