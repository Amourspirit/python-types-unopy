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
    from ...lang.locale import Locale as Locale_70d308fa
    from .input_source import InputSource as InputSource_c88c0c54
    from .xdtd_handler import XDTDHandler as XDTDHandler_c3df0bc5
    from .x_document_handler import XDocumentHandler as XDocumentHandler_9b90e28
    from .x_entity_resolver import XEntityResolver as XEntityResolver_fcf10dfa
    from .x_error_handler import XErrorHandler as XErrorHandler_e0860cf3

class XParser(XInterface_8f010a43):
    """
    specifies a SAX parser.
    
    This interface is an IDL version of the Java interface org.xml.sax.Parser with some minor adaptations.

    See Also:
        `API XParser <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1sax_1_1XParser.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.sax.XParser']

    def parseStream(self, aInputSource: 'InputSource_c88c0c54') -> None:
        """
        parses an XML document from a stream.
        
        Set the desired handlers before calling this method.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def setDTDHandler(self, xHandler: 'XDTDHandler_c3df0bc5') -> None:
        """
        allows an application to register a DTD-Handler.
        """
        ...
    def setDocumentHandler(self, xHandler: 'XDocumentHandler_9b90e28') -> None:
        """
        allows an application to register a document event handler.
        """
        ...
    def setEntityResolver(self, xResolver: 'XEntityResolver_fcf10dfa') -> None:
        """
        allows an application to register a DTD-Handler.
        """
        ...
    def setErrorHandler(self, xHandler: 'XErrorHandler_e0860cf3') -> None:
        """
        allows an application to register an error event handler.
        
        Note that the error handler can throw an exception when an error or warning occurs. Note that an exception is thrown by the parser when an unrecoverable (fatal) error occurs.
        """
        ...
    def setLocale(self, locale: 'Locale_70d308fa') -> None:
        """
        sets a locale specified for localization of warnings and error messages.
        
        Set the language of the error messages. Useful when the parsing errors will be presented to the user.
        """
        ...


