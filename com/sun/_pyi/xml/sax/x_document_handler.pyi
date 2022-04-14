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
# Libre Office Version: 7.2
# Namespace: com.sun.star.xml.sax
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_attribute_list import XAttributeList as XAttributeList_eec70d7b
    from .x_locator import XLocator as XLocator_a3fb0aff

class XDocumentHandler(XInterface_8f010a43):
    """
    receives notification of general document events.
    
    This interface is an IDL version of the Java interface org.xml.sax.DocumentHandler with some smaller adaptations.

    See Also:
        `API XDocumentHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1sax_1_1XDocumentHandler.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.sax.XDocumentHandler']

    def characters(self, aChars: str) -> None:
        """
        receives notification of character data.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    def endDocument(self) -> None:
        """
        receives notification of the end of a document.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    def endElement(self, aName: str) -> None:
        """
        receives notification of the end of an element.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    def ignorableWhitespace(self, aWhitespaces: str) -> None:
        """
        receives notification of white space that can be ignored.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    def processingInstruction(self, aTarget: str, aData: str) -> None:
        """
        receives notification of a processing instruction.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    def setDocumentLocator(self, xLocator: 'XLocator_a3fb0aff') -> None:
        """
        receives an object for locating the origin of SAX document events.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    def startDocument(self) -> None:
        """
        receives notification of the beginning of a document.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    def startElement(self, aName: str, xAttribs: 'XAttributeList_eec70d7b') -> None:
        """
        receives notification of the beginning of an element .

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """

__all__ = ['XDocumentHandler']

