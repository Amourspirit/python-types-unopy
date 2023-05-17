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
# Namespace: com.sun.star.xml.sax
import typing
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from ...uno.x_interface import XInterface as XInterface_8f010a43


class XDTDHandler(XInterface_8f010a43):
    """
    receives events according to the DTD of the document.
    
    The SAX parser may report these events in any order, regardless of the order in which the notations and unparsed entities were declared; however, all DTD events must be reported after the document handler's startDocument event, and before the first startElement event. It is up to the application to store the information for future use (perhaps in a hash table or object tree). If the application encounters attributes of type \"NOTATION\", \"ENTITY\", or \"ENTITIES\", it can use the information that it obtained through this interface to find the entity and/or notation that corresponds with the attribute value.

    See Also:
        `API XDTDHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1sax_1_1XDTDHandler.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.sax.XDTDHandler']

    def notationDecl(self, sName: str, sPublicId: str, sSystemId: str) -> None:
        """
        receives notification of a notation declaration event.
        """
        ...
    def unparsedEntityDecl(self, sName: str, sPublicId: str, sSystemId: str, sNotationName: str) -> None:
        """
        receives notification of an unparsed entity declaration event.
        """
        ...


