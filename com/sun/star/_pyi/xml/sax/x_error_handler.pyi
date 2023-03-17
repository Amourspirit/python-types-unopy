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
from ...uno.x_interface import XInterface as XInterface_8f010a43

class XErrorHandler(XInterface_8f010a43):
    """
    is the basic interface for SAX error handlers.
    
    If a SAX application needs to implement customized error handling, it must implement this interface and then register an instance with the SAX parser using the parser's XParser.setErrorhandler() method. The parser will then report all errors and warnings through this interface.
    
    This interface is a slight adaptation of the Java interface org.xml.sax.ErrorHandler. In IDL, no exception can be passed as an argument, so an any serves as the container. The type of the exception is SAXParseException or an instance of a derived class.

    See Also:
        `API XErrorHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1sax_1_1XErrorHandler.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.sax.XErrorHandler']

    def error(self, aSAXParseException: object) -> None:
        """
        receives notification of a recoverable error.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    def fatalError(self, aSAXParseException: object) -> None:
        """
        receives notification of a non-recoverable error.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...
    def warning(self, aSAXParseException: object) -> None:
        """
        receives notification of a warning.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
        ...


