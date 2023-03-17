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
# Namespace: com.sun.star.document
from typing_extensions import Literal
import typing
from ..lang.x_event_listener import XEventListener as XEventListener_c7230c4a
if typing.TYPE_CHECKING:
    from .document_event import DocumentEvent as DocumentEvent_f21b0da8

class XDocumentEventListener(XEventListener_c7230c4a):
    """
    allows to be notified of events happening in an OfficeDocument
    
    This interface is the successor of the XEventListener interface, which should not be used anymore.
    
    **since**
    
        OOo 3.1

    See Also:
        `API XDocumentEventListener <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XDocumentEventListener.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.document.XDocumentEventListener']

    def documentEventOccured(self, Event: 'DocumentEvent_f21b0da8') -> None:
        """
        is called whenever a document event occurred
        """
        ...


