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
# Exception Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.task
# Libre Office Version: 2024.2
from typing_extensions import Literal
import typing
from .classified_interaction_request import ClassifiedInteractionRequest as ClassifiedInteractionRequest_9f72121b
from ..uno.x_interface import XInterface as XInterface_8f010a43
from .interaction_classification import InteractionClassification as InteractionClassification_6c4d10e7
from ..embed.x_storage import XStorage as XStorage_8e460a32
from ..security.document_signature_information import DocumentSignatureInformation as DocumentSignatureInformation_f36c13f7

class DocumentMacroConfirmationRequest(ClassifiedInteractionRequest_9f72121b):
    """
    Exception Class

    describes the request to approve or deny the execution of macros contained in a document.

    See Also:
        `API DocumentMacroConfirmationRequest <https://api.libreoffice.org/docs/idl/ref/exceptioncom_1_1sun_1_1star_1_1task_1_1DocumentMacroConfirmationRequest.html>`_
    """

    typeName: Literal['com.sun.star.task.DocumentMacroConfirmationRequest']

    def __init__(self, Message: typing.Optional[str] = ..., Context: typing.Optional[XInterface_8f010a43] = ..., Classification: typing.Optional[InteractionClassification_6c4d10e7] = ..., DocumentURL: typing.Optional[str] = ..., DocumentStorage: typing.Optional[XStorage_8e460a32] = ..., DocumentVersion: typing.Optional[str] = ..., DocumentSignatureInformation: typing.Optional[typing.Tuple[DocumentSignatureInformation_f36c13f7, ...]] = ...) -> None:
        """
        Constructor

        Arguments:
            Message (str, optional): Message value.
            Context (XInterface, optional): Context value.
            Classification (InteractionClassification, optional): Classification value.
            DocumentURL (str, optional): DocumentURL value.
            DocumentStorage (XStorage, optional): DocumentStorage value.
            DocumentVersion (str, optional): DocumentVersion value.
            DocumentSignatureInformation (typing.Tuple[DocumentSignatureInformation, ...], optional): DocumentSignatureInformation value.
        """
        ...
    @property
    def DocumentURL(self) -> str:
        """
        specifies the URL of the document which contains macros whose execution should be approved or rejected.
        """
        ...
    @DocumentURL.setter
    def DocumentURL(self, value: str) -> None:
        ...
    @property
    def DocumentStorage(self) -> XStorage_8e460a32:
        """
        refers to the storage related to the last committed version of the document.
        
        This storage is necessary e.g. for displaying the existing signatures to the user, to allow him a decision whether or not to trust those signatures and thus the signed macros.
        """
        ...
    @DocumentStorage.setter
    def DocumentStorage(self, value: XStorage_8e460a32) -> None:
        ...
    @property
    def DocumentVersion(self) -> str:
        """
        contains information about the ODF version of the document
        """
        ...
    @DocumentVersion.setter
    def DocumentVersion(self, value: str) -> None:
        ...
    @property
    def DocumentSignatureInformation(self) -> typing.Tuple[DocumentSignatureInformation_f36c13f7, ...]:
        """
        contains information about the signatures in the document
        """
        ...
    @DocumentSignatureInformation.setter
    def DocumentSignatureInformation(self, value: typing.Tuple[DocumentSignatureInformation_f36c13f7, ...]) -> None:
        ...

__all__ = ['DocumentMacroConfirmationRequest']

