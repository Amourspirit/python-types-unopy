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
# Namespace: com.sun.star.ucb
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .x_content import XContent as XContent_79db0975
    from .x_content_identifier import XContentIdentifier as XContentIdentifier_edc90d78

class XContentIdentifierMapping(XInterface_8f010a43):
    """
    A mapping from a (source) set of XContentIdentifiers to another (target) set of XContentIdentifiers.
    
    For convenience and performance, mapping between the string representations of source/target XContentIdentifiers, as well as mapping between XContents identified by source/target XContentIdentifiers is also supported.
    
    This interface can be useful in cases where the identifiers (and associated contents) returned by the various methods of an XContentAccess need to be mapped to some other space of identifiers (and associated contents).

    See Also:
        `API XContentIdentifierMapping <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1ucb_1_1XContentIdentifierMapping.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.ucb.XContentIdentifierMapping']

    def mapContent(self, Source: 'XContent_79db0975') -> 'XContent_79db0975':
        """
        Map the XContent identified by an XContentIdentifier.
        """
        ...
    def mapContentIdentifier(self, Source: 'XContentIdentifier_edc90d78') -> 'XContentIdentifier_edc90d78':
        """
        Map an XContentIdentifier.
        """
        ...
    def mapContentIdentifierString(self, Source: str) -> str:
        """
        Map the string representation of an XContentIdentifier.
        """
        ...
    def mapRow(self, Value: object) -> bool:
        """
        Map the content identifiers (or related data) contained in the columns of a com.sun.star.sdbc.XRow.
        """
        ...


