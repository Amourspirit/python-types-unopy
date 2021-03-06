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
# Const
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.configuration.backend
from typing_extensions import Literal


class SchemaAttribute(object):
    """
    Const

    These values are used to specify the behavior of a node or property in the schema.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API SchemaAttribute <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1configuration_1_1backend_1_1SchemaAttribute.html>`_
    """
    REQUIRED: Literal[1]
    """
    indicates that a property value can't be null.
    """
    LOCALIZED: Literal[2]
    """
    indicates that the content of the node or the value of the property may depend on the locale.
    """
    EXTENSIBLE: Literal[4]
    """
    indicates that properties can be added to the node at runtime
    """
    MASK: Literal[255]
    """
    can be used to mask the schema attributes from merged attributes
    """

