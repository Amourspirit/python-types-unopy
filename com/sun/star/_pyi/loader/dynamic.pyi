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
# Namespace: com.sun.star.loader
from .x_implementation_loader import XImplementationLoader as XImplementationLoader_498f0ff4

class Dynamic(XImplementationLoader_498f0ff4):
    """
    Service Class

    Makes it possible to access services accessible via a UnoUrlResolver E.g., instantiation of services in another process.
    
    This service is still in an experimental state and should not be used in a production environment.
    
    Is used to write persistent information into the given registry for accessing a SingleServiceFactory and for activating this implementation.
    
    Allows registration and activation of described service. The url parameter has to be a comma-separated list of attributes. The following attribute types are understood: servicename = the service name to register this component under link = a parameter given to a resolver to get a SingleServiceFactory resolver = a UnoUrlResolver service, which is used to resolve the link

    See Also:
        `API Dynamic <https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1loader_1_1Dynamic.html>`_
    """
    ...


