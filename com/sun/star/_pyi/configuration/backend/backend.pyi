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
# Namespace: com.sun.star.configuration.backend
from .x_backend import XBackend as XBackend_6ce81076
from .x_backend_entities import XBackendEntities as XBackendEntities_fecf13bb
from .x_schema_supplier import XSchemaSupplier as XSchemaSupplier_eca11373

class Backend(XBackend_6ce81076, XBackendEntities_fecf13bb, XSchemaSupplier_eca11373):
    """
    Service Class

    provides access to a configuration database composed of one or more storage backends containing settings used by software modules.
    
    Configuration data is organized into layers which are selected by components and entities.
    
    Components are characterized by configuration schemas. A component contains configuration data for a particular application domain or software module.
    
    Entities are organized hierarchically in organizations, groups, roles and individual users. Each element of the associated hierarchy corresponds to a layer that applies to an entity.
    
    A layer contains data for multiple components associated to a single entity.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API Backend <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1Backend.html>`_
    """
    ...


