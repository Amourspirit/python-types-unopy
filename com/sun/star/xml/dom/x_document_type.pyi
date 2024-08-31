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
# Namespace: com.sun.star.xml.dom
from __future__ import annotations
import typing

from .x_node import XNode as XNode_83fb09a5
if typing.TYPE_CHECKING:
    from .x_named_node_map import XNamedNodeMap as XNamedNodeMap_de600ca8


class XDocumentType(XNode_83fb09a5):
    """

    See Also:
        `API XDocumentType <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1xml_1_1dom_1_1XDocumentType.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.xml.dom.XDocumentType'

    def getEntities(self) -> XNamedNodeMap_de600ca8:
        """
        A NamedNodeMap containing the general entities, both external and internal, declared in the DTD.
        """
        ...
    def getInternalSubset(self) -> str:
        """
        The internal subset as a string, or null if there is none.
        """
        ...
    def getName(self) -> str:
        """
        The name of DTD; i.e., the name immediately following the DOCTYPE keyword.
        """
        ...
    def getNotations(self) -> XNamedNodeMap_de600ca8:
        """
        A NamedNodeMap containing the notations declared in the DTD.
        """
        ...
    def getPublicId(self) -> str:
        """
        The public identifier of the external subset.
        """
        ...
    def getSystemId(self) -> str:
        """
        The system identifier of the external subset.
        """
        ...


