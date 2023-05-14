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
# Namespace: com.sun.star.configuration
from .hierarchy_element import HierarchyElement as HierarchyElement_6fb410e9
from ..lang.x_component import XComponent as XComponent_98dc0ab5
from ..lang.x_localizable import XLocalizable as XLocalizable_aee00b64
from ..util.x_changes_notifier import XChangesNotifier as XChangesNotifier_e1b50d17

class AccessRootElement(HierarchyElement_6fb410e9, XComponent_98dc0ab5, XLocalizable_aee00b64, XChangesNotifier_e1b50d17):
    """
    Service Class

    provides information about the root element of a hierarchy and about the hierarchy as a whole.
    
    Provides information about the element and the whole hierarchy. Allows controlling the lifetime of the hierarchy. Allows observing changes in the hierarchy as a whole.
    
    When access to a hierarchy is first obtained from a factory or provider, this is the initial object that is created by the factory. It represents the root of the accessible part of the hierarchy.
    
    NOTE: In this description \"hierarchy\" may actually designate a part or fragment of a larger hierarchy. It is that part that is rooted in the element represented by an implementation of this service and that is accessible starting from this element.
    
    Generally it is not possible to navigate the parent or siblings, if any, of this element, so com.sun.star.container.XChild is not supported.

    See Also:
        `API AccessRootElement <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1AccessRootElement.html>`_
    """
    ...

