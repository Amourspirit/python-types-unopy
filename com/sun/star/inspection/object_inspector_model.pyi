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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.4
# Namespace: com.sun.star.inspection
from __future__ import annotations
import typing
from .x_object_inspector_model import XObjectInspectorModel as XObjectInspectorModel_9077119b

class ObjectInspectorModel(XObjectInspectorModel_9077119b):
    """
    Service Class

    describes a default implementation of an ObjectInspectorModel
    
    This service simplifies usage of an ObjectInspector.
    
    The XObjectInspectorModel implemented by this service will not provide any property categories, nor apply any particular order to the properties provided by its handler(s).
    
    **since**
    
        OOo 2.0.3

    See Also:
        `API ObjectInspectorModel <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1inspection_1_1ObjectInspectorModel.html>`_
    """
    def createDefault(self) -> None:
        """
        creates a default ObjectInspectorModel, whose one and only handler factory creates a GenericPropertyHandler.
        """
        ...
    def createWithHandlerFactories(self, handlerFactories: typing.Tuple[object, ...]) -> None:
        """
        creates a default ObjectInspectorModel, using an externally provided sequence of property handler factories.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...
    def createWithHandlerFactoriesAndHelpSection(self, handlerFactories: typing.Tuple[object, ...], minHelpTextLines: int, maxHelpTextLines: int) -> None:
        """
        creates a default ObjectInspectorModel, using an externally provided sequence of property handler factories, and describing an ObjectInspector which has a help section.
        
        **since**
        
            OOo 2.2

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
        ...

