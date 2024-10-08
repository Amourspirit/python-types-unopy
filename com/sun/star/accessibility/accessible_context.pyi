# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
# Namespace: com.sun.star.accessibility
from __future__ import annotations
from .x_accessible_context import XAccessibleContext as XAccessibleContext_8eae119b
from .x_accessible_event_broadcaster import XAccessibleEventBroadcaster as XAccessibleEventBroadcaster_3d811522

class AccessibleContext(XAccessibleContext_8eae119b, XAccessibleEventBroadcaster_3d811522):
    """
    Service Class

    Central service of the Accessibility API that gives access to various facets of an object's content.
    
    This service has to be implemented by every class that represents the actual accessibility information of another UNO service. It exposes two kinds of information: A tree structure in which all accessible objects are organized can be navigated in freely. It typically represents spatial relationship of one object containing a set of children like a dialog box contains a set of buttons. Additionally the XAccessibleContext interface of this service exposes methods that provide access to the actual object's content. This can be the object's role, name, description, and so on.
    
    **since**
    
        OOo 1.1.2

    See Also:
        `API AccessibleContext <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1accessibility_1_1AccessibleContext.html>`_
    """
    ...

