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
# Namespace: com.sun.star.document
from __future__ import annotations
import typing

from ..task.x_interaction_continuation import XInteractionContinuation as XInteractionContinuation_5af0108e
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73


class XInteractionFilterOptions(XInteractionContinuation_5af0108e):
    """
    A continuation to return filter options from interaction helper.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XInteractionFilterOptions <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1document_1_1XInteractionFilterOptions.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.document.XInteractionFilterOptions'

    def getFilterOptions(self) -> typing.Tuple[PropertyValue_c9610c73, ...]:
        """
        Get results from the continuation.
        """
        ...
    def setFilterOptions(self, rProperties: typing.Tuple[PropertyValue_c9610c73, ...]) -> None:
        """
        Store results to the continuation.
        """
        ...


