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
# Namespace: com.sun.star.configuration
from ..beans.x_hierarchical_property_set import XHierarchicalPropertySet as XHierarchicalPropertySet_679a10b9
from ..beans.x_multi_hierarchical_property_set import XMultiHierarchicalPropertySet as XMultiHierarchicalPropertySet_c18e12c4
from ..beans.x_multi_property_set import XMultiPropertySet as XMultiPropertySet_fd880e05
from ..beans.x_property_set import XPropertySet as XPropertySet_bc180bfa

class PropertyHierarchy(XHierarchicalPropertySet_679a10b9, XMultiHierarchicalPropertySet_c18e12c4, XMultiPropertySet_fd880e05, XPropertySet_bc180bfa):
    """
    Service Class

    provides access to and information about properties and subproperties of an implementation.
    
    Properties in a property set may be full-fledged objects that have properties themselves (and so on recursively), thereby forming a hierarchy of properties. This service describes such a hierarchy, and allows direct access even to subproperties.

    See Also:
        `API PropertyHierarchy <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1PropertyHierarchy.html>`_
    """
    ...


