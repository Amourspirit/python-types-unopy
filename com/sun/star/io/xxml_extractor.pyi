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
# Namespace: com.sun.star.io
from __future__ import annotations
import typing

from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_input_stream import XInputStream as XInputStream_98d40ab4


class XXMLExtractor(XInterface_8f010a43):
    """
    offers the capability to extract the XML document stream from a document storage.

    See Also:
        `API XXMLExtractor <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1io_1_1XXMLExtractor.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.io.XXMLExtractor'

    def extract(self, aStream: XInputStream_98d40ab4) -> XInputStream_98d40ab4:
        """
        extracts the XML stream from the document storage.
        """
        ...



