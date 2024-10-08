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

from ..task.x_interaction_continuation import XInteractionContinuation as XInteractionContinuation_5af0108e


class XInteractionFilterSelect(XInteractionContinuation_5af0108e):
    """
    continuation used by interaction mechanism at filter detection during loading documents
    
    If during loading time the filter can't be detected and wasn't given at calling time, a possible com.sun.star.task.InteractionHandler will be used. (it's a part of used MediaDescriptor) A NoSuchFilterRequest will be used then to start right interaction on that to get a decision which filter should be used for given URL. A possible continuation of that can be this XInteractionFilterSelect. It will transport the decision back to generic filter detection and force using of it. Of course it's possible to abort the loading process by use another continuation com.sun.star.task.XInteractionAbort.

    See Also:
        `API XInteractionFilterSelect <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XInteractionFilterSelect.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.document.XInteractionFilterSelect'

    def getFilter(self) -> str:
        """
        used by detection to get selected filter
        """
        ...
    def setFilter(self, Name: str) -> None:
        """
        used by interaction to set selected filter
        
        This value must be saved till another one will be set and must be provided on getFilter() for interest users.
        """
        ...


