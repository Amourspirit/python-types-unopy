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
# Service Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.2
# Namespace: com.sun.star.registry
from ..lang.x_initialization import XInitialization as XInitialization_d46c0cca
from .x_simple_registry import XSimpleRegistry as XSimpleRegistry_10150e9c

class NestedRegistry(XInitialization_d46c0cca, XSimpleRegistry_10150e9c):
    """
    Service Class

    supports a shared view on two different registries.
    
    The registry files will be opened in two different modes, registry1 will be opened with read/write rights and registry2 will be opened read-only. In the context of this service, the functions open, close, and destroy from XSimpleRegistry are not supported and throw an exception if they are used.
    
    Functions of XSimpleRegistry:
    
    Functions of XRegistryKey:
    
    How to initialize the registries:Use a sequence of XSimpleRegistry with two elements. The first element must be the registry which is opened with read/write rights and the second element must be the read-only one.Two different ways are possible:
    
    Guarantees:

    See Also:
        `API NestedRegistry <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1registry_1_1NestedRegistry.html>`_
    """
    ...


