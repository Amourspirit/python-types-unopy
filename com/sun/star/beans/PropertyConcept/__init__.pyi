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
# Libre Office Version: 7.4
# Namespace: com.sun.star.beans
from typing_extensions import Literal
"""
Const

These constants are used to specify concepts of the introspection which apply to properties and to the methods which represent attributes.

This list is not necessarily complete; new constants may be added.

See Also:
    `API PropertyConcept <https://api.libreoffice.org/docs/idl/ref/namespacecom_1_1sun_1_1star_1_1beans_1_1PropertyConcept.html>`_
"""
ALL: Literal[-1]
"""
This value is used to query for all properties.

See XIntrospectionAccess.getProperty() and XIntrospectionAccess.getProperties()
"""
DANGEROUS: Literal[1]
"""
specifies that the change or retrieval of this property directly by the user can result in an unstable state (deadlock, application crash, security hole, etc.)
"""
PROPERTYSET: Literal[2]
"""
specifies all properties which are reachable by XPropertySet, XFastPropertySet or XMultiPropertySet.
"""
ATTRIBUTES: Literal[4]
"""
specifies all properties which are actually attributes of interfaces.
"""
METHODS: Literal[8]
"""
specifies all properties which are represented by getter or setter methods.

These methods have the signature type get...(), void set...() or boolean is...().
"""

