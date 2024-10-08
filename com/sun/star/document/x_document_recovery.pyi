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
# Namespace: com.sun.star.document
from __future__ import annotations
import typing

from abc import ABC
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73


class XDocumentRecovery(ABC):
    """
    is the interface to be implemented by documents who wish to participate in the document emergency-save / recovery process.

    See Also:
        `API XDocumentRecovery <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XDocumentRecovery.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.document.XDocumentRecovery'

    def recoverFromFile(self, SourceLocation: str, SalvagedFile: str, MediaDescriptor: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        """
        recovers the document after a previous emergency or session save.
        
        The document itself has previously been created, but not loaded (via com.sun.star.frame.XLoadable.load()) or initialized (via com.sun.star.frame.XLoadable.initNew()).
        
        Upon successful return, the document must be fully initialized. In particular, the caller is not responsible for calling com.sun.star.frame.XModel.attachResource(). Instead, the implementation is responsible to do so, if required.
        
        A default implementation of this method could simply delegate this call to com.sun.star.frame.XLoadable.load(), followed by com.sun.star.frame.XModel.attachResource().

        Raises:
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def storeToRecoveryFile(self, TargetLocation: str, MediaDescriptor: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        """
        does an emergency save of the document
        
        A default implementation of this method could simply delegate this call to com.sun.star.frame.XStorable.storeToURL().

        Raises:
            com.sun.star.io.IOException: ``IOException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def wasModifiedSinceLastSave(self) -> bool:
        """
        determines whether the document has been modified since the last call to storeToRecoveryFile().
        
        If storeToRecoveryFile has not been called before, this method returns whether the document has been modified since it has been loaded respectively created.
        
        When saving a session, either in case of an emergency (when OpenOffice.org crashed), or during a periodic session save as configured by the user, storeToRecoveryFile() is called for every document where wasModifiedSinceLastSave returns TRUE.
        
        It's allowed to implement this method sloppy, by returning TRUE in cases where it is not sure whether the document actually has been modified. So, the most simple implementation could simply delegate this call to com.sun.star.util.XModifiable.isModified(). (Well, actually that's the second simple implementation, the most simple one would, still legitimately, always return TRUE.)
        
        However, in such a case, the document might be saved more often than needed. In particular during the periodic session save, this might become a problem when saving is expensive, for a single document or the sum of all open documents.
        """
        ...


