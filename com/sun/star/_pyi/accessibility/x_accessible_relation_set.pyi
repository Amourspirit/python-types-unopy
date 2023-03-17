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
# Namespace: com.sun.star.accessibility
from typing_extensions import Literal
import typing
from ..uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .accessible_relation import AccessibleRelation as AccessibleRelation_8f8b119c

class XAccessibleRelationSet(XInterface_8f010a43):
    """
    Implement this interface to give access to an object's set of relations.
    
    Such relation are modeled with the AccessibleRelation structure. This interface is used for representing sets of relations between Accessible objects. Most of the convenience methods of the corresponding AccessibleRelationSet interface of the Java Accessibility API have been removed from this interface in order to clean it up. These methods are add(), addAll(), clear(), and remove(). The other methods have been renamed to achieve a greater conformance with the other accessibility interfaces.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XAccessibleRelationSet <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleRelationSet.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.accessibility.XAccessibleRelationSet']

    def containsRelation(self, aRelationType: int) -> bool:
        """
        Tests whether the relation set contains a relation matching the specified key.
        """
        ...
    def getRelation(self, nIndex: int) -> 'AccessibleRelation_8f8b119c':
        """
        Returns the relation of this relation set that is specified by the given index.

        Raises:
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...
    def getRelationByType(self, aRelationType: int) -> 'AccessibleRelation_8f8b119c':
        """
        Retrieve and return the relation with the given relation type.
        """
        ...
    def getRelationCount(self) -> int:
        """
        Returns the number of relations in this relation set.
        """
        ...


