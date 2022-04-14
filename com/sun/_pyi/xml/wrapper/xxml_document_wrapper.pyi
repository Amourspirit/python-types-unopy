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
# Namespace: com.sun.star.xml.wrapper
from typing_extensions import Literal
import typing
from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..sax.x_document_handler import XDocumentHandler as XDocumentHandler_9b90e28
    from .xxml_element_wrapper import XXMLElementWrapper as XXMLElementWrapper_66c0107c

class XXMLDocumentWrapper(XInterface_8f010a43):
    """
    Interface of XML Document Wrapper.
    
    When converting SAX events into a DOM tree, this interface is used to manipulate the DOM data in UNO perspective.
    
    Every language has its own methods to manipulate its native DOM data structure, this interface provides a common method set which each language have to implement.
    
    In another word, this interface wraps language dependent methods, then other component can manipulate DOM data through UNO methods.

    See Also:
        `API XXMLDocumentWrapper <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1wrapper_1_1XXMLDocumentWrapper.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.xml.wrapper.XXMLDocumentWrapper']

    def clearUselessData(self, node: 'XXMLElementWrapper_66c0107c', reservedDescendants: 'typing.Tuple[XXMLElementWrapper_66c0107c, ...]', stopAtNode: 'XXMLElementWrapper_66c0107c') -> None:
        """
        Clears all useless element in a branch of the DOM tree along the tree order.
        """
    def collapse(self, node: 'XXMLElementWrapper_66c0107c') -> None:
        """
        Collapses a tree path.
        
        Each element in the ancestor path of the node will be checked, if this element is empty, then deletes it.
        """
    def generateSAXEvents(self, handler: 'XDocumentHandler_9b90e28', saxEventKeeperHandler: 'XDocumentHandler_9b90e28', startNode: 'XXMLElementWrapper_66c0107c', endNode: 'XXMLElementWrapper_66c0107c') -> None:
        """
        Converts a part of the DOM tree into SAX events.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    def getCurrentElement(self) -> 'XXMLElementWrapper_66c0107c':
        """
        Gets the current element.
        """
    def getNodeName(self, node: 'XXMLElementWrapper_66c0107c') -> str:
        """
        Gets the name of the element.
        """
    def getTree(self, handler: 'XDocumentHandler_9b90e28') -> None:
        """
        Converts the whole DOM tree into a SAX event stream.

        Raises:
            com.sun.star.xml.sax.SAXException: ``SAXException``
        """
    def isCurrent(self, node: 'XXMLElementWrapper_66c0107c') -> bool:
        """
        Checks whether an element is the current element.
        """
    def isCurrentElementEmpty(self) -> bool:
        """
        Checks whether the current element is empty.
        """
    def rebuildIDLink(self, node: 'XXMLElementWrapper_66c0107c') -> None:
        """
        Rebuild the ID attribute in the branch starting from the particular element.
        """
    def removeCurrentElement(self) -> None:
        """
        Removes the current element.
        
        When the current element is removed, then its parent element becomes the new current element.
        """
    def setCurrentElement(self, element: 'XXMLElementWrapper_66c0107c') -> None:
        """
        Sets the current element.
        
        When the current element is replaced outside of this interface, then uses this method can update the current element pointer.
        """

__all__ = ['XXMLDocumentWrapper']

