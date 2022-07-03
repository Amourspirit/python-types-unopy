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
# Namespace: com.sun.star.rdf
from typing_extensions import Literal
import typing
from .x_repository_supplier import XRepositorySupplier as XRepositorySupplier_feff0e30
from .xuri import XURI as XURI_5682078c
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from ..beans.string_pair import StringPair as StringPair_a4bc0b14
    from ..embed.x_storage import XStorage as XStorage_8e460a32
    from ..io.x_input_stream import XInputStream as XInputStream_98d40ab4
    from .x_metadatable import XMetadatable as XMetadatable_a3000af0
    from ..task.x_interaction_handler import XInteractionHandler as XInteractionHandler_bf80e51

class XDocumentMetadataAccess(XRepositorySupplier_feff0e30, XURI_5682078c):
    """
    document metadata functionality related to the \"manifest.rdf\".
    
    This interface contains some methods that create connections between the content and the RDF metadata of an ODF document. The main idea is to make querying and manipulating the data in the metadata manifest easier.
    
    Note that this interface inherits from XURI: the base URI of the document is the string value of the RDF node. This is so that you can easily make RDF statements about the document.
    
    **since**
    
        OOo 3.2

    See Also:
        `API XDocumentMetadataAccess <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rdf_1_1XDocumentMetadataAccess.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.rdf.XDocumentMetadataAccess']

    def addContentOrStylesFile(self, FileName: str) -> None:
        """
        add a content or styles file to the manifest.
        
        This convenience method adds the required statements declaring a content or styles file to the manifest graph.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """
        ...
    def addMetadataFile(self, FileName: str, Types: 'typing.Tuple[XURI_5682078c, ...]') -> 'XURI_5682078c':
        """
        add a metadata file to the manifest.
        
        This convenience method does the following:

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
        """
        ...
    def getElementByMetadataReference(self, MetadataReference: 'StringPair_a4bc0b14') -> 'XMetadatable_a3000af0':
        """
        get the unique ODF element with the given metadata reference.
        """
        ...
    def getElementByURI(self, URI: 'XURI_5682078c') -> 'XMetadatable_a3000af0':
        """
        get the ODF element that corresponds to a URI.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def getMetadataGraphsWithType(self, Type: 'XURI_5682078c') -> 'typing.Tuple[XURI_5682078c, ...]':
        """
        get the names of all metadata files with a given type.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def importMetadataFile(self, Format: int, InStream: 'XInputStream_98d40ab4', FileName: str, BaseURI: 'XURI_5682078c', Types: 'typing.Tuple[XURI_5682078c, ...]') -> 'XURI_5682078c':
        """
        import a metadata file into the document repository, and add it to the manifest.
        
        This convenience method does the following:

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.datatransfer.UnsupportedFlavorException: ``UnsupportedFlavorException``
            com.sun.star.container.ElementExistException: ``ElementExistException``
            ParseException: ``ParseException``
            com.sun.star.io.IOException: ``IOException``
        """
        ...
    def loadMetadataFromMedium(self, Medium: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        loads document metadata from a medium.
        
        If the Medium contains an InteractionHandler, it will be used for error reporting.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def loadMetadataFromStorage(self, Storage: 'XStorage_8e460a32', BaseURI: 'XURI_5682078c', InteractionHandler: 'XInteractionHandler_bf80e51') -> None:
        """
        initialize document metadata from a storage.
        
        This method re-initializes the document metadata, loads the stream named \"manifest.rdf\" from the storage, and then loads all metadata streams mentioned in the manifest.
        
        Note that it is not an error if the storage does not contain a manifest. In this case, the document metadata will be default initialized.
        
        If an InteractionHandler argument is given, it will be used for error reporting. Otherwise, errors will be reported as exceptions.
        
        N.B.: when loading from an ODF package, the base URI is not the URI of the package, but the URI of the directory in the package that contains the metadata.rdf

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def removeContentOrStylesFile(self, FileName: str) -> None:
        """
        remove a content or styles file from the manifest.
        
        This convenience method removes the statements declaring a content or styles file from the manifest graph.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    def removeMetadataFile(self, GraphName: 'XURI_5682078c') -> None:
        """
        remove a metadata file from the manifest and the repository.
        
        This convenience method does the following:

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.container.NoSuchElementException: ``NoSuchElementException``
        """
        ...
    def storeMetadataToMedium(self, Medium: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        stores document metadata to a medium.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def storeMetadataToStorage(self, Storage: 'XStorage_8e460a32') -> None:
        """
        store document metadata to a storage.
        
        This method stores all the graphs in the document metadata repository to the given storage.
        
        Note that to be stored correctly, a named graph must have a complete entry in the manifest graph.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...


