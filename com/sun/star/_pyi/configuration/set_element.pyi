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
# Libre Office Version: 7.3
# Namespace: com.sun.star.configuration
from .hierarchy_element import HierarchyElement as HierarchyElement_6fb410e9
from .x_template_instance import XTemplateInstance as XTemplateInstance_81181149
from ..lang.x_component import XComponent as XComponent_98dc0ab5

class SetElement(HierarchyElement_6fb410e9, XTemplateInstance_81181149, XComponent_98dc0ab5):
    """
    Service Class

    provides information about a dynamic element that can be inserted into a homogeneous set of elements within a hierarchy.
    
    Provides information about the element. Provides access to its containing set object. Allows controlling the lifetime of the element.
    
    Set elements may be added to and removed from the hierarchy at runtime. They bear user-defined names. They may exist independently, outside any container.
    
    New set element instances generally are created through members of com.sun.star.lang.XSingleServiceFactory or, if supported, com.sun.star.lang.XMultiServiceFactory on an implementation of SetUpdate. Initially, they are not contained in a set object and have no meaningful name.
    
    While an instance is not contained in a set object, it is owned by the client and can be disposed by calling com.sun.star.lang.XComponent.dispose(). The name of the object can freely be changed in that situation though without persistent effect.
    
    When the instance is inserted into a set (this includes replacing an existing element), ownership is transferred to the container. While it is contained in the container, clients must not dispose the object. When inserted, the name of the object is fixed and is used to identify it within the container. An implementation may support com.sun.star.container.XNamed.setName() even in this case. If it does, changing the name has the same effect of removing the object (under the old name) and then reinserting it into the same container (using the new name).
    
    When an instance is removed from a set (this includes being replaced by a new element), ownership is transferred to the client again. It can then be disposed or reinserted into a container. An instance can only be inserted into a container, if it was obtained from the same hierarchy.
    
    When a set element is removed from its set from outside the hierarchy, the container disposes of the object. This occurrence can be detected by registering a com.sun.star.lang.XEventListener with the object.
    
    If an implementation is part of a read-only view of the hierarchy, changing the name or parent is not supported (the object can't be removed from its container anyway).

    See Also:
        `API SetElement <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1configuration_1_1SetElement.html>`_
    """

