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
# Namespace: com.sun.star.xml.dom
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_document import XDocument as XDocument_aebc0b5e
    from .x_document_type import XDocumentType as XDocumentType_e0340d00


class XDOMImplementation(XInterface_8f010a43):
    """

    See Also:
        `API XDOMImplementation <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1dom_1_1XDOMImplementation.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.dom.XDOMImplementation']

    def createDocument(self, namespaceURI: str, qualifiedName: str, doctype: 'XDocumentType_e0340d00') -> 'XDocument_aebc0b5e':
        """
        Creates a DOM Document object of the specified type with its document element.
        
        Throws: DOMException - INVALID_CHARACTER_ERR: Raised if the specified qualified name contains an illegal character. NAMESPACE_ERR: Raised if the qualifiedName is malformed, if the qualifiedName has a prefix and the namespaceURI is null, or if the qualifiedName has a prefix that is \"xml\" and the namespaceURI is different from \" http://www.w3.org/XML/1998/namespace\" , or if the DOM implementation does not support the \"XML\" feature but a non-null namespace URI was provided, since namespaces were defined by XML. WRONG_DOCUMENT_ERR: Raised if doctype has already been used with a different document or was created from a different implementation. NOT_SUPPORTED_ERR: May be raised by DOM implementations which do not support the \"XML\" feature, if they choose not to support this method. Other features introduced in the future, by the DOM WG or in extensions defined by other groups, may also demand support for this method; please consult the definition of the feature to see if it requires this method.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    def createDocumentType(self, qualifiedName: str, publicId: str, systemId: str) -> 'XDocumentType_e0340d00':
        """
        Creates an empty DocumentType node.
        
        Throws: DOMException - INVALID_CHARACTER_ERR: Raised if the specified qualified name contains an illegal character. NAMESPACE_ERR: Raised if the qualifiedName is malformed. NOT_SUPPORTED_ERR: May be raised by DOM implementations which do not support the \"XML\" feature, if they choose not to support this method. Other features introduced in the future, by the DOM WG or in extensions defined by other groups, may also demand support for this method; please consult the definition of the feature to see if it requires this method.

        Raises:
            DOMException: ``DOMException``
        """
        ...
    def hasFeature(self, feature: str, ver: str) -> bool:
        """
        Test if the DOM implementation implements a specific feature.
        """
        ...


