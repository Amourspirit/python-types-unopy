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
# Namespace: com.sun.star.xml.csax
from __future__ import annotations
import typing

from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .xml_attribute import XMLAttribute as XMLAttribute_df0f0cdb


class XCompressedDocumentHandler(XInterface_8f010a43):
    """
    A compressed XDocumentHandler interface.
    
    All methods in this interface have the same function with methods in the XDocumentHandler interface.
    
    Because there is no interface parameter in these methods, so using this interface to transfer SAX event is thought to have better performance than using the XDocumentHandler interface, in case of when UNO C++/Java bridge is involved.

    See Also:
        `API XCompressedDocumentHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1csax_1_1XCompressedDocumentHandler.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.xml.csax.XCompressedDocumentHandler'

    def compressedCharacters(self, aChars: str) -> None:
        """

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    def compressedEndDocument(self) -> None:
        """

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    def compressedEndElement(self, aName: str) -> None:
        """

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    def compressedIgnorableWhitespace(self, aWhitespaces: str) -> None:
        """

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    def compressedProcessingInstruction(self, aTarget: str, aData: str) -> None:
        """

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    def compressedSetDocumentLocator(self, columnNumber: int, lineNumber: int, publicId: str, systemId: str) -> None:
        """

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    def compressedStartDocument(self) -> None:
        """

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    def compressedStartElement(self, aName: str, aAttributes: typing.Tuple[XMLAttribute_df0f0cdb, ...]) -> None:
        """

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...


