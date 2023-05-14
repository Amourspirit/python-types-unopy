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
# Namespace: com.sun.star.configuration.backend
from .layer import Layer as Layer_3d4f0f73
from .x_updatable_layer import XUpdatableLayer as XUpdatableLayer_ec97135d

class UpdatableLayer(Layer_3d4f0f73, XUpdatableLayer_ec97135d):
    """
    Service Class

    provides read/write access to a configuration data layer.
    
    A layer contains the configuration setting changes to be performed on a default layer (or schema) to obtain the values of those settings for a given entity and component.
    
    An updatable layer can be read or replaced with another layer.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API UpdatableLayer <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1UpdatableLayer.html>`_
    """
    ...

