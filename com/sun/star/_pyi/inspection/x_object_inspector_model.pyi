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
# Namespace: com.sun.star.inspection
from typing_extensions import Literal
import typing
from abc import ABC
if typing.TYPE_CHECKING:
    from .property_category_descriptor import PropertyCategoryDescriptor as PropertyCategoryDescriptor_f4691406

class XObjectInspectorModel(ABC):
    """
    describes the model of an ObjectInspector
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API XObjectInspectorModel <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1inspection_1_1XObjectInspectorModel.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.inspection.XObjectInspectorModel']

    def describeCategories(self) -> 'typing.Tuple[PropertyCategoryDescriptor_f4691406, ...]':
        """
        describes the property categories used by the property handlers.
        
        Properties can be sorted into different categories, described by the LineDescriptor.Category attribute, which is filled in XPropertyHandler.describePropertyLine() method of your property handler.Those names provided by the handlers are programmatic names. All other information about categories is part of the PropertyCategoryDescriptor, and describeCategories() assembles information about all categories which all property handlers provided by the model use.
        """
        ...
    def getPropertyOrderIndex(self, PropertyName: str) -> int:
        """
        retrieves an index in a global property ordering, for a given property name
        
        In the user interface of an ObjectInspector, single properties are represented by single lines, and those lines are displayed successively. To determine an order of the property lines, the inspector model can associate an \"order index\" with each property. The ObjectInspector will then sort the property lines in a way that they have the same relative ordering as the \"order indexes\" of their properties.
        
        Note that the concrete value the model returns for a given property does not matter. All what matters is that if you want a certain property Foo to be displayed after another property Bar, then the order index of Foo should be greater than the order index of Bar.
        
        If for two different properties the same order index is returned, the ObjectInspector will assume the order in which those properties were provided by the respective property handler (XPropertyHandler.getSupportedProperties()).If two such properties originate from different handlers, they will be ordered according to the order of the handlers, as provided in the HandlerFactories attribute.
        """
        ...

    @property
    def HandlerFactories(self) -> 'typing.Tuple[object, ...]':
        """
        describes a set of factories for creating XPropertyHandlers
        
        Every element of the sequence must contain information to create a XPropertyHandler instance. Two ways are currently supported:
        
        This attribute is usually only evaluated by the ObjectInspector instance which the model is currently bound to.
        
        The order of factories is important: If two property handlers declare themselves responsible for the same property, the one whose factory is listed last wins. Also, if a handler B wants to supersede a property of another handler A, A's factory must precede the factory of B.
        """
        ...
    @HandlerFactories.setter
    def HandlerFactories(self, value: 'typing.Tuple[object, ...]') -> None:
        ...
    @property
    def HasHelpSection(self) -> bool:
        """
        indicates that the object inspector should have a help section.
        
        The object inspector displays lines of property/values, optionally grouped into categories, as described by the property handlers.Additionally, the inspector can optionally display a section dedicated to help texts. Clients could use this section to display context-sensitive help, for instance short texts explaining the currently selected property.
        
        **since**
        
            OOo 2.2
        """
        ...
    @HasHelpSection.setter
    def HasHelpSection(self, value: bool) -> None:
        ...
    @property
    def IsReadOnly(self) -> bool:
        """
        determines whether the object inspector's UI should be read-only.
        
        In this case, the user is able to browse through all properties, but cannot change any of them.
        
        In a read-only object inspector, the property controls are readonly or disabled themselves, and the primary and secondary buttons of a property line are both disabled.
        """
        ...
    @IsReadOnly.setter
    def IsReadOnly(self, value: bool) -> None:
        ...
    @property
    def MaxHelpTextLines(self) -> int:
        """
        denotes the maximum number of lines of text to be reserved for the help section.
        
        This property is ignored by the ObjectInspector if HasHelpSection is FALSE.
        
        The layout of the ObjectInspector is undefined if MaxHelpTextLines is smaller than MinHelpTextLines.
        
        **since**
        
            OOo 2.2
        """
        ...
    @MaxHelpTextLines.setter
    def MaxHelpTextLines(self, value: int) -> None:
        ...
    @property
    def MinHelpTextLines(self) -> int:
        """
        denotes the minimum number of lines of text to be reserved for the help section.
        
        This property is ignored by the ObjectInspector if HasHelpSection is FALSE.
        
        The layout of the ObjectInspector is undefined if MinHelpTextLines is larger than MaxHelpTextLines.
        
        **since**
        
            OOo 2.2
        """
        ...
    @MinHelpTextLines.setter
    def MinHelpTextLines(self, value: int) -> None:
        ...

