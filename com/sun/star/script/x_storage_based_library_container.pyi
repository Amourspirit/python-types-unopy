# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.script
from __future__ import annotations
import typing

from .x_persistent_library_container import XPersistentLibraryContainer as XPersistentLibraryContainer_b6b2129e
if typing.TYPE_CHECKING:
    from ..embed.x_storage import XStorage as XStorage_8e460a32


class XStorageBasedLibraryContainer(XPersistentLibraryContainer_b6b2129e):
    """
    is the interface for an XLibraryContainer which can be made persistent in a com.sun.star.embed.XStorage.
    
    A persistent library container is associated with a root storage. The container is responsible for a particular sub storage of the root storage, the container storage.
    
    **since**
    
        OOo 2.3

    See Also:
        `API XStorageBasedLibraryContainer <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1script_1_1XStorageBasedLibraryContainer.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.script.XStorageBasedLibraryContainer'

    def storeLibrariesToStorage(self, RootStorage: XStorage_8e460a32) -> None:
        """
        stores the libraries to a storage other than the current container storage
        
        Note that the library container is not automatically associated with the new root storage. Instead, you need to manually set the RootStorage attribute afterwards. This separation allows for Save-To as well Save-As operations.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...

    @property
    def RootStorage(self) -> XStorage_8e460a32:
        """
        denotes the root storage associated with the container.
        
        Effectively, this attribute is a typed version of XPersistentLibraryContainer.RootLocation, it's guaranteed that at every time, XPersistentLibraryContainer.RootLocation and RootStorage have the same value.
        
        You should only set this attribute to a new value if you previously called storeLibrariesToStorage with the same storage. Setting this attribute to a storage into which the container has not been stored previously might result in unexpected behavior.
        """
        ...
    @RootStorage.setter
    def RootStorage(self, value: XStorage_8e460a32) -> None:
        ...

