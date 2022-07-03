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
# Libre Office Version: 7.3
# Namespace: com.sun.star.document
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73
    from .x_storage_change_listener import XStorageChangeListener as XStorageChangeListener_7c7d1120
    from ..embed.x_storage import XStorage as XStorage_8e460a32

class XStorageBasedDocument(XInterface_8f010a43):
    """
    allows to initialize document with a storage, to store document to a storage, and to set document to be based on provided storage.

    See Also:
        `API XStorageBasedDocument <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XStorageBasedDocument.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.document.XStorageBasedDocument']

    def addStorageChangeListener(self, xListener: 'XStorageChangeListener_7c7d1120') -> None:
        """
        allows to register a listener that will be notified when another storage is set to the document.
        """
        ...
    def getDocumentStorage(self) -> 'XStorage_8e460a32':
        """
        allows to get the storage the document is based on.

        Raises:
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    def loadFromStorage(self, xStorage: 'XStorage_8e460a32', aMediaDescriptor: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        lets the document load itself using provided storage.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.frame.DoubleInitializationException: ``DoubleInitializationException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    def removeStorageChangeListener(self, xListener: 'XStorageChangeListener_7c7d1120') -> None:
        """
        allows to deregister the listener.
        """
        ...
    def storeToStorage(self, xStorage: 'XStorage_8e460a32', aMediaDescriptor: 'typing.Tuple[PropertyValue_c9610c73, ...]') -> None:
        """
        lets the document store itself to the provided storage.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...
    def switchToStorage(self, xStorage: 'XStorage_8e460a32') -> None:
        """
        allows to switch the document to the provided storage.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.uno.Exception: ``Exception``
        """
        ...


