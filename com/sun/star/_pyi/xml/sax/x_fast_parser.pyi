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
# Libre Office Version: 7.4
# Namespace: com.sun.star.xml.sax
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ...lang.locale import Locale as Locale_70d308fa
    from .input_source import InputSource as InputSource_c88c0c54
    from .x_entity_resolver import XEntityResolver as XEntityResolver_fcf10dfa
    from .x_error_handler import XErrorHandler as XErrorHandler_e0860cf3
    from .x_fast_document_handler import XFastDocumentHandler as XFastDocumentHandler_454c0fb6
    from .x_fast_namespace_handler import XFastNamespaceHandler as XFastNamespaceHandler_549c1004
    from .x_fast_token_handler import XFastTokenHandler as XFastTokenHandler_17510e78

class XFastParser(XInterface_8f010a43):
    """
    specifies a SAX parser that uses integer values for known XML names (elements, attributes and attribute values).
    
    The parser also handles namespaces and allows to have individual contexts for each XML element.
    
    Before parsing is possible you have to set your XFastDocumentHandler using setFastDocumentHandler().
    
    Parsing starts with calling parseStream(). If the parser finds a valid XML file with the given InputSource, it calls XFastDocumentHandler.startDocument() first.
    
    This parser generates either \"fast\" events that use integer token values for namespaces, elements and attributes or \"unknown\" events for elements that are unknown.
    
    A namespace is unknown if the namespace URL was not registered with registerNamespace().
    
    An element is unknown if no XFastTokenHandler is set or if the XFastTokenHandler does not return a valid identifier for the elements local name. An element is also unknown if the elements local name is known but it uses a namespace that is unknown.
    
    Setting a XFastTokenHandler with setTokenHandler() is optional, but without a XFastTokenHandler you will only get unknown sax events. This can be useful if you are only interested in the namespace handling and/or the context feature.
    
    For each element the parser sends a create child element event to the elements parent context by calling XFastContextHandler.createFastChildContext() for known elements or XFastContextHandler.createUnknownChildContext() for unknown elements. The parent context for the root element is the XFastDocumentHandler itself.
    
    If the parent context returns an empty reference, no further events for the element and all of its children are created.
    
    If a valid context is returned this context gets a start event by a call to XFastContextHandler.startFastElement() for known elements or XFastContextHandler.startUnknownElement() for unknown elements.
    
    After processing all its child elements the context gets an end event by a call to XFastContextHandler.endFastElement() for known elements or XFastContextHandler.endUnknownElement() for unknown elements.
    
    It is valid to return one instance of XFastContextHandler more than once. It is even possible to only use the XFastDocumentHandler by always returning a reference to itself for each create child context event.
    
    After the last element is processed the parser generates an end document event at the XFastDocumentHandler by calling XFastDocumentHandler.endDocument().
    
    **since**
    
        LibreOffice 7.1

    See Also:
        `API XFastParser <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1sax_1_1XFastParser.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.sax.XFastParser']

    def getNamespaceURL(self, prefix: str) -> str:
        """
        Gets the namespace url string.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def parseStream(self, aInputSource: 'InputSource_c88c0c54') -> None:
        """
        parses an XML document from a stream.
        
        Set the desired handlers before calling this method.

        Raises:
            SAXException: ``SAXException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def registerNamespace(self, NamespaceURL: str, NamespaceToken: int) -> None:
        """
        registers a known namespace url with the given integer token.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def setCustomEntityNames(self, replacements: 'typing.Tuple[typing.Tuple[str, str], ...]') -> None:
        """
        Simulate a DTD file.
        
        Will allow to use customized entity references like ∞ .
        
        **since**
        
            LibreOffice 7.1
        """
        ...
    def setEntityResolver(self, Resolver: 'XEntityResolver_fcf10dfa') -> None:
        """
        allows an application to register a DTD-Handler.
        """
        ...
    def setErrorHandler(self, Handler: 'XErrorHandler_e0860cf3') -> None:
        """
        allows an application to register an error event handler.
        
        Note that the error handler can throw an exception when an error or warning occurs. Note that an exception is thrown by the parser when an unrecoverable (fatal) error occurs.
        """
        ...
    def setFastDocumentHandler(self, Handler: 'XFastDocumentHandler_454c0fb6') -> None:
        """
        Application must register a document event handler to get sax events for the parsed stream.
        """
        ...
    def setLocale(self, locale: 'Locale_70d308fa') -> None:
        """
        sets a locale specified for localization of warnings and error messages.
        
        Set the language of the error messages. Useful when the parsing errors will be presented to the user.
        """
        ...
    def setNamespaceHandler(self, Handler: 'XFastNamespaceHandler_549c1004') -> None:
        """
        """
        ...
    def setTokenHandler(self, Handler: 'XFastTokenHandler_17510e78') -> None:
        """
        must be registered to translate known XML names to integer tokens.
        """
        ...


