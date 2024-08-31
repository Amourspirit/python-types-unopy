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
# Namespace: com.sun.star.rdf
from __future__ import annotations
import typing

from .x_node import XNode as XNode_5ee40822
if typing.TYPE_CHECKING:
    from .xuri import XURI as XURI_5682078c


class XLiteral(XNode_5ee40822):
    """
    represents a literal that may occur in a RDF graph.
    
    RDF literals may come in three varieties:
    
    Note that there is no literal with both Language and Datatype.
    
    **since**
    
        OOo 3.0

    See Also:
        `API XLiteral <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rdf_1_1XLiteral.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.rdf.XLiteral'

    @property
    def Datatype(self) -> XURI_5682078c:
        """
        the data type of the literal; may be NULL
        """
        ...
    @Datatype.setter
    def Datatype(self, value: XURI_5682078c) -> None:
        ...
    @property
    def Language(self) -> str:
        """
        the language of the literal; may be the empty string
        """
        ...
    @Language.setter
    def Language(self, value: str) -> None:
        ...
    @property
    def Value(self) -> str:
        """
        the content of the literal
        """
        ...
    @Value.setter
    def Value(self, value: str) -> None:
        ...

