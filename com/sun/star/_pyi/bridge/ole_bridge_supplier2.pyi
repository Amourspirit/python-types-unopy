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
# Namespace: com.sun.star.bridge
from .x_bridge_supplier2 import XBridgeSupplier2 as XBridgeSupplier2_fb800da0

class OleBridgeSupplier2(XBridgeSupplier2_fb800da0):
    """
    Service Class

    maps UNO types to oleautomation types and vice versa.
    
    The XBridgeSupplier2 interface provides the function createBridge which maps a value of a UNO or Automation type to the desired target type. If a UNO interface was mapped to IDispatch, then all objects (interfaces, structs) and other types which are obtained from that Automation object are automatically mapped to the corresponding Automation types. Hence, if one provides an initial object which forms the root of all other objects, such as a service manager, then only that object needs to be explicitly mapped by a call to createBridge. The same holds true if an automation object is mapped to a UNO interface.
    
    The Automation types VT_CY and VT_DATE are not supported. For Automation objects to be mapped they have to implement IDispatch interface. Other COM interfaces, except for IUnknown, are not supported.UNO interfaces and structs are mapped to IDispatch.
    
    The service implements the XBridgeSupplier2 interface and handles the model types com.sun.star.bridge.ModelDependent.UNO and com.sun.star.bridge.ModelDependent.OLE. The service does not specify any requirements for registering OLE objects and class factories.
    
    .. deprecated::
    
        Class is deprecated.

    See Also:
        `API OleBridgeSupplier2 <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1bridge_1_1OleBridgeSupplier2.html>`_
    """
    ...


