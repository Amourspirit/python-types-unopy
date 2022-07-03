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
# Namespace: com.sun.star.accessibility
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from ..beans.property_value import PropertyValue as PropertyValue_c9610c73

class XAccessibleTextAttributes(ABC):
    """
    Implement this interface to give access to the attributes of a text.
    
    **since**
    
        OOo 2.0.4

    See Also:
        `API XAccessibleTextAttributes <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1accessibility_1_1XAccessibleTextAttributes.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.accessibility.XAccessibleTextAttributes']

    def getDefaultAttributes(self, RequestedAttributes: 'typing.Tuple[str, ...]') -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        Get the default attribute set for the text.
        
        Returns a set of all default paragraph and default character attributes that are associated for the text. To prevent the method from returning possibly large sets of attributes that the caller is not interested in the caller can provide a list of attributes that he wants to be returned.
        
        When the sequence is empty all attributes are returned.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
        """
        ...
    def getRunAttributes(self, Index: int, RequestedAttributes: 'typing.Tuple[str, ...]') -> 'typing.Tuple[PropertyValue_c9610c73, ...]':
        """
        Get the run attribute set for the specified position.
        
        Returns a set of character attributes that are associated for the character at the given index and are directly set or are set via a character style. To prevent the method from returning all of these attributes the caller can provide a list of attributes that he wants to be returned.
        
        When the sequence is empty all attributes are returned.

        Raises:
            com.sun.star.beans.UnknownPropertyException: ``UnknownPropertyException``
            com.sun.star.lang.IndexOutOfBoundsException: ``IndexOutOfBoundsException``
        """
        ...


