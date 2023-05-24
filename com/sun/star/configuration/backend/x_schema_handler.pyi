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
# Namespace: com.sun.star.configuration.backend
from __future__ import annotations
import typing

from ...uno.x_interface import XInterface as XInterface_8f010a43
if typing.TYPE_CHECKING:
    from .template_identifier import TemplateIdentifier as TemplateIdentifier_2aaa14b5


class XSchemaHandler(XInterface_8f010a43):
    """
    receives a description of a configuration schema as a sequence of events.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API XSchemaHandler <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1XSchemaHandler.html>`_
    """
    __pyunointerface__: str = 'com.sun.star.configuration.backend.XSchemaHandler'

    def addInstance(self, aName: str, aTemplate: TemplateIdentifier_2aaa14b5) -> None:
        """
        receives notification that the current group has a child node that is an instance of a specified template.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def addItemType(self, aItemType: TemplateIdentifier_2aaa14b5) -> None:
        """
        receives notification that the current set can contain items that are instances of a specified template.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def addProperty(self, aName: str, aAttributes: int, aType: typing.Any) -> None:
        """
        receives notification that a property is added to the current node.
        
        The property will have a default value of NULL (unless it is SchemaAttribute.REQUIRED).
        
        The value is a combination of SchemaAttribute flags.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def addPropertyWithDefault(self, aName: str, aAttributes: int, aDefaultValue: typing.Any) -> None:
        """
        receives notification that a property having a default value is added to the current node.
        
        The value is a combination of SchemaAttribute flags.
        
        The value also determines the type. Therefore the value must not be VOID.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def endComponent(self) -> None:
        """
        receives notification that a component description is complete.
        
        Must match a previous call to startComponent().
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def endNode(self) -> None:
        """
        receives notification that a node description is complete.
        
        Must match the last open call to startGroup() or startSet().
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def endSchema(self) -> None:
        """
        receives notification that the current schema description is complete.
        
        Must match a previous call to startSchema().
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def endTemplate(self) -> None:
        """
        receives notification that a template description is complete.
        
        Must match a previous call to startGroupTemplate() or startSetTemplate().
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def importComponent(self, aName: str) -> None:
        """
        receives notification that the schema depends on templates from a different component.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def startComponent(self, aName: str) -> None:
        """
        receives notification that a component description is started.
        
        Subsequent calls describe the schema of the component until a matching call to endComponent() is encountered.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def startGroup(self, aName: str, aAttributes: int) -> None:
        """
        receives notification that a group description is started.
        
        Subsequent calls describe the members and properties of the group until a matching call to endNode() is encountered.
        
        The value is a combination of SchemaAttribute flags.
        
        SchemaAttribute.EXTENSIBLE can be used to describe a group with an extensible set of properties.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def startGroupTemplate(self, aTemplate: TemplateIdentifier_2aaa14b5, aAttributes: int) -> None:
        """
        receives notification that a template description is started for a group.
        
        Subsequent calls describe the members and properties of the template until a matching call to endTemplate() is encountered.
        
        The value is a combination of SchemaAttribute flags.
        
        SchemaAttribute.EXTENSIBLE can be used to describe a template for a node with an extensible set of properties.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def startSchema(self) -> None:
        """
        receives notification that a schema description is started.
        
        The schema description may comprise components templates or both.

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def startSet(self, aName: str, aAttributes: int, aItemType: TemplateIdentifier_2aaa14b5) -> None:
        """
        receives notification that a set description is started.
        
        Subsequent calls describe the item-types and properties of the set until a matching call to endNode() is encountered.
        
        The value is a combination of SchemaAttribute flags.
        
        SchemaAttribute.EXTENSIBLE can be used to describe a set with an extensible set of properties.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...
    def startSetTemplate(self, aTemplate: TemplateIdentifier_2aaa14b5, aAttributes: int, aItemType: TemplateIdentifier_2aaa14b5) -> None:
        """
        receives notification that a template description is started for a set.
        
        Subsequent calls describe the members and properties of the template until a matching call to endTemplate() is encountered.
        
        The value is a combination of SchemaAttribute flags.
        
        SchemaAttribute.EXTENSIBLE can be used to describe a template for a node with an extensible set of properties.
        
        Not every implementation can detect each condition

        Raises:
            MalformedDataException: ``MalformedDataException``
            com.sun.star.lang.WrappedTargetException: ``WrappedTargetException``
        """
        ...


