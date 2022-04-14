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
# Namespace: com.sun.star.xml.crypto.sax
from typing_extensions import Literal
import typing
from ....uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ...sax.x_document_handler import XDocumentHandler as XDocumentHandler_9b90e28
    from ...wrapper.xxml_element_wrapper import XXMLElementWrapper as XXMLElementWrapper_66c0107c

class XSAXEventKeeper(XInterface_8f010a43):
    """
    Interface of SAX Event Keeper.
    
    This interface is used to manipulate element marks in a SAX event stream.
    
    There are two kinds of element mark, one is element collector, which is used to collect a particular element from the SAX event stream; the other is blocker, which is used to block the SAX event stream.

    See Also:
        `API XSAXEventKeeper <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1crypto_1_1sax_1_1XSAXEventKeeper.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.crypto.sax.XSAXEventKeeper']

    def addBlocker(self) -> int:
        """
        Adds a new blocker on the next element in the SAX event stream.
        
        No SAX event starting from the next element will be forwarded until this blocker is removed.
        """
    def addElementCollector(self) -> int:
        """
        Adds a new element collector on the next element in the SAX event stream.
        """
    def getCurrentBlockingNode(self) -> 'XXMLElementWrapper_66c0107c':
        """
        Gets the element which current blocking happens.
        
        This element is the working element of the first blocker in tree order.
        """
    def getElement(self, id: int) -> 'XXMLElementWrapper_66c0107c':
        """
        Gets the element of an element mark.
        """
    def isBlocking(self) -> bool:
        """
        Checks whether the SAX event stream is blocking.
        """
    def printBufferNodeTree(self) -> str:
        """
        Prints information about all buffered elements.
        """
    def removeBlocker(self, id: int) -> None:
        """
        Removes a blocker.
        """
    def removeElementCollector(self, id: int) -> None:
        """
        Removes an element collector.
        """
    def setElement(self, id: int, aElement: 'XXMLElementWrapper_66c0107c') -> None:
        """
        Sets the element of an element mark.
        
        When an element is replaced outside of this interface, then uses this method can restore the link between an element mark and its working element.
        """
    def setNextHandler(self, nextHandler: 'XDocumentHandler_9b90e28') -> 'XDocumentHandler_9b90e28':
        """
        Sets the next document handler in the SAX chain.
        
        This handler will receive SAX events forwarded by the SAXEventKeeper.
        """

__all__ = ['XSAXEventKeeper']

