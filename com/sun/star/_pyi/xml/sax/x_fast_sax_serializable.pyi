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
from abc import ABC
if typing.TYPE_CHECKING:
    from ...beans.string_pair import StringPair as StringPair_a4bc0b14
    from .x_fast_document_handler import XFastDocumentHandler as XFastDocumentHandler_454c0fb6
    from .x_fast_token_handler import XFastTokenHandler as XFastTokenHandler_17510e78

class XFastSAXSerializable(ABC):
    """
    serializes a DOM tree by generating FastSAX events.
    
    **since**
    
        OOo 3.1

    See Also:
        `API XFastSAXSerializable <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1sax_1_1XFastSAXSerializable.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.sax.XFastSAXSerializable']

    def fastSerialize(self, handler: 'XFastDocumentHandler_454c0fb6', tokenHandler: 'XFastTokenHandler_17510e78', namespaces: 'typing.Tuple[StringPair_a4bc0b14, ...]', registerNamespaces: 'typing.Tuple[typing.Tuple[str, int], ...]') -> None:
        """
        serializes an object (e.g.
        
        a DOM tree) that represents an XML document by generating fast SAX events.
        
        This is necessary mostly because the DOM implementation does not permit attaching namespaces declarations directly to nodes, which may lead to duplicate namespace declarations on export, and thus larger documents. Note that the first part of each tuple is the prefix, e.g. \"office\", and the second is the numeric namespace identifier.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...


